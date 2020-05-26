#bubble Sorting
from array import *

arr = array('i',[67,90,78,7,5,5,-8,45])

length = len(arr)

for i in range(length):
    for j in range(i+1,length):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)