"""
update.py - check if new version is available

"""

import urllib2
from api.std import *
from main import modules_counter


def generate_update():
    check_path(home)
    sb0x_file = open("%s/core/version" %(home), "wt")
    sb0x_file.write("#This file is auto-generated by sb0x DO NOT EDIT\n")
    sb0x_file.write("%s\n" %(SB0X_VERSION))
    sb0x_file.write("%s\n" %(SB0X_CORE_VERSION))
    sb0x_file.write("%d" %(modules_counter()))
    sb0x_file.close()

def parse_remote():

    try:
         remote = urllib2.urlopen("https://raw.githubusercontent.com/levi0x0/sb0x-project/master/core/version").readlines()

    except Exception as e:
        error("Connection Failed!")
        raise KeyboardInterrupt
    counter = 0
    for i in remote:
        i = i.replace("\n", "")
        counter +=1
        if i.startswith("#"):
            pass
        else:
            if counter == 2:
                if i == SB0X_VERSION:
                    print "\033[01;32m[OK] sb0x-project is up-to-date.\033[00m"
                else:
                    warning("sb0x-project is out-of-date.")
                    print "- New sb0x-version available, Version: %s" %(i)
            elif counter == 3:
                if i == SB0X_CORE_VERSION:
                    print "\033[01;32m[OK] sb0x-core is up-to-date.\033[00m"
                else:
                    warning("sb0x-core is out-of-date.")
                    print "- New sb0x-core available, Core: %s" %(i)
            elif counter == 4:
                if int(i) == int(modules_counter()):
                    pass
                else:
                    summ = int(i) - int(modules_counter())
                    if summ == -1:
                        pass
                    else:
                        print "\033[01;32m[NEW] There is %d New sb0x modules " %(summ)
