"""
Reads input from Test_cases.cfg and creates a new file test_case.py
"""
import sys
import os
import configparser
from time import sleep
import subprocess
import platform

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

testCases_file = r'src/Utilities_test/test_cases_cfg.py'

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception('Argument is Missing or There are more\nExample: python Convert_cfgToPy.py Test_cases.cfg')
        elif not os.path.isfile(sys.argv[1]):
            raise Exception('The file Provided as Argument is not exist in the path')
        else:
            with open(testCases_file, "w") as nw_file:
                nw_file.write(required_imports)
                testCases = configparser.ConfigParser()
                testCases.read(sys.argv[1])
                Test_suite = "Test_suite"
                for i, t_case in enumerate(testCases.sections()):
                    if i == 0 and t_case.lower() == "config":
                        for item in testCases.items(t_case):
                            if item[0].lower() == "test_suit":
                                Test_suite = item[1]
                                if "'" in Test_suite or "\"" in Test_suite:
                                    Test_suite = Test_suite[1:-1]
                            else:
                                nw_file.write("{0} = {1}\n".format(item[0],item[1]))
                        add_str = "\n\nclass "+Test_suite+"(BaseSetup,TestFlow):\n"
                        nw_file.write(add_str)
                    elif i == 0 and t_case.lower() != "config":
                        add_str = "class " + Test_suite + "(BaseSetup, TestFlow):\n"
                        nw_file.write(add_str)
                    else:
                        for j, item in enumerate(testCases.items(t_case)):
                            if j == 0 and item[0].lower() == "test_case":
                                if "'" in item[1]:
                                    item_val = item[1][1:-1]
                                else:
                                    item_val = item[1]
                                add_str="\n{0}def test{1}_{2}(self):\n".format(" "*4,i,item_val.lower())
                                add_str+="{0}warnings.simplefilter('ignore')\n".format(" "*8)
                                add_str+="{0}self.assertTrue(TestFlow.{1}(self".format(" "*8,item_val)
                            elif j == 0 and item[0].lower() != "test_case":
                                break
                            else:
                                add_str +=",{0}={1}".format(item[0],item[1])
                        add_str = add_str + "))\n"
                        nw_file.write(add_str)
                        add_str=""
                unittest_code = unittest_code.replace('Test_SuitXYZ',Test_suite)
                nw_file.write(unittest_code)

        sleep(5)
        if platform.system().lower() == "windows":
            result_out = subprocess.check_output('python '+testCases_file).decode().split('\n')
        elif platform.system().lower() == "darwin":
            subprocess.call('python '+testCases_file, shell=True)
        else:
            subprocess.call('python '+testCases_file, shell=True)

    except Exception as e:
        print("Exception: {}".format(e))
    except IndexError as e:
        print("IndexError: {}".format(e))
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt: {}".format(e))
        sys.exit()
