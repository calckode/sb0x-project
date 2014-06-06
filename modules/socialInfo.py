"""
social_info.py - get user information from social networks

Author: Levi (levi0x0)
Date: 01/06/2014
Version: 0.1
License: GPL 3

Description:
	get user information from social networks
"""

MODULE_NAME = "Social info"
MODULE_AUTHOR = "Levi(levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1-test"
MODULE_DESC = "get user information from social networks, Works only with facebook for now.."


import json
import urllib2
from api.std import *

USER_AGENT = "Mozilla/5.0 (Unknown; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) PingdomTMS/0.8.5 Safari/534.34"

def get_facebook(user):
    start("Fetching information from facebook.com...")

    index = "https://graph.facebook.com/%s" %(user)

    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', USER_AGENT)]

    try:
        remote = opener.open(index)

    except Exception as e:
        if e.code == 404:
            error("User Name: %s Not Found" %(user))
            raise Exception
            
        else:
            pass

    local = json.load(remote)
    notify("\t=> User: %s" % (local["username"]))
    notify("\t=> ID: %s" %(local["id"]))
    notify("\t=> First name: %s" %(local["first_name"]))
    notify("\t=> Last name: %s" %(local["last_name"]))
    notify("\t=> Locale: %s" %(local["locale"]))
    notify("\t=> Gender: %s" %(local["gender"]))

    remote = opener.open("http://graph.facebook.com/%s/picture?&height=200&type=normal&width=200" %(local["id"])).geturl()

    notify("\t=> Profile Picture: %s" %(remote))

def main():
    user = raw_input("User Name: (Example: LOL_USER): ")

    try:
        get_facebook(user)

    except Exception as e:
        error(e.message)
    notify("Done.")

# vim set tabstop=8
