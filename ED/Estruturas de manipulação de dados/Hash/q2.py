class Table:
	def __init__(self, m):
		self.m = m
		self.table = [None]*m

	def hash(self, x):
		cod = 0
		x = x.lower()
		for i in str(x):
			cod += ord(i)
		return cod % self.m

	def insert(self, x):
		h = self.hash(x)
		if self.table[h] == None:
			self.table[h] = []
		self.table[h].append(x)

	def hashPrint(self):
		for i in range(self.m):
			print(i, self.table[i])
		print('---')

	def isAuthorized(self, x):
		h = self.hash(x)
		flag = False
		for i in range(self.m):
			if self.table[h] != None:
				for i in self.table[h]:
					if i == x:
						flag = True
		return "sim" if flag else "não"

controle = Table(10)
controle.insert('João')
controle.insert('Maria')
controle.insert('José')
controle.hashPrint()
print(controle.isAuthorized('Carlos'))