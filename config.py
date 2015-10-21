import sys
import re
from Stock import Stock
from Kprocess import Kprocess

class Config(object):

	def __init__(self, filename):
		self.filename = filename
		self.stock = []
		self.process = {}

		try:
			fd = open(filename, 'r')
		except IOError:
			print("Can't open " + filename)
			sys.exit(0)
		self.parse(fd)

	def parse(self, fd):
		for line in fd :
			if (line[0] == '#'):
				continue
			self.findAction(line)

	def findAction(self, line):
		patterns = [
			"^([a-zA-Z0-9_\-]{1,}):([0-9]{1,})$",
			"^([a-zA-Z_0-9\-]{1,}):\((([a-zA-Z_\-0-9]{1,}):([0-9]);?){1,}\):\((([a-zA-Z_\-0-9]{1,}):([0-9]);?){1,}\):([0-9]{1,})$",
			"optimize:\((((time)|([a-zA-Z0-9_\-]{1,}));?){1,}\)"
			]
		name = ["stock", "process", "optimize"]
		ptr = [self.setStock, self.setProcess, self.setOptimize]

		for i in xrange(0, len(patterns)):
			if (re.match(patterns[i], line)):
				ptr[i](line)

	def setStock(self, line):
		m = re.match("([a-zA-Z\-_0-9]{1,}):([0-9]{1,})", line)
		self.addStock(m.group(1), m.group(2))

	def setProcess(self, line):
		array = {}
		m = re.search("\(([a-z\-_A-Z0-9\:\;]*)\):\(([a-z\-_A-Z0-9\:\;]*)\)", line[line.find(":"):line.rfind(":")])
		lNeed = m.group(1)
		lResult = m.group(2)
		name = line[:line.find(":")]
		time = line[line.rfind(":") + 1:len(line) - 1]

		lNeed = lNeed.split(";")
		array["needed"] = {}
		for elem in lNeed:
			tmp = elem.split(":")
			self.addStock(tmp[0], 0)
			array["needed"][tmp[0]] = int(tmp[1])

		lResult = lResult.split(";")
		array["result"] = {}
		for elem in lResult:
			tmp = elem.split(":")
			self.addStock(tmp[0], 0)
			array["result"][tmp[0]] = int(tmp[1])

		array["delay"] = time
		self.addProcess(name, array["needed"], array["result"], int(time))

	def setOptimize(self, line):
		tmp = line[10:len(line) - 2]
		print ("[A FAIRE] OPTIMISATION ")
		print(tmp.split(";"))

	def addStock(self, name, qty):
		for x in xrange(0,len(self.stock)):
			if ( self.stock[x].name == name ):
				return
		self.stock.append(Stock(name, int(qty)))

	def addProcess(self, name, needed, result, delay):
		if name in self.process :
			print ("ERROR with config file")
			sys.exit(0)
		self.process[name] = Kprocess(name, needed, result, int(delay))

