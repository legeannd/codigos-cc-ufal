class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class chainedList:
    def __init__(self):
        self.start = Node(None)
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, item, *pos):
        pos = pos if pos != () else self.size
        if pos <= self.size:
            p = self.start
            for i in range(pos):
                p = p.next
            aux = Node(item)
            aux.next = p.next
            p.next = aux
            self.size += 1
        else:
            print('Invalido')

    def pop(self, pos):
        if not self.isEmpty() and pos < self.size:
            p = self.start
            for i in range(pos):
                p = p.next
            aux = p.next
            p.next = aux.next
            item = aux.item
            del aux
            self.size -= 1
            return item
        else:
            return None

    def listPrint(self):
        p = self.start
        for i in range(self.size):
            p = p.next
            print(p.item)
        print('---')
