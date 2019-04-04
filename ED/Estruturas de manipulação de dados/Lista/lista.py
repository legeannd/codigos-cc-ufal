class List:
    items = None
    last = None
    size = None

    def __init__(self, size):
        self.size = size
        self.items = [None]*size
        self.last = 0

    def isEmpty(self):
        return self.last == 0

    def isFull(self):
        return self.size == self.last

    def push(self, item, pos):
        if not self.isFull() and pos <= self.last:
            for i in range(self.last, pos, -1):
                self.items[i] = self.items[i-1]
            self.items[pos] = item
            self.last += 1
        else:
            return None
    def pop(self, pos):
        if not self.isEmpty() and pos < self.last:
            item = self.items[pos]
            for i in range(pos, self.last-1):
                self.items[i] = self.items[i+1]
            self.last -= 1
            return item
        else:
            return None

    def listPrint(self):
        for i in range(self.last):
            print(self.items[i])
        print('---')
        
lista = List(10)
print(lista.isEmpty())
print(lista.isFull())
lista.push('a', 0)
lista.push('b',1)
lista.listPrint()
lista.push('c',2)
lista.pop(1)
lista.push('k',1)
lista.listPrint()
