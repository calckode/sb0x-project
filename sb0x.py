#!/usr/bin/env python2.7
"""
sb0x.py - Main shell

This file is part of the sb0x-project (C) 2013 -2014

"""

import sys
import getopt #C Style (:
import os
try:
    from core.tests import tests, init
    tests = tests()
    tests.test_python_version()
    init()
    tests.test_for_output()
except Exception as e:
    print("\033[01;31m[ERROR] %s\033[00m" %(e) )
    sys.exit(1)

from core.main import *
from core.update import generate_update, parse_remote
import api.auto
from api.std import *

class sb0x_shell(object):
		"""sb0x shell"""
		def __init__(self, runc):
			self.runc = runc

		def run(self):
                    for command in options_array_system_load:
                        if command == "load" or command == "exit":
                            pass
                        elif command == self.runc:
                            warning("You are in Main shell, to run %s type load." %(self.runc))
                            break
		    if self.runc == "load":
		    	load()
                    elif self.runc == "cupdate":
                        parse_remote()
		    elif self.runc == "banner":
			header()
		    elif self.runc == "exit" or self.runc == "q":
			api.std.quit(0)
		    elif self.runc == "help" or self.runc == "?":
			help()
		    else:
                        shell(self.runc)


"""
The Main Fucntion Init the Code
"""

def main():
                auto.sb0x_complete(options_array_system)
                runc = raw_input(sb0x_prompt)
	        start = sb0x_shell(runc)
	        start.run()

if __name__ == '__main__':
        headerf = True
        try:
            opts, args = getopt.getopt(sys.argv[1:], "vhns:")
        except getopt.GetoptError as err:
            error(str(err))
            usage()
            sys.exit(1)

        try:
            for o, a in opts:
                if o == "-v":
                    print "%s" % (SB0X_VERSION)
                    sys.exit(0)
                elif o == "-h":
                    usage()
                    sys.exit(0)
                elif o == "-n":
                    headerf = False
                    break
                elif o == "-s":
                    port = int(a)
                    from core.http_server import httpd
                    httpd(port)
                    break
                else:
                    break
        except Exception as e:
            error(e.message)
            sys.exit(1)

        #===================#
        # show header or not#
        #===================#
        if headerf:
            cles()
            header()
        else:
            pass
        generate_update()
        while True:
            try:
                main()
            except KeyboardInterrupt:
                notify("\n Press 'q' to quit")
                continue
            except Exception as e:
                if DEBUG:
                    print traceback.format_exc()
                    continue
                else:
                    error(e.message)
                    continue

