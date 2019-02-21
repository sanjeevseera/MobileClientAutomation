from Client.src.Utilities.base_setup import BaseSetup
from Client.src.Utilities.Test_flow import TestFlow
from time import sleep
import unittest
import warnings

orig_id = "user5"
orig_pass = "1234"
term_id = "user4"
term_pass = "1234"


class UCC_Testcases(BaseSetup,TestFlow):

    def test1_login_out(self):
        warnings.simplefilter('ignore')
        self.assertTrue(TestFlow.Login_out(self,platform='Android',user_id=orig_id,user_pass=orig_pass))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UCC_Testcases)
    unittest.TextTestRunner(verbosity=2).run(suite)
