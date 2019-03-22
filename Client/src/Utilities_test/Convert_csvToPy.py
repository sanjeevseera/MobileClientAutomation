"""
Reads input from Test_cases.csv and creates a new file test_case.py
"""
import sys
import os
import configparser
from time import sleep
import subprocess
import platform
import inspect
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from template.cases_template import test_case_dict
from Utilities_support.log_writer import log_print
from Utilities_support.Client import remote_command


required_imports = """import sys
import os
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from Utilities.base_setup import BaseSetup
from Utilities.Test_flow import TestFlow
from Utilities_support.report_email import email_reporter
from Utilities_support.log_writer import log_print
import unittest
import warnings
import HtmlTestRunner


"""
unittest_code = """\n\nif __name__ == "__main__":
    template = "src/template/report_template.html"
    report_title = "Test Report"
    html_report_dir = r"../report/"
    #if not path.isdir(html_report_dir):
    #    os.mkdir(html_report_dir)

    test_suite = unittest.TestSuite()
    test = unittest.makeSuite(Test_SuitXYZ)
    test_suite.addTest(test)
    test_runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir, verbosity=2, report_title=report_title, template=template)
    test_runner.run(test_suite)
    report_status = email_reporter(html_report_dir.split('/', 1)[-1])
    log_print("info", "report_status:: "+str(report_status))
    #email_reporter(html_report_dir)

    #suite = unittest.TestLoader().loadTestsFromTestCase(Test_SuitXYZ)
    #unittest.TextTestRunner(verbosity=2).run(suite)
"""

Config_file = r'src/Appium_configs/config_general.py'
testCases_file = r'src/Utilities_test/test_cases_csv.py'

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception('Argument is Missing or There are more\nExample: python Convert_csvToPy.py Test_cases.csv')
        elif not os.path.isfile(sys.argv[1]):
            raise Exception('The file Provided as Argument is not exist in the path')
        else:
            with open(testCases_file, "w") as nw_file, open(Config_file, "w") as cn_file:
                nw_file.write(required_imports)
                Test_suite = "Test_suite"
                add_class_str = ""
                test_count = 1
                with open(sys.argv[1], 'r') as csv_file:
                    for fdata in csv_file.readlines():
                        fdata_list = fdata.split(',')
                        if fdata_list[0].rstrip().lower() == "test_suit":
                            unittest_code = unittest_code.replace('Test_SuitXYZ', fdata_list[1].rstrip())
                            Test_suite = fdata_list[1].rstrip()
                        elif fdata_list[0].rstrip().lower() == "config":
                            if "appium" in fdata_list[1].rstrip().lower():
                                cn_file.write("{0} = \"{1}\"\n".format(fdata_list[1].rstrip(), fdata_list[2].rstrip()))
                            else:
                                nw_file.write("{0} = \"{1}\"\n".format(fdata_list[1].rstrip(), fdata_list[2].rstrip()))
                        elif fdata_list[0].rstrip().lower() is not "":
                            if add_class_str == "":
                                add_class_str += "\n\nclass {0}(BaseSetup, TestFlow):\n".format(Test_suite)

                            try:
                                test_template = test_case_dict[fdata_list[1].rstrip()[1:-1]]
                                test_parm_str = ""
                                for i, param in enumerate(test_template):
                                    if i+2 < len(fdata_list):
                                        if fdata_list[i+2].rstrip() == "" and param[1] == 'MANDATE':
                                            test_parm_str += ", {}={}".format(param[0], "\"\"")
                                        elif fdata_list[i+2].rstrip() == "" and param[1] == 'OPTIONAL':
                                            pass
                                        else:
                                            test_parm_str += ", {}={}".format(param[0], fdata_list[i + 2].rstrip())
                                    elif param[1] == 'MANDATE':
                                        log_print("WARNING", "Can not add test case::{}, some parameters are missing\n".format(fdata_list[0].rstrip()))
                                        test_parm_str = ""

                                if test_parm_str != "":
                                    add_class_str += "\n{0}def test{1}_{2}(self):\n".format(" " * 4, test_count, fdata_list[0])
                                    test_count += 1
                                    add_class_str += "{0}warnings.simplefilter('ignore')\n".format(" " * 8)
                                    add_class_str += "{0}self.assertTrue(TestFlow.{1}(self".format(" " * 8,fdata_list[1][1:-1].rstrip())
                                    add_class_str += test_parm_str + "))\n"
                            except KeyError:
                                log_print("WARNING", "The test case::{} is not supported\n".format(fdata_list[0].rstrip()))


                nw_file.write(add_class_str)
                nw_file.write(unittest_code)

        sleep(5)

        from Appium_configs.config_general import *  # don't move from here, this should be imported after above code executed
        if "win" in Appium_Server.lower():
            netstat_cmd = 'netstat -ano | find "' + Appium_Port + '"'
        elif "mac" in Appium_Server.lower():
            netstat_cmd = 'netstat -an | grep "' + Appium_Port + '"'
        else:
            netstat_cmd = 'netstat -anp | grep "' + Appium_Port + '"'
        log_print("INFO", "netstat command:: "+netstat_cmd)
        result_out = remote_command(netstat_cmd, Appium_IP)
        print("INFO", "netstat command output :: "+result_out)
        if "returned non-zero exit status" not in result_out:
            if platform.system().lower() == "windows":
                result_out = subprocess.check_output('python ' + testCases_file).decode().split('\n')
            elif platform.system().lower() == "darwin":
                subprocess.call('python ' + testCases_file, shell=True)
            else:
                subprocess.call('python ' + testCases_file, shell=True)
        else:
            raise Exception(str(result_out))

    except Exception as e:
        log_print("ERROR", "Exception: {}".format(e))
    except IndexError as e:
        log_print("ERROR", "IndexError: {}".format(e))
    except KeyboardInterrupt as e:
        log_print("ERROR", "KeyboardInterrupt: {}".format(e))
        sys.exit()
