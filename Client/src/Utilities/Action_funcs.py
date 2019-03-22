from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import sys
import os
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from Utilities.Actions_android import android_setup
from Utilities.Actions_ios import ios_setup
from Utilities.Actions_web import web_setup
from Utilities_support.log_writer import log_print


class Action_funcs(android_setup, ios_setup, web_setup):

    def __init__(self, VERSION, UDID, PLATFORM):
        self.VERSION = VERSION
        self.UDID = UDID
        self.PLATFORM = PLATFORM
        log_print("info", "initialization done in Action_funcs")


    def LogIn(self, USERNAME, PASSWORD):
        if self.PLATFORM.lower() == "android":
            android_setup._AppLaunch(self, self.VERSION, self.UDID)
            sleep(3)
            user_number = android_setup._login(self,USERNAME,PASSWORD)
            return user_number

        elif self.PLATFORM.lower() == "ios":
            ios_setup._AppLaunch(self, self.VERSION, self.UDID)
            sleep(3)
            user_number = ios_setup._login(self, USERNAME, PASSWORD)
            return user_number

        elif "web" in self.PLATFORM.lower() or "chrome" in self.PLATFORM.lower()\
                or "firefox" in self.PLATFORM.lower() or "explorer" in self.PLATFORM.lower()\
                or "safari" in self.PLATFORM.lower() or "opera" in self.PLATFORM.lower():
            web_setup._AppLaunch(self, self.VERSION, self.UDID, self.PLATFORM)
            sleep(3)
            user_number = web_setup._login(self, USERNAME, PASSWORD)
            return user_number

        else:
            raise Exception("The selected Platform:[{}] not supported".format(self.PLATFORM))

    def Logout(self):
        if self.PLATFORM.lower() == "android":
            try:
                android_setup._logout(self)
            finally:
                android_setup._TearDown(self)

        elif self.PLATFORM.lower() == "ios":
            try:
                ios_setup._logout(self)
            finally:
                ios_setup._TearDown(self)

        else:
            try:
                web_setup._logout(self)
            finally:
                web_setup._TearDown(self)

    def Login_Logout(self,USERNAME,PASSWORD):
        user_number = self.LogIn(USERNAME,PASSWORD)
        sleep(20)
        self.Logout()
        print(user_number)


    def Call(self,term_number):
        if self.PLATFORM.lower() == "android":
            android_setup._call(self,term_number)
        elif self.PLATFORM.lower() == "ios":
            ios_setup._call(self,term_number)
        else:
            web_setup._call(self,term_number)

    def Answer(self):
        if self.PLATFORM.lower() == "android":
            android_setup._answer(self)
        elif self.PLATFORM.lower() == "ios":
            ios_setup._answer(self)
        else:
            web_setup._answer(self)


    def Disconnect(self):
        if self.PLATFORM.lower() == "android":
            android_setup._disconnect(self)
        elif self.PLATFORM.lower() == "ios":
            ios_setup._disconnect(self)
        else:
            web_setup._disconnect(self)

    def Send_Msg(self, term_number):
        if self.PLATFORM.lower() == "android":
            android_setup._msg_send(self, term_number)

        elif self.PLATFORM.lower() == "ios":
            ios_setup._msg_send(self, term_number)

        elif self.PLATFORM.lower() == "web":
            web_setup._msg_send(self, term_number)


