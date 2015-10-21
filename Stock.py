import sys
import os

class Stock(object):

	def __init__( self, name, qty ):
		self.name = name
		self.qty = qty

	# add stock
	def add( self, number ):
		self.qty = self.qty + number

	# sub stock
	def sub( self, number ):
		self.qty = self.qty - number
