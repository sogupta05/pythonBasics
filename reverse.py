# reversing the array

from array import *
from math import *

arr = array('i',[34,55,77,44,36,7657,98,39])
print(arr)
revarr = array(arr.typecode,[])

for i in range(len(arr),0,-1):
    revarr.append(arr[i-1])

print(revarr)
print()

## reversing the array

arr = array('i',[34,55,77,44,36,7657,98,39,11])
print(arr)
length = len(arr)

if(length%2 == 0):
    len = int(length/2)
else:
    len = ceil(length/2)

for i in range(len):
    temp = arr[i]
    arr[i] = arr[length-1-i]
    arr[length-1-i] = temp

print(arr)

print()


# reversing the array

arr = array('i',[34,55,77,44,36,7657,98,39,11,39])
print(arr)
length = len(arr)

if(length%2 == 0):
    len = int(length/2)
else:
    len = ceil(length/2)

for i in range(len):
    arr[i], arr[length-1-i] = arr[length-1-i],arr[i]

print(arr)
print()