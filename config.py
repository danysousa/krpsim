import sys
import re

class Config(object):

	def __init__(self, filename):
		self.filename = filename
		self.stock = []

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
		ptr = [self.addStock, self.addProcess, self.setOptimize]

		for i in xrange(0, len(patterns)):
			if (re.match(patterns[i], line)):
				ptr[i](line)


	def addStock(self, line):
		print ("[Stock] " + line)
		m = re.match("([a-zA-Z\-_0-9]{1,}):([0-9]{1,})", line)
		print("on ajoute " + m.group(2) + " a la pile " + m.group(1))


	def addProcess(self, line):
		array = {}
		m = re.search("\(([a-z\-_A-Z0-9\:\;]*)\):\(([a-z\-_A-Z0-9\:\;]*)\)", line[line.find(":"):line.rfind(":")])
		lNeed = m.group(1)
		lResult = m.group(2)
		name = line[:line.find(":")]
		time = line[line.rfind(":") + 1:len(line) - 1]

		lNeed = lNeed.split(";")
		array["cost"] = {}
		for elem in lNeed:
			tmp = elem.split(":")
			array["cost"][tmp[0]] = tmp[1]

		lResult = lResult.split(";")
		array["result"] = {}
		for elem in lResult:
			tmp = elem.split(":")
			array["result"][tmp[0]] = tmp[1]

		array["delay"] = time
		print (name);
		print (array);

	def setOptimize(self, line):
		tmp = line[10:len(line) - 2]
		print(tmp.split(";"))
