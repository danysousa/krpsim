import sys
import os
import time

class Kprocess(object):

	def __init__( self, name, needed, result, delay ):
		self.name = name
		self.needed = needed
		self.result = result
		self.delay = delay

	def launch( self, allStock ):
		for key, value in self.needed.items():
			for stock in allStock:
				if ( key == stock.name ):
					stock.sub( value )
		for key, value in self.result.items():
			for stock in allStock:
				if ( key == stock.name ):
					stock.add( value )
		return ( allStock) 



