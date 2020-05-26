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
row2,col2 = arr1.shape

arr3 = zeros((row1,col2))

print(arr3)