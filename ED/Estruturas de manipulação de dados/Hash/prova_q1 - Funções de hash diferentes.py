class Table:
    def __init__(self, m):
        self.m = m
        self.table = [None]*m

    def hash(self, x):
        return x % self.m

    def insert(self, x, oper):
        if self.table[self.hashSumorTimes(x, oper)] == None:
            self.table[self.hashSumorTimes(x, oper)] = []
        self.table[self.hashSumorTimes(x, oper)].append(x)

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

    def hashPrint(self):
        for i in range(self.m):
            print(i, self.table[i])
        print('---')

    def hashSumorTimes(self, x, oper):
        x = str(x)
        first = ''
        second = ''
        for i in range(len(x)):
            if i < len(x)/2:
                first += x[i]
            else:
                second += x[i]
        if oper == '+':
            return (int(first)+int(second))%10
        elif oper == '*':
            return (int(first)*int(second))%10

chaves = ['0513', 9402, 5591, 4792, 8753, 4496, 9999, 1234]

tabelaSum = Table(10)
tabelaTimes = Table(10)
for i in chaves:
    tabelaSum.insert(i, '+')
    tabelaTimes.insert(i, '*')

print('Tabela com hash de soma:')
tabelaSum.hashPrint()
print('Tabela com hash de multiplicação:')
tabelaTimes.hashPrint()
