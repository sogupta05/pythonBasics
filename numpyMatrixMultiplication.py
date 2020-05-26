from numpy import *

arr1 = array([  [1,2,3],
                [3,2,1],
                [5,2,5]
            ])

arr2 = array([  [3,1],
                [5,2],
                [2,5]
            ])
row1,col1 = arr1.shape
row2,col2 = arr2.shape
col1row2 = col1
arr3 = zeros((row1,col2),'int')

for i in range(col2):
    for j in range(row1):
        for k in range(col1row2):
            arr3[j][i] += arr1[j][k]*arr2[k][i]
        print(arr3[j][i])
print(arr3)

