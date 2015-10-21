#!/usr/bin/python2.7

from config import Config
import sys

if ( len(sys.argv) == 2 ):
	c = Config(sys.argv[1])
else:
	print("Usage : ./main.py [config_file]")
