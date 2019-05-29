class Table:
	def __init__(self, m):
		self.m = m
		self.table = [None]*m

	def insert(self, x, oper):
		if oper == 't':
			h = self.hashTimes(x)
		elif oper == 'p':
			h = self.hashPow(x)

		if self.table[h] == None:
			self.table[h] = []
		self.table[h].append(x)

	def hashPrint(self):
		print('Tabela de hash:')
		for i in range(self.m):
			print(i, self.table[i])
		print('---')

	def hashTimes(self, x):
		x = str(x)
		first = ''
		second = ''
		for i in range(len(x)):
			if i < 3:
				first += x[i]
			else:
				second += x[i]
		return (int(first)*int(second)) % 8

	def hashPow(self, x):
		x = str(x)
		first = ''
		second = ''
		for i in range(len(x)):
			if i < 4:
				first += x[i]
			else:
				second += x[i]
		return (int(first)**int(second)) % 8

chaves = ['05132', '94023', '55917', '47925', '87539', '44963', '99999', '12345']
tabelaTimes = Table(8)
tabelaPow = Table(8)
for i in chaves:
	tabelaTimes.insert(i, 't')
	tabelaPow.insert(i, 'p')

tabelaTimes.hashPrint()
tabelaPow.hashPrint()