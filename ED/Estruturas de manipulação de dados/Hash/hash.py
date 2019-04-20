class Table:
    def __init__(self, m):
        self.m = m
        self.table = [None]*m

    def hash(self, x):
        return x % self.m

    def insert(self, x):
        if self.table[self.hash(x)] == None:
            self.table[self.hash(x)] = []
        self.table[self.hash(x)].append(x)

    def delHash(self, x):
        flag = False
        for i in range(self.m):
            if self.table[i] != None:
                for j in self.table[i]:
                    if j == x:
                        self.table[i].remove(x)
                        flag = True
                        return
        if not flag:
            print('Elemento não existe')

    def hashLen(self, x):
        if self.table[x] != None:
            return len(self.table[x])
        else:
            return 0

    def hashPrint(self):
        for i in range(self.m):
            print(i, self.table[i])
        print('---')

#tabela = Table(8)
#print(tabela.hash(100))
#tabela.insert(100)
#tabela.insert(52)
#tabela.insert(44)
#tabela.insert(32)
#tabela.insert(33)
#tabela.hashPrint()
#tabela.delHash(52)
#tabela.hashPrint()
