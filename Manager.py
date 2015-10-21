import sys
import os

class Manager(object):

	def __init__( self, stocks, process ):
		self.allStock = stocks
		self.allProcess = process

	# add process
	def addProcess( self, process ):
		self.allProcess[process.name] = process

	# call process
	def callProcess( self, name ):
		print (name + " called")
		self.allStock = self.allProcess[name].launch( self.allStock )

	def displayStock( self ):
		for value in self.allStock :
			print( value.name + " " + str(value.qty) )
