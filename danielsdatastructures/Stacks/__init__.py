from . import stacks
from abc import ABC, abstractmethod

class AbstractStack(ABC):
    @abstractmethod
    def push(self, item):
        pass
    def pop(self):
        pass
    def isEmpty(self):
        pass
    def isFull(self):
        pass
    pass

print("Stacks' x: ", stacks.x)