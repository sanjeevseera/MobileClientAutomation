from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from time import sleep
import sys
import os
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from Appium_configs.config_android import *


class android_setup():

    def _AppLaunch(self, VERSION, UDID):
        """Sets up desired capabilities and the Appium driver."""
        desired_caps = {}
        """
        The following desired capabilities must be set when running locally.
        Make sure they are NOT set when uploading to Device Farm.

        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '3300f4b7d5f56461'
        """
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Device'
        desired_caps['platformVersion'] = VERSION
        desired_caps['fullReset'] = 'false'
        desired_caps['noReset'] = 'true'
        desired_caps['newCommandTimeout'] = '3600'
        desired_caps['udid'] = UDID
        desired_caps["appPackage"] = "com.mavenir.gmid"
        desired_caps["appActivity"] = "com.mavenir.ucc.tab.TabActivity"
        desired_caps["automationName"] = "UiAutomator2"
        self.driver = webdriver.Remote(url, desired_caps)
        #self.navigation_page = NavigationPage(self.driver)
        #self.driver.launch_app()


    def _TearDown(self):
        self.driver.quit()

    def _login(self,USERNAME,PASSWORD):
        # Long press on button
        alert_ele = self.driver.find_elements_by_class_name(android['TextView'])
        for ele in alert_ele:
            if ele.text == "UIAutomator has stopped":
                self.driver.find_element_by_id(android['alertTitle']).click()
                self.driver.find_element_by_id(android['aerr_close']).click()
                break

        sleep(3)
        el1 = self.driver.find_element_by_id(UCC_id_login['dev_settings_fragment'])
        actions = TouchAction(self.driver)
        actions.long_press(el1)
        actions.perform()
        sleep(2)
        #self.driver.find_element_by_xpath(UCC_xpath['Lab_Setting']).click()
        #self.driver.find_element_by_xpath(UCC_xpath['Lab_Name']).click()
        elements = self.driver.find_elements_by_class_name(android['TextView'])
        for el in elements:
            if el.text == "Lab Settings":
                el.click()
                break
        elements = self.driver.find_elements_by_class_name(android['TextView'])
        for el in elements:
            if el.text == "Bangalore lab":
                el.click()
                break
        sleep(5)
        self.driver.find_element_by_id(UCC_id_login['input_login']).click()
        sleep(2)
        self.driver.find_element_by_id(UCC_id_login['input_login']).clear()
        self.driver.find_element_by_id(UCC_id_login['input_login']).send_keys(USERNAME)
        sleep(2)
        self.driver.find_element_by_id(UCC_id_login['input_password']).click()
        self.driver.find_element_by_id(UCC_id_login['input_password']).clear()
        self.driver.find_element_by_id(UCC_id_login['input_password']).send_keys(PASSWORD)
        sleep(2)
        self.driver.find_element_by_id(UCC_id_login['btn_login']).click()
        sleep(5)
        # Code for Allow permissions
        ale = self.driver.find_elements_by_class_name(android['Button'])
        for element in ale:
            if element.text == "ALLOW":
                element.click()
                element.click()
                element.click()
                element.click()
                element.click()
                #self.driver.find_element_by_xpath(UCC_xpath['ALLOW']).click()
                #self.driver.find_element_by_xpath(UCC_xpath['ALLOW']).click()
                #self.driver.find_element_by_xpath(UCC_xpath['ALLOW']).click()
                #self.driver.find_element_by_xpath(UCC_xpath['ALLOW']).click()
                break
        sleep(10)
        self.driver.find_element_by_id(UCC_id_login['parent_layout']).click()
        user_line = self.driver.find_element_by_id(UCC_id_login['line_name_view']).text
        user_number = self.driver.find_element_by_id(UCC_id_login['line_number_view']).text
        print(user_line, user_number)
        self.driver.find_element_by_id(UCC_id_login['navigate_button']).click()
        sleep(10)
        # self.driver.find_element_by_id("android:id/button2").click()
        eleButton = self.driver.find_elements_by_class_name(android['Button'])
        for eleB in eleButton:
            if eleB.text == "IGNORE":
                eleB.click()
                break
        return user_number

    def _logout(self):
        self.driver.find_element_by_id(UCC_id_login['user_status']).click()
        """
        elements = self.driver.find_elements_by_class_name("android.support.v7.widget.LinearLayoutCompat")
        elements[-1].click()
        """
        elements = self.driver.find_element_by_class_name(android['CheckedTextView'])
        for ele in elements:
            if ele.text == "Sign out":
                ele.click()

    def _call(self, term_number):
        sleep(5)
        self.driver.find_element_by_id(UCC_id_call['btn_calls']).click()
        self.driver.find_element_by_id(UCC_id_call['lines_spinner']).click()
        elements = self.driver.find_elements_by_class_name(android['ViewGroup'])
        elements[1].click()
        self.driver.find_element_by_id(UCC_id_call['btn_dialer']).click()
        sleep(2)
        self.driver.find_element_by_id(UCC_id_call['input']).send_keys(term_number)
        sleep(2)
        self.driver.find_element_by_id(UCC_id_call['btn_call']).click()
        sleep(2)

    def _answer(self):
        sleep(10)
        self.driver.find_element_by_id(UCC_id_call['swipe_up']).click()
        self.driver.swipe(553, 1668, 712, 1034, 1634)

    def _disconnect(self):
        self.driver.find_element_by_id(UCC_id_call['btn_decline_call']).click()

    def _msg_send(self, term_number):
        self.driver.find_element_by_id(UCC_id_msg['btn_chats']).click()
        self.driver.find_element_by_id(UCC_id_msg['btn_add_chat']).click()
        sleep(5)
        # alert popup
        element = self.driver.find_elements_by_class_name(android['Button'])
        for ele in element:
            if ele.text == "ALLOW":
                ele.click()
                break

        self.driver.find_element_by_id(UCC_id_msg['message_input']).click()
        self.driver.find_element_by_id(UCC_id_msg['message_input']).clear()
        self.driver.find_element_by_id(UCC_id_msg['message_input']).send_keys(term_number)
        sleep(5)
        self.driver.keyevent(84)
        #self.driver.press_keycode(84)
        #self.driver.press_keycode(84)
        self.driver.find_element_by_id("android.view.inputmethod.EditorInfo").send_keys("IME_ACTION_DONE")

        sleep(60)
        #self.driver.find_element_by_id(UCC_id_msg['message_input']).click()
        #self.driver.find_element_by_id(UCC_id_msg['message_input']).send_keys("testmsg1")






