class Fila:
    items = None
    start = None
    end = None
    size = None

    def __init__(self,size):
        self.size = size
        self.start = 0
        self.end = 0
        self.items = [None]*size

    def isEmpty(self):
        return self.start == self.end

    def isFull(self):
        return (self.end+1)%self.size == self.start

    def push(self, item):
        if not self.isFull():
            self.items[self.end] = item
            self.end = (self.end+1)%self.size
        else:
            print('Queue Full')

    def pop(self):
        if not self.isEmpty():
            item = self.items[self.start]
            self.start = (self.start+1)%self.size
            return item

    def queuePrint(self):
        i = self.start
        while i != self.end:
            print(i,' - ',self.items[i])
            i = (i+1)%self.size
