import unittest
import subprocess
import random


class BaseSetup(unittest.TestCase):
    appiumPORT = ['4723', '4724', '4725', '4726']
    """Basis for all tests."""

    def setUp(self):
        self.Android_devices_dict = {}
        self.Android_devices_list = []
        self.Android_devices_used = []
        result_out = subprocess.check_output('adb devices').decode().split('\n')
        for s in result_out:
            s = s.rstrip()
            if s != "List of devices attached" and s != "":
                # script to get android or ios version of each device
                self.Android_devices_dict[s.split('\t')[0]] = subprocess.check_output(
                    'adb -s ' + s.split('\t')[0] + ' shell getprop ro.build.version.release').decode().rstrip()
                # below command to Avoid below error
                # Error: An unknown server-side error occurred while processing the command.
                # Original error: Could not proxy command to remote server. Original error: Error: read ECONNRESET
                try:
                    print(subprocess.check_output('adb -s ' + s.split('\t')[0] + ' uninstall io.appium.uiautomator2.server').decode().rstrip())
                    print(subprocess.check_output('adb -s ' + s.split('\t')[0] +' uninstall io.appium.uiautomator2.server.test').decode().rstrip())
                except:
                    print("Already Uninstalled")

        self.Android_devices_list = self.Android_devices_list + list(self.Android_devices_dict.keys())

        ####
        self.ios_devices_dict = {}
        self.ios_devices_list = []
        self.ios_devices_used = []
        # Add code here for IOS devices
        ####

    def getDevice(self, platformName):
        if platformName.lower() == "android":
            device = random.choice(self.Android_devices_list)
            self.Android_devices_list.remove(device)
            self.Android_devices_used.append(device)
            return self.Android_devices_dict[device], device
        elif platformName.lower() == "ios":
            device = random.choice(self.ios_devices_list)
            self.ios_devices_list.remove(device)
            self.ios_devices_used.append(device)
            return self.ios_devices_dict[device], device
        else:
            return None, None

    def addDevice(self, platformName):
        if platformName.lower() == "android":
            self.Android_devices_list.extend(self.Android_devices_used)
            self.Android_devices_used = []
        elif platformName.lower() == "ios":
            self.ios_devices_list.extend(self.ios_devices_used)
            self.ios_devices_used = []

    def tearDown(self):
        pass

    def get_name(self):
        raise NotImplementedError

    def navigate_to_page(self):
        """Navigates to desired page."""
        self.navigation_page.go_to_category(self.get_name())

