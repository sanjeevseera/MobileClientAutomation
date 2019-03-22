import sys
import os
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from Utilities.Action_funcs import Action_funcs
from Utilities.base_setup import BaseSetup
from Utilities_support.log_writer import log_print
from time import sleep
import inspect

class TestFlow(Action_funcs):

    def Login_out(self, platform, user_id, user_pass):
        func = inspect.stack()[1].function
        try:
            log_print("info", "TestCase::[{0}] - ".format(func) + "Starting test case Basic_Messaging")
            VERSION, UDID = BaseSetup.getDevice(self, platform)
            log_print("info", "{0} Mobile picked[UDID: {1}, VERSION: {2}]".format(platform.capitalize(), UDID, VERSION))
            user = Action_funcs(VERSION, UDID, platform)
            #user.Login_Logout(user_id, user_pass)
            user_number = user.LogIn(user_id, user_pass)
            log_print("info", "Login is successful and Active number for the user:[{0}] is [{1}]".format(user_id, user_number))
            sleep(30)
            user.Logout()
            log_print("info", "Login and Logout test is successful for user:[{}]".format(user_id))
            return True
        except IndexError as e:
            log_print("error", "IndexError: "+str(e))
            log_print("error", "Login and Logout test is failed for user:[{}]".format(user_id))
            return False
        except Exception as e:
            log_print("error", str(e))
            log_print("error", "Login and Logout test is failed for user:[{}]".format(user_id))
            return False
        finally:
            BaseSetup.addDevice(self, platform)

    def Basic_Call(self, platform, orig_id, orig_pass, term_id, term_pass):
        func = inspect.stack()[1].function
        log_print("info", "TestCase::[{0}] - ".format(func) + "Starting test case Basic_Call")
        Platform = platform.split("-")
        VERSION_1, UDID_1 = BaseSetup.getDevice(self, Platform[0])
        log_print("info", "{0} Mobile picked[UDID: {1}, VERSION: {2}]".format(Platform[0].capitalize(), UDID_1, VERSION_1))
        user1 = Action_funcs(VERSION_1, UDID_1, Platform[0])
        VERSION_2, UDID_2 = BaseSetup.getDevice(self, Platform[1])
        log_print("info", "{0} Mobile picked[UDID: {1}, VERSION: {2}]".format(Platform[1].capitalize(), UDID_2, VERSION_2))
        user2 = Action_funcs(VERSION_2, UDID_2, Platform[1])
        orig_number = user1.LogIn(orig_id, orig_pass)
        log_print("info", "Active number for the Orig user:[{0}] is [{1}]".format(orig_id, orig_number))
        sleep(2)
        term_number = user2.LogIn(term_id, term_pass)
        log_print("info", "Active number for the Term user:[{0}] is [{1}]".format(term_id, term_number))
        sleep(5)
        user1.Call(str(term_number))
        sleep(5)
        user2.Answer()
        sleep(20)
        user1.Disconnect()
        sleep(5)
        user1.Logout()
        sleep(4)
        user2.Logout()

        if Platform[0] == Platform[1]:
            BaseSetup.addDevice(self,Platform[0])
        else:
            BaseSetup.addDevice(self,Platform[0])
            BaseSetup.addDevice(self,Platform[1])
        return True

    def Basic_Messaging(self, platform, orig_id, orig_pass, term_id, term_pass):
        func = inspect.stack()[1].function
        try:
            log_print("info", "TestCase::[{0}] - ".format(func) + "Starting test case Basic_Messaging")
            Platform = platform.split("-")
            VERSION_1, UDID_1 = BaseSetup.getDevice(self, Platform[0])
            user1 = Action_funcs(VERSION_1, UDID_1, Platform[0])
            log_print("info", "{0} Mobile picked[UDID: {1}, VERSION: {2}]".format(Platform[0].capitalize(), UDID_1, VERSION_1))
            # VERSION_2, UDID_2 = BaseSetup.getDevice(self, Platform[1])
            # user2 = Action_funcs(VERSION_2, UDID_2, Platform[1])
            #log_print("info", "{0} Mobile picked[UDID: {1}, VERSION: {2}]".format(Platform[1].capitalize(), UDID_2, VERSION_2))
            orig_number = user1.LogIn(orig_id, orig_pass)
            log_print("info", "Active number for the Orig user:[{0}] is [{1}]".format(orig_id, orig_number))
            # sleep(2)
            # term_number = user2.LogIn(term_id, term_pass)
            # print(term_number)
            sleep(10)
            user1.Send_Msg("+917022943949")
            sleep(5)
            return True

        except Exception as e:
            log_print("error", "Exception: {}".format(e))
            return False

        finally:
            user1.Logout()
            sleep(5)
            # user2.Logout()

            if Platform[0] == Platform[1]:
                BaseSetup.addDevice(self, Platform[0])
            else:
                BaseSetup.addDevice(self, Platform[0])
                BaseSetup.addDevice(self, Platform[1])
            return True
