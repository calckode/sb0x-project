"""
kali_tools.py - Download git repository from Kali-Linux git

Author: Levi (levi0x0)
Date: 28/05/2014
Version: 0.1
License: GPL 3

Description:
	Kali Linux Tools Downloader from the Offical git repository
"""

import urllib2
import os
from api.std import *
from api import auto

MODULE_NAME = "Kali Tools"
MODULE_AUTHOR = "Levi (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "Kali Linux Tools Downloader from the Offical git repository"


USER_AGENT = "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"

class kali_tools(object):
        """A Simple Module for Downloading kali linux tools"""
        def __init__(self):
            self.text_index = "http://git.kali.org/gitweb/?a=project_index"
            self.kali_git = "git://git.kali.org/"
            self.repo_list = []
            self.repo_counter = 0
            self.git_path = "/usr/bin/git"
            self.prompt =  "\033[01;32m=> \033[00m"
        def get_list(self):
            notify("Please wait...")
            opener = urllib2.build_opener()
            opener.add_headers = [('User-Agent', USER_AGENT)]
            data = opener.open(self.text_index).readlines()

            for repository in data:
                self.repo_counter += 1
                repository = repository.replace("\n", "")
                self.repo_list.append(repository)
                notify("%d. %s" %(self.repo_counter, repository))
            auto.sb0x_complete(self.repo_list)
            print("\nEnter the name of the repository (Example: packages/sqlmap.git)")
            self.toClone = raw_input(self.prompt)
            if not "packages" in self.toClone:
                error("%s - worng repository name" %(self.toClone))
                raise KeyboardInterrupt
                

        """
            XXX: to clone the git repository i can use python-git library 
            but i prefer to use the system git (git clone ...)
        """
        def clone_repo(self):
            if ( os.path.exists(self.git_path)):
                debug("Found git")
            else:
                error("git - not Found in: %s \Please install git\or change to git path" %(self.git_path))
                raise KeyboardInterrupt
            repo_path = "%s/output/%s" %(home, self.toClone)
            repo_to_clone =  "git clone %s%s %s" %(self.kali_git, self.toClone, repo_path)
            if not "sb0x" in home:
                error(" %s - is not sb0x-path" %(home))
                raise KeyboardInterrupt
            os.system(repo_to_clone)

            if ( os.path.exists(repo_path) ):
                notify("Done! Repository saved to: \n%s/output/%s" %(home, self.toClone))

            else:
                pass
def main():
	start = kali_tools()
        start.get_list()
        start.clone_repo()
