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

	def	linkStock( self ):
		allStockResult = self.allStock
		allStockNeeded = self.allStock
		for keyProcess, process in self.allProcess.items():
			for keyResult, result in process.result.items():
				for stockResult in allStockResult :
					if ( keyResult == stockResult.name ):
						print(stockResult.name)
						for keyNeeded, needed in process.needed.items():
							for stockNeeded in allStockNeeded :
								if ( keyNeeded == stockNeeded.name ):
									print( "   " + stockNeeded.name )
									stockResult.addLink( stockNeeded )
					

	def displayStock( self ):
		for value in self.allStock :
			print( value.name + " " + str(value.qty) )
			print("Link : ")
			for x in xrange(0,len(value.linkNeeded)):
				print( "   " + value.linkNeeded[x].name )


