import Queue
import numpy as np

class CircularQueue(Queue):
    def __init__(self, maxsize, dtype=np.int64):
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxsize = maxsize
        self.array = np.empty(self.maxsize)

    def isFull(self):
        return self.size == self.maxsize
    
    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        self.rear = (self.rear+1) % self.maxsize
        self.array[self.rear] = item
    
    def dequeue(self):
        x = self.array[self.front]
        self.front = (self.front+1) % self.maxsize
        return x
    
