class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def isEmpty(self):
        return (self.start == None)

    def push(self, value):
        node = Node(value)

        if(self.isEmpty()):
            self.start = node
        else:
            self.end.next = node

        self.length += 1
        self.end = node

    def pop(self):
        if(self.isEmpty()):
            return None
        value = self.start.item
        self.start = self.start.next
        self.length -= 1

        return value

    def queuePrint(self):
        aux = self.start
        while(aux != None):
            print(aux.item)
            aux = aux.next

class Node:
    def __init__(self, value):
        self.item = value
        self.next = None
