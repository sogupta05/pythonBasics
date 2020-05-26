#Bubble sort - smallest number bubbles up or the biggest number sinks down
# every iteration two elements are compared and based on the condition swapped
# so the biggest element will sink down and the smallest will start bubbling up

def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(0,i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        print(list)

    return list

list = [66,89,98,101,900,8,65,44,35,67,9,53,63,55,56]


lst = bubbleSort(list)
print(lst)
