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

    def hashLen(self, x):
        if self.table[x] != None:
            return len(self.table[x])
        else:
            return 0

    def hashPrint(self):
        for i in range(self.m):
            print(i, self.table[i])
        print('---')

    def hashSumorTimes(self, x, oper):
        x = str(x)
        first = 0
        second = 0
        for i in range(len(x)):
            if i < len(x)/2:
                first += ord(x[i])
            else:
                second += ord(x[i])
        if oper == '+':
            return (int(first)+int(second))%10
        elif oper == '*':
            return (int(first)*int(second))%10


votos=["basquete","futebol","futebol","basquete","judo","volei","futebol","basquete","futebol","volei",
"judo","judo","futebol","ciclismo","judo"]

tabelaVotos = Table(10)
for i in votos:
    tabelaVotos.insert(i, '*')
