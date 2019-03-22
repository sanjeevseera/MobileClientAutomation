import sys
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


orig_id = "user5"
orig_pass = "1234"
term_id = "user4"
term_pass = "1234"


class OTT_Client(BaseSetup, TestFlow):

    def test1_Login_out_orig(self):
        warnings.simplefilter('ignore')
        self.assertTrue(TestFlow.Login_out(self, platform=Android, user_id=orig_id, user_pass=orig_pass))

    def test2_Login_out_term(self):
        warnings.simplefilter('ignore')
        self.assertTrue(TestFlow.Login_out(self, platform=Android, user_id=term_id, user_pass=term_pass))

    def test3_Basic_Call(self):
        warnings.simplefilter('ignore')
        self.assertTrue(TestFlow.Basic_Call(self, platform=Android-Android, orig_id=orig_id, orig_pass=orig_pass, term_id=term_id, term_pass=term_pass))

    def test4_Basic_Messaging(self):
        warnings.simplefilter('ignore')
        self.assertTrue(TestFlow.Basic_Messaging(self, platform=Android-Android, orig_id=orig_id, orig_pass=orig_pass, term_id=term_id, term_pass=term_pass))


if __name__ == "__main__":
    template = "src/template/report_template.html"
    report_title = "Test Report"
    html_report_dir = r"../report/"
    #if not path.isdir(html_report_dir):
    #    os.mkdir(html_report_dir)

    test_suite = unittest.TestSuite()
    test = unittest.makeSuite(OTT_Client)
    test_suite.addTest(test)
    test_runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir, verbosity=2, report_title=report_title, template=template)
    test_runner.run(test_suite)
    report_status = email_reporter(html_report_dir.split('/', 1)[-1])
    log_print("info", "report_status:: "+str(report_status))
    #email_reporter(html_report_dir)

    #suite = unittest.TestLoader().loadTestsFromTestCase(OTT_Client)
    #unittest.TextTestRunner(verbosity=2).run(suite)
