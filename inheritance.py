#inheritance - single level, multiple level and multiple inheritance

#constructor in inheritance
#how to use super() in inheritance - to access all the methods of the super class
#method resolution order - MRO - works left to right

class A:

    def __init__(self):
        print("In A's init")

    def feature(self):
        print("Feature 1A working")

    def feature2(self):
        print("Feature 2 working")


class B:

    def __init__(self):
        print('In Bs init')


    def feature(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")


class C(A,B):

    def __init__(self):
        super().__init__()
        print('In Cs init')

    def feature5(self):
        print("Feature 3 working")

    def feature6(self):
        print("Feature 4 working")

    def feat(self):
        super().feature4()

#a1 = A()
#b1 = B()
c1 = C()
c1.feat()