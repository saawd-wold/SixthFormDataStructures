from abc import ABC, abstractmethod

class Queue(ABC):
    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def isFull(self):
        pass