class Node:
    item = None
    next = None

    def __init__(self, item):
        self.item = item

class ChainedStack:
    top = None
    size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def stackSize(self):
        return self.size

    def pile(self, item):
        aux = self.top
        self.top = Node(item)
        self.top.next = aux
        self.size += 1

    def unpile(self):
        if not self.isEmpty():
            item = self.top.item
            self.top = self.top.next
            self.size -= 1
            return item

    def stackPrint(self):
        aux = self.top
        while aux != None:
            print(aux.item)
            aux = aux.next
