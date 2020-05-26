#Instance variable and class/static variable
#Methods - instance method, class method and static method. class and static methods are different in methods
# instance methods: Accessors and Mutators

class Student:

    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1            # instance variables
        self.m2 = m2
        self.m3 = m3

    def avg(self):   #instance method, as we are passing self
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):  # Accessor method of Instance method type - only fetch the value of the variable. do not change it
        return self.m1

    def set_m1(self,value):  #Mutator method of Instance method type - change the value of the variable
        self.m1 = value

    @classmethod     #decorator needed to create the class method
    def getSchool(cls):   #Class method, accessed via class
        cls.school = 'New Telusko'
        return cls.school


    @staticmethod
    def info():    #static method
        print("this is student class ....in abc module")

s1 = Student(34,34,54)
s2 = Student(45,34,78)

print(s1.avg())
print(s2.avg())

print(s1.getSchool())
print(Student.getSchool())

Student.info()