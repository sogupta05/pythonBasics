#Actual arguments are the ones we are sending while calling the function - there are 4 types, POSITION, KEYWORD, DEFAULT, VARIABLE
#Formal arguments are the ones which are given while defining the function

def add(*b): #Variable length argument : b is a variable argument, *b is sent as a tuple.  Tuple is immutable
    print(b)
    c = 0
    for i in b:
        c +=i
    print(c)

add(5,6,34.98,78)  #Variable argument : b is a variable argument, *b is sent as a tuple

def person(name,lname='G',age=18): #default argument should always be the last argument
    print(name)
    print(age-5)

person('Sonia','gupta',67) #position argument - decided merely by position of the arguments being passed
person(age= 45,lname='gupta', name='sonia')  # keyword agrument - decided by the keyword, postiion of the argument not important
person('sonia') # Default argument - already value is provided in the function, so not necessary to send it while calling
print()
#keyworded variable length argument - double ** before data tells that its a keyworded variable argument
# functions that can work with any number of arguments - function(*args, **kwargs).
# In this way, args will be the tuple of positional arguments and kwargs will be the dictionary of keyword arguments.
def person(*args, **kwargs):
    for e in args:
        print(e)
    for k,w in kwargs.items():
        print(k,w)

person('sonia',age=38,city='NZ',mob=9878758987)
person()