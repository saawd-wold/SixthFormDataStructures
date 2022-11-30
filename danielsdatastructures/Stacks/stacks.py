from danielsdatastructures.Stacks import AbstractStack

class Stack(AbstractStack):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.list = []
    def push(self, x):
        self.size += 1
        self.list.insert(0, x)
    def pop(self):
        self.size -= 1
        hd, *tl = self.list
        self.list = tl
        return hd
    def isEmpty(self):
        return True
    def isFull(self):
        return self.size == self.maxsize