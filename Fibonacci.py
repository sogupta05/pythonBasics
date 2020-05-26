import math as m

num1 = 0
num2 = 1
print('First 50 Fibonacci numbers are:')
print(num1, end = " ")


for i in range (1, 50):
    print(num2, end=" ")
    num2 = num1 + num2
    num1 = num2 - num1
   # print(num2, end=" ")
print()

fib = [0,1]
type(fib)
for i in range(1,49):
    fib.append(fib[-1]+fib[-2])
print('USing list First 50 Fibonacci numbers are:')
for i in fib:
    print(i, end =" ")
print()

x,y=0,1
print(x, end=" ")
for i in range(1,50):
    print(y, end=" ")
    x,y=y,x+y
print()

#function

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)


fib(10)

#function for printing fibnacci numbers less than 100

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    c = a + b
    while c < 100:
        print(c)
        a = b
        b = c
        c = a + b




fib(10)