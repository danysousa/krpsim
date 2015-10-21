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

	m.callProcess("achat_materiel")
	m.callProcess("realisation_produit")
	m.callProcess("livraison")

main( )
