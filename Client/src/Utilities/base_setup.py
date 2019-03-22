import unittest
import subprocess
import random
import platform
import os, sys
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from Utilities_support.Client import remote_command
from Appium_configs.config_general import *
from Utilities_support.log_writer import log_print

class BaseSetup(unittest.TestCase):
    """Basis for all tests."""

    def setUp(self):
        self.Android_devices_dict = {}
        self.Android_devices_list = []
        self.Android_devices_used = []
        if platform.system().lower() == "windows":
            adb_path = ""
        else:
            adb_path = "~/Library/Android/sdk/platform-tools/"
        #result_out = subprocess.check_output(adb_path+'adb devices', shell=True, stderr=subprocess.STDOUT).decode().split('\n')
        result_out = remote_command(adb_path+'adb devices', Appium_IP).split('\n')
        print(result_out)
        for s in result_out:
            s = s.rstrip()
            if s != "List of devices attached" and s != "":
                # script to get android or ios version of each device
                log_print("INFO", str(s.split('\t')[0]))
                #self.Android_devices_dict[s.split('\t')[0]] = subprocess.check_output(adb_path+'adb -s ' + s.split('\t')[0] + ' shell getprop ro.build.version.release', shell=True, stderr=subprocess.STDOUT).decode().rstrip()
                self.Android_devices_dict[s.split('\t')[0]] = remote_command(adb_path+'adb -s ' + s.split('\t')[0] + ' shell getprop ro.build.version.release', Appium_IP).rstrip()
                # below command to Avoid below error
                # Error: An unknown server-side error occurred while processing the command.
                # Original error: Could not proxy command to remote server. Original error: Error: read ECONNRESET
                try:
                    #print(subprocess.check_output(adb_path+'adb -s ' + s.split('\t')[0] + ' uninstall io.appium.uiautomator2.server', shell=True, stderr=subprocess.STDOUT).decode().rstrip())
                    #print(subprocess.check_output(adb_path+'adb -s ' + s.split('\t')[0] +' uninstall io.appium.uiautomator2.server.test', shell=True, stderr=subprocess.STDOUT).decode().rstrip())
                    log_print("INFO", remote_command(adb_path+'adb -s ' + s.split('\t')[0] + ' uninstall io.appium.uiautomator2.server').rstrip())
                    log_print("INFO", remote_command(adb_path+'adb -s ' + s.split('\t')[0] +' uninstall io.appium.uiautomator2.server.test').rstrip())
                except:
                    log_print("INFO", "Already Uninstalled")

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

