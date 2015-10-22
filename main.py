#!/usr/bin/python2.7
import sys
import os

from Stock import Stock
from Manager import Manager
from Kprocess import Kprocess
from config import Config

def main( ):
	if ( len(sys.argv) == 2 ):
		c = Config(sys.argv[1])
	else:
		print("Usage : ./main.py [config_file]")

	m = Manager( c.stock, c.process )

	m.linkStock( )

	print("")
	m.displayStock()
#	m.callProcess("cuisson_1")
#	m.callProcess("cuisson_2")
#	m.callProcess("cuisson_3")

main( )
