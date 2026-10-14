from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("i can walk and run")

class Snake(Animal):
    def move(self):
        print("i can crawl")

class Dog(Animal):
    def move(self):
        print("i can bark")
h = Human()
h.move()

s = Snake()
s.move()

d = Dog()
d.move()