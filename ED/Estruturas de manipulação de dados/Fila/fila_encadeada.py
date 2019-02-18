class Node:
    item = None
    next = None

    def __init__(self, item):
        self.item = item

class chainedQueue:
    start = None
    end = None
    size = 0

    def __init__(self):
        self.start = Node(None)
        self.end = self.start

    def isEmpty(self):
        return self.size == 0

    def push(self,item):
        self.end.next = Node(item)
        self.end = self.end.next
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            aux = self.start.next
            self.start.next = aux.next
            item = aux.item
            self.size -= 1
            if self.size == 0:
                self.end = self.start
            return item

    def queuePrint(self):
        aux = self.start.next
        while aux != None:
            print(aux.item)
            aux = aux.next
        print('---')
