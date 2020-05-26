from functools import reduce
# convert celcius to fahrenheit
celcius = [20, 30, 31,32,33,34,35,45,51, 36, 37,38,50,70,-34]

fahrenheit = list(map(lambda c: c*1.8+32 ,celcius))

print(fahrenheit)

bigcelcius = list(filter(lambda c: c>38 ,celcius))
print(bigcelcius)

maxcelcius = reduce(lambda a,b: a if a>b else b,celcius)
print(maxcelcius)
print()


#functions are objects in python

f = lambda a,b: a*b   #anonymus function - functions without name, can only have one expression, can have multiple arguments
result = f(5, 6)

print(result)
print()

#lambda explame with filter()
def is_even(n):
    return n+2

def update(n):
    return n*2

def add_all(a,b):
    return a+b

nums = [3,4,2,5,7,9,8,1,10]

#evens = list(filter(is_even,nums))   #filter takes n gives sequence,  takes a function n a list/sequence
#filter filters out some values from sequence and returns the rest
evens = list(filter(lambda n : n%2==0,nums))
print(evens)

#double all the values, example of map, MAp - performs a function on each item in the sequence
#it returns mostly the same number of elements
doubles = list(map(lambda n : n*2 ,evens))
print(doubles)

#reduce - belongs to module functools,
# reduce reduces the sequence to a value, like it keeps adding two numbers in the list till all are added
# reduce probably can take only two variables in the lambda fumction
#reduce takes the first two values in the a and b, then the result it moved to a and next element in swquence to b

sum = reduce(lambda a,b: a+b,doubles)
print(sum)
print()


#map and lambda example
a,b = [int(x) for x in input('Enter two values separated by space: ').split()]

tup=(lambda c,d: c+d, lambda c,d: c-d, lambda c,d: c*d, lambda c,d: (c+d)/2)

dic = dict(zip(('sum','difference','product','average'),map(lambda x:x(a,b),tup)))

for j in dic:
    print('{} : {}'.format(j,dic[j]))