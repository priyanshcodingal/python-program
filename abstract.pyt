from abc import ABC,abstractmethod

class AbcClass(ABC):
    def print(self, x):
        print("Passed value : ",x)

    @abstractmethod
    def task(self):
        print("Its abstract class")

class test_class(AbcClass):
    def task(self):
        print("implimented method")

ob = test_class()
ob.task()
ob.print(72627)