x = 5

from danielsdatastructures.Stacks import AbstractStack

class Stack(AbstractStack):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.list = []
    def push(self, x):
        print(x)
    def pop(self):
        print("pop")
    def isEmpty(self):
        return True
    def isFull(self):
        return False