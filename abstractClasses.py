#abstact class - not directly supported in python but can be achieved using ABC module
# method which only has declaration but no definition, that is a method without a body, its an abstract method
# a class having at least on abstract method is called an abstract class
# an abstract class cannot have an instance/object
#when abstract class is inherited, all the subclasses have to implement all the astract methods
#abstract class acts as a blueprint for others - OOPS way - follow patterns - its a design aspect
# defining signature for other classes.  Eg. APIs, when u defining APIs then you want user to define those methods

from abc import ABC, abstractmethod


class Computer(ABC):

    def process(self):
        print("Running")

    @abstractmethod
    def abprocess(self):
        pass

class Laptop(Computer):
    def abprocess(self):
        print('its running in laptop')

class Whiteboard(Computer):
    def write(self):
        print('writing on whiteboard')
    def abprocess(self):
        print('its running in whiteboard')

class Programmer:
    def work(self,com):
        print('Solving bugs')
        com.abprocess()
#comp1 = Computer()
#comp1.abprocess()

comp2 = Laptop()
wht = Whiteboard()
prog1 = Programmer()
prog1.work(wht)