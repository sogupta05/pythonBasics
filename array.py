from array import *

vals = array('i',[5,6,8,7,6,3,1])
print(sorted(vals))

#newArr = array(vals.typecode, (a*a for a in vals))

#for e in newArr:
 #   print(e)

arr = array('i',[])
n = int(input('Enter the length of the array: '))
for i in range(n):
    x = int(input('Enter the value: '))
    arr.append(x)

print(arr)
print()
val = int(input('Enter the value to search: '))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k +=1

print(arr.index(val))

#creating an array by taking values from the user
n = int(input("Enter a size of array: "))

a = array('i',[int(input()) for x in range(n)])
print(a)