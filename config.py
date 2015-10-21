import sys
import re

class Config(object):

	def __init__(self, filename):
		self.filename = filename
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
			"^([a-zA-Z0-9_]{1,}):([0-9]{1,})$",
			"^([a-zA-Z0-9_]{1,}):((\([a-zA-Z0-9_]{1,}:[0-9]\));?){1,}:((\([a-zA-Z0-9_]{1,}:[0-9]\));?){1,}:([a-zA-Z0-9_]{1,})$",
			"optimize:\(((time|[a-zA-Z0-9_]{1,});?){1,}\)"
			]
		name = ["stock", "process", "optimize"]

		for i in xrange(0, len(patterns)):
			m = re.match(patterns[i], line)
			if (m):
				print("[" + name[i] + "]: " + line)
				print(m.groups())



