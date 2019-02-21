"""
Log_Writer.py
"""
import logging
import os
from os import path
from datetime import datetime

now = datetime.now()
file_dir = "log/"
if not path.isdir(file_dir):
    os.mkdir(file_dir)
LOG_FILENAME = file_dir+"Automation_" + now.strftime("%Y%m%d_%H%M%S") + ".log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logging.info("Automation Framework Logs\n")

def log_print(lv_type="", text=""):
    if lv_type.upper() == "INFO":
        logging.basicConfig(level=logging.INFO)
        logging.info(" "+text)
    elif lv_type.upper() == "DEBUG":
        logging.basicConfig(level=logging.DEBUG)
        logging.debug(" "+text)
    elif lv_type.upper() == "WARNING":
        logging.basicConfig(level=logging.WARNING)
        logging.warning(" "+text)
    elif lv_type.upper() == "ERROR":
        logging.basicConfig(level=logging.ERROR)
        logging.error(" "+text)
    elif lv_type.upper() == "CRITICAL":
        logging.basicConfig(level=logging.CRITICAL)
        logging.critical(" "+text)
    else:
        logging.debug(" ** Final result of this suit **\n"+text)
