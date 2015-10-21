#!/usr/bin/python

import sys
import os

from Stock import Stock
from Manager import Manager
from Kprocess import Kprocess

def main( ):
	s1 = Stock( 'euro', 8 )
	s2 = Stock( 'materiel', 0 )
	s3 = Stock( 'produit', 0 )
	s4 = Stock( 'client_content', 0 )
	stocks =  [s1, s2, s3, s4]
	p1 = Kprocess( 'achat_materiel', {'euro': 8}, {'materiel': 1}, 10 )
	p2 = Kprocess( 'realisation_produit', {'materiel': 1}, {'produit': 1}, 30 )
	p3 = Kprocess( 'produit', {'produit': 1}, {'client_content': 1}, 20 )
	m = Manager( stocks )
	m.addProcess( p1 )
	m.addProcess( p2 )
	m.addProcess( p3 )

	m.callProcess( p1 )
	m.displayStock( )
	print("\n")
	m.callProcess( p2 )
	m.displayStock( )
	print("\n")
	m.callProcess( p3 )
	m.displayStock( )
	print("\n")

main( )