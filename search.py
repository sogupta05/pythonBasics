# searching for a number and its index in an array
from array import *
from math import *
arr = array('i',[34,55,77,44,36,7657,98,39,11,39])
print(arr)

num = int(input("Enter the number you want to search: "))
length = len(arr)

for i in range(length):
    if( num == arr[i]):
        print("Number",num,"is first found at",i+1,"position" )
        break
else:
    print('Number ',num, ' is not found in the array')

print(arr)
print()