from abc import ABC, abstractmethod

class AbstractStack(ABC):
    @abstractmethod
    def push(self, item):
        pass
    @abstractmethod
    def pop(self):
        pass
    @abstractmethod
    def isEmpty(self):
        pass
    @abstractmethod
    def isFull(self):
        pass
