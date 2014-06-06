"""
ip_Generator.py - A simple IP Addresses generator

Author: Levi (levi0x0)
Date: 28/05/2014
Version: 0.1
License: GPL 3

Description:
	A Simple IP Addresses generator
"""
from random import randrange
from api.std import *

MODULE_NAME = "IP Generator"
MODULE_AUTHOR = "Levi (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "A Simple IPv4 Addresses generator"


def generate_ips(ips, save):
    do_not_use = [10,127,254,255,1,2,169,172,192]
    i = 0

    log_path = "%s/output/%s.ips" %(home, random_string(4))

    if save:
        log = open(log_path, "wt")
    while i < int(ips):
        step = randrange(1, 256)
        i+=1
        while step in do_not_use:
            step = randrange(1, 256)
        ip = ".".join([str(step), str(randrange(1, 256)),
            str(randrange(1,256)), str(randrange(1,256))])
        if save:
            log.write(ip)
            log.write('\n')
        notify(ip)
    if save:
        print("\nIP List Saved to: %s" %(log_path)) 


def main():
    ips = int(raw_input("Number of IP'S to generate (Example: 200):"))
    save = raw_input("Want to save the IP's in a file? (y/N):")
    if save == "y" or save == "yes":
        save = True
    else:
        save = False
    generate_ips(ips, save)
