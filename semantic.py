txt = ""
count = 0
def add_count():
	global count
	count += 1
	return "%s" % count
class Node:
	def __init__(self, name):
		self.name = name
		
class Program(Node):
	def __init__(self, name, *args):
		Node.__init__(self, name)
		self.sons = []
		for x in args:
			self.sons.append(x)

	def print(self, identation):
		for x in self.sons:
			x.print("\t" + identation)
		print(identation + "Node: " + self.name)

	def translate(self):
		global txt
		number = add_count()
		txt += number + "[label = " + self.name + "]\n\t"
		for x in self.sons:
			son = x.translate()
			txt += number + "->" + son + "\n\t"
		return "digraph G {\n\t" + txt + "}"

class Terminal(Node):
	def __init__(self, name):
		Node.__init__(self, name)

	def print(self, identation):
		print(identation + "Node: " + self.name)

	def translate(self):
		global txt
		number = add_count()
		if self.name == "Squals" or self.name == "Non_equal" or self.name == "Less" or self.name == "Less equal" or self.name == "Greater" or self.name == "Greater equal" or self.name == "String":
			txt += number + "[label = \"" + str(self.name) + "\"]\n\t"
		else:
			txt += number + "[label = " + str(self.name) + "]\n\t"
		return number

class NonTerminal(Node):
	def __init__(self, name, *args):
		Node.__init__(self, name)
		self.sons = []
		for x in args:
			self.sons.append(x)

	def print(self, identation):
		for x in self.sons:
			if type(x) == type(tuple()):
				x[0].print("\t" + identation)
			else:
				x.print("\t" + identation)
		print(identation + "Node: " + self.name)
		
	def translate(self):
		global txt
		number = add_count()
		txt += number + "[label = " + self.name + "]\n\t"
		for x in self.sons:
			if type(x) == type(tuple()):
				son = x[0].translate()
			else:
				son = x.translate()
			txt += number + "->" + son + "\n\t"
		return number

class Null(Node):
	def __init__(self):
		self.type = "void"

	def print(self, identation):
		print(identation + "Null")

	def translate(self):
		global txt
		number = add_count()
		txt += number + "[label = " + "Null" + "]\n\t"
		return number