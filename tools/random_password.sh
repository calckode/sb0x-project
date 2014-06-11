#!/usr/bin/bash 
#
# A simple random password genartor using the /dev/random Device
# Written by levi0x0


if [ -z $1 ];then
	echo -e "\nUsage: $0 [PASSWORD LENGTH]"
	echo -e "\n\tExample:"
	echo -e "\t\t$0 9\n"

else
	password=`cat /dev/urandom | tr -dc A-Za-z0-9 | head -c$1`
	echo -e "\e[01;32m$password\033[00m"

fi

