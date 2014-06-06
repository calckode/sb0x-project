"""
main.py - General config

This file is part of sb0x-project

"""

import os 
import glob
import sys
import subprocess
import traceback
from random import choice
from importlib import import_module
from api import auto #import auto-complate api module
from api.std import *#the standart API module

DEBUG = False #devel mode

"""
	The get modules function returns the modules name
	And split .py
	Remove __init__.py from the array
"""

def get_modules():
		try:
			os.chdir("%s/modules" %(home))
			mod_lst = glob.glob("*py")
			os.chdir(home)
			lst = []
			for module in mod_lst:
				if module == "__init__.py":
					pass
				else:
					lst.append(module.replace(".py", ""))
		except Exception as e:
			error(e.message)
			return(1)

		return lst


def modules_counter():
    modules = get_modules()
    modules_counter = 0

    for i in modules:
        modules_counter += 1

    return modules_counter


def select_random_line():
    os.chdir("%s/core/lines/" %(home))

    lines = glob.glob("*li")
    aline = choice(lines)
    line = open(aline, "rt").read()

    return line

def select_random_logo():
    os.chdir("%s/core/logos/" %(home))

    logos = glob.glob("*logo")
    alogo = choice(logos)

    logo = open(alogo, "rt").read()

    return logo

def header():
	print "\033[01;32m"
	print "\t\t+--------------------------------------+"
	print select_random_logo()
	print "\t\t+--------------------------------------+\033[00m\n"

        print "\t\t   .:[\033[01;35mVersion: %s Modules: %d\033[00m]:." %(SB0X_VERSION,modules_counter())
        print "\t\t=[\033[01;34mCode Name: %s | core: %s | api: %s\033[00m]=" %(SB0X_RELEASE_CODE_NAME, 
                SB0X_CORE_VERSION, SB0X_API_VERSION)
        #print "\n\n\033[01;36m - %s\033[00m\n" %(select_random_line())

def usage():
    print "Usage: sb0x.py [OPTIONS]"
    print "\nOptions:"
    print "\t -h, --help - print this screen and exit."
    print "\t -v - print version number and exit."
    print "\t -s [PORT] - run HTTP Server."
    print "\t -n - do not print header at startup."

sb0x_prompt = "\033[01;36msb0x > \033[00m"

def help():
	notify("\thelp, ? - print help.")
	notify("\tload - load modules prompt.")
        notify("\tcupdate - check for updates.")
	notify("\tbanner - print banner.")

def help_load():
	notify("Load Options:")
	notify("\thelp, ? - print help.")
	notify("\tlist - Modules list, to load module type his name in the prompt.")
	notify("\tinfo - print module info author, version etc... Usage: info module_name")
	notify("\tback - back to main.")
"""
The system auto-complate commands array
"""
options_array_system = ["banner", "quit", "clear", "load", "help", "cupdate"]

def dump_module_info(module):
	module = module.replace("info", "").strip()

	module_path = "modules.%s" % (module)
	info = import_module(module_path)
	notify("\t=> Module Name: %s" %(info.MODULE_NAME))
	notify("\t=> Module Author: %s" %(info.MODULE_AUTHOR))
 	notify("\t=> Module Version: %s" %(info.MODULE_VERSION))
	notify("\t=> Module License: %s" %(info.MODULE_LICENSE))
	notify("\t=> Module Description: %s" %(info.MODULE_DESC))

def shell(execs):
	"""The sb0xExec shell"""
	if "cd" in execs:
		try:
			os.chdir(execs.replace("cd", "").strip())
		except Exception as e:
			pass
	else:
		notify("sh: %s" %(execs))
		subprocess.call(execs, shell=True)


options_array_system_load = ['info', 'back', 'exit', 'list', 'load']

def load():
	counter = 0
	while True:
		counter += 1
		options_array = get_modules() + options_array_system_load
		auto.sb0x_complete(options_array)
		prompt = "\033[01;36m[%d] load => \033[00m" % (counter)
		run = raw_input(prompt)
		if not run:
			continue

                elif run == "back" or run == "b":
                    break
		elif run == "list" or run == "ls":
			counter2 = 0
			for module in get_modules():
				counter2 += 1
				notify("\t- %d. %s" %(counter2, module))
			continue
		elif run == "help" or run == "?":
			help_load()
			continue
		elif run == "exit" or run == "q":
			quit(0)
		elif run == "clear":
			cles()
			continue
		elif "info" in run:
			try:
				dump_module_info(run)
                                continue
			except KeyError:
				error(" info: Failed to dump info for: %s" %(run.replace("info", "")))
				continue
			except Exception as e:
                                if DEBUG:
                                    debug("Module info function.")
			        error(e.message)
				continue
		elif run:
			os.chdir("%s" %(home))
			module_path = "modules.%s" % (run)
                        
                        try:
			    init_module = import_module(module_path)
			    """
				Import module -
				The Module Must Contain main() function [REQUIERD]
				See the API tutorial in the Wiki:
				https://github.com/levi0x0/sb0x-project/wiki/API/
			    """
			    init_module.main()
                        except ImportError as e:
                            error(e.message)
                            continue
                        except Exception as e:
                            if DEBUG:
                                error(traceback.format_exc())
                            else:
                                error(e.message)
                            continue
			continue
