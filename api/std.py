"""
auto.py - API standart

Author: Levi (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3

Description:
	Basic functions

"""
from os import getcwd as home
from os import getuid as UID
import random
import string

#global config
SB0X_VERSION = "2.0.1rc4"
SB0X_RELEASE_CODE_NAME = "Dex"
SB0X_PLATFROM = "linux"
SB0X_AUTHOR = "Levi (levi0x0)"
SB0X_LICENSE = "GPL 3"
SB0X_CURRENT_MAINTAINER = "Levi (levi0x0)"
SB0X_CORE_VERSION = "0.8"
SB0X_API_VERSION = "0.3"

"""
FIXEME: More nice API (:
KISS - Keep it Simple S**D
"""

def is_root():
    if UID() != 0:
        return False
    elif UID() == 0:
        return True
    else:
        return False


def start(message):
    print "\033[01;32m%s\033[00m" % (message)

def error(message):
		print "\033[01;31m[ERROR] %s\033[00m" % (message)


def warning(message):
		print "\033[01;33m[WARNING] %s\033[00m" % (message)

def notify(message):
		print "\033[01;34m%s\033[00m" % (message)

def debug(message):
		print "[DEBUG] %s" % (message)

def quit(code):
	notify("[*] Bye bye!")
	exit(code)

def check_path(path):
    if not "sb0x" in path:
        error("This is not sb0x-project path.")
        quit(1)
    else:
        pass
LOOP_COUNT = 0

"""
This API function will clear the screen
"""
def cles():
	print("\033[H\033[J")


"""
random_string - the function will create random string
"""
def random_string(length):
   	return ''.join(random.choice(string.lowercase) for i in range(length))

#the current path
home = home()
