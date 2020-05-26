#decorators: add the extra feature in the existing function
#we can write a function inside a function
# we can assign a function to a function
# we can pass function as an agrument
# we can modify a function without even touching the function
# this can be done by changing the behavior of existing function at the compile time
# functional programming
#This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner


@smart_div
def div(a,b):
     print(a/b)

#div1 = smart_div(div)   # this is equivalent to @smart_div, its a sugar syntax :)
#div1(2,4)

div(5,10)


# DECORATORS
def smart_div(func):

    def inner(a,b):
        if b == 0:
            print("division by zero is undefinded")
            return
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    print(a/b)

div(3,5)

#we can make general decorators that work with any number of parameter.
#In Python, this magic is done as function(*args, **kwargs).
#In this way, args will be the tuple of positional arguments and kwargs will be the dictionary of keyword arguments.
#Multiple decorators can be chained in Python.
#This is to say, a function can be decorated multiple times with different (or same) decorators.
#The order in which we chain decorators matter

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@percent
@star
def printer(msg):
    print(msg)
printer("Hello "*5)