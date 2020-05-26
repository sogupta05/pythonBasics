

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

resultadd, resultsub = add_sub(5,4)
print(resultadd, resultsub)

def update(x):
    print('x1 ', id(x))
    x = 8
    print('x2 ', id(x))
    print('x2:8: ', id(8))
    print(x)

a = 90  # integers are imutable
print('a1 ',id(a))
print('a1:90 ',id(90))
update(a)
print('a2 ',id(a))
print('a2:90 ',id(90))

# list is mutable
def update(lst):
    print('Lst address before update', id(lst))
    lst[1] = 23
    print('Lst address after update', id(lst))
    print('Inside update', lst)

lsst = [10,20,30]
print('Before calling update', lsst)
print('Lst address before update', id(lsst))
update(lsst)
print('Lst address after update', id(lsst))
print('After calling update', lsst)