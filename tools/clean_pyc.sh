#!/usr/bin/env bash
#
#
# This script will clean all the *.pyc compiled files
# Written by: Levi (levi0x0)
# Date: 21-05-2014

cd ../

rm api/*pyc
rm api/lib/*pyc
rm modules/*pyc
rm -r api/__pycache__
rm -r core/__pycache__
rm -r modules/__pycache__

echo "Cleanup..."
