from Client.src.Utilities.base_setup import BaseSetup
from Client.src.Utilities.Test_flow import TestFlow
import unittest
#import warnings

orig_id = "user5"
orig_pass = "1234"
term_id = "user4"
term_pass = "1234"


class UCC_Testcases(BaseSetup,TestFlow):

    def test1_login_out(self):
        self.assertTrue(TestFlow.Login_out(self,platform='Android',user_id=orig_id,user_pass=orig_pass))

    def test2_login_out(self):
        self.assertTrue(TestFlow.Login_out(self,platform='Android',user_id=term_id,user_pass=term_pass))

    def test3_basic_call(self):
        self.assertTrue(TestFlow.Basic_Call(self,platform='Android-Android',orig_id=orig_id,orig_pass=orig_pass,
                                            term_id=term_id,term_pass=term_pass))
    def test4_basic_msg(self):
        self.assertTrue(TestFlow.Basic_Messaging(self, platform='Android-Android', orig_id=orig_id, orig_pass=orig_pass,
                                                 term_id=term_id, term_pass=term_pass))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UCC_Testcases)
    unittest.TextTestRunner(verbosity=2).run(suite)