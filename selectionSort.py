#saving the minimun value position and swapping at the end of inner loop

def selectionSort(list):

    for i in range(len(list)-1):
       minpos = i
       for j in range(i+1,len(list)):
           if list[minpos] > list[j]:
               minpos = j
       temp = list[i]
       list[i] = list[minpos]
       list[minpos] = temp
       print(list)

    return list

list = [8,65,44,35,67,9]
lst = selectionSort(list)
print(lst)