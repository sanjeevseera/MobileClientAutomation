"""
ios strategy vaiables for
Accessibility ID, Class name, ID, Name, XPath, Image
"""
import sys
import os
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from Appium_configs.config_general import *
PORT = Appium_Port
IP = Appium_IP
url = "http://"+IP+":"+str(PORT)+"/wd/hub"