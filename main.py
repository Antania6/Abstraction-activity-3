from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass 

class human(animal):
    def move(self):
        print("I can walk and run")

class snake(animal):
    def move(self):
        print("I can slither")

class dog(animal):
    def move(self):
        print("I can run")

obj = human()
obj.move()
obj1 = snake()
obj1.move()
obj2 = dog()
obj2.move()

