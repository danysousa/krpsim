import sys
import os

class Stock(object):

	def __init__( self, name, qty ):
		self.name = name
		self.qty = qty
		self.linkNeeded = []

	# add stock
	def add( self, number ):
		self.qty = self.qty + number

	# sub stock
	def sub( self, number ):
		self.qty = self.qty - number

	def addLink( self, stock ):
		i = 0
		while i < len(self.linkNeeded) :
			if ( self.linkNeeded[i].name == stock.name ):
				return 0
			i += 1
		self.linkNeeded.append(stock)
