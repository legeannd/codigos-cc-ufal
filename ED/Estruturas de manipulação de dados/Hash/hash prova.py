class Table:
	def __init__(self, m):
		self.m = m
		self.table = [None]*m

	def hash(self, x):
		return x % self.m

	def insert(self, x):
		h = self.hash(x)
		if self.table[h] == None:
			self.table[h] = []
		self.table[h].append(x)

	def delHash(self, x):
		h = self.hash(x)
		flag = False
		for i in range(self.m):
			if self.table[h] != None:
				for i in self.table[h]:
					if i == x:
						flag = True
		self.table[h].remove(x) if flag else print("Elemento", x," não encontrado")

	def hashPrint(self):
		for i in range(self.m):
			print(i, self.table[i])
