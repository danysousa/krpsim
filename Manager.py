import sys
import os

class Manager(object):

	def __init__( self, stocks ):
		self.allStock = stocks
		self.allProcess = {}

	# add process
	def addProcess( self, process ):
		self.allProcess[process.name] = process

	# call process
	def callProcess( self, process ):
		print( process.name + " is launched !" )
		self.allStock = process.launch( self.allStock )

	def displayStock( self ):
		for value in self.allStock :
			print( value.name + " " + str(value.qty) )
