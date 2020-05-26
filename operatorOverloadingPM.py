#polymorphism - one object many forms
#polymorphis used in - loose coupling, dependency injection, interfaces
#can be implemented in below 4 ways
#duck typing - if a bird walks like a duck, quacks like a duck, swims like a duck then its a duck
# so in duck typing polymorphism, if a class has the same function as in example "Execute" then it can be used in class
#laptop

#operator overloading  - behind the scene we are calling methods for operators like + - @ / etc
#method overloading
#method overriding

a = 5
b = 6

print(a+b)

print(int.__add__(a,b))

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1+ self.m2
        r2 = other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}' .format(self.m1,self.m2)

    def show(self):
        print(self.m1, self.m2)

s1 = Student(45,65)
s2 = Student(65,76)

s3 = s1+s2

s3.show()

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)