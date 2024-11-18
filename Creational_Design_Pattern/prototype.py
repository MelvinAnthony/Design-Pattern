from abc import ABCMeta, abstractmethod
import copy

class Prototype(metaclass = ABCMeta):
    #interface for clone
    @abstractmethod
    def Clone():
        pass


class ConcerateClass1(Prototype):
    def __init__(self,i =0 , s = '', l = [], d = {}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def Clone(self):
        return type(self)(
            self.i,
            self.s,
            self.l.copy(),
            self.d.copy()
        )
    
    def __str__(self):
        return f"{id(self)}\t i = {self.i}\t s = {self.s}\t l = {self.l}\t d = {self.d}"
    
if __name__ == '__main__':
    obj = ConcerateClass1(1, "Obj1", [1,2,3], {'a':1,'b':2,'c':3})
    print(obj)
    obj2 = obj.Clone()
    obj2.s = "Obj2"
    print(obj2)
