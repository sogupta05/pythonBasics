#polymorphism - one object many forms
#polymorphis used in - loose coupling, dependency injection, interfaces
#can be implemented in below 4 ways
#duck typing - if a bird walks like a duck, quacks like a duck, swims like a duck then its a duck
# so in duck typing polymorphism, if a class has the same function as in example "Execute" then it can be used in class
#laptop
# Dependency injection mechanism - Duck typing - the class you are implementing knows only the behaviour of the dependency
#(function signature) but not the concrete implementation.  In the dynamic languages you have Duck Typing which means all
#relative dependencies should implement the same methods(ie execute in the example). So by this way a single class can
#use any of these dependencies at any time without knowing anything about them at the compile time.
# With NORMAL typing, suitability is determined by an object's type. In DUCK typing, an object's suitability is
# determined by the presence of certain methods and properties, rather than the type of the object itself.
#Duck typing is similar to, but distinct from structural typing. Structural typing is a static typing system that
# determines type compatibility and equivalence by a type's structure, whereas duck typing is dynamic and
# determines type compatibility by only that part of a type's structure that is accessed during run time.

#operator overloading
#method overloading
#method overriding

class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class Slime:

    def execute(self):
        print("Code convention")
        print("Syntax")
        print("Compiling")
        print("Running")

class Laptop:

    def coding(self, ide):
        ide.execute()

ide = Slime()

lap = Laptop()
lap.coding(ide)

