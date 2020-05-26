#Binary search - list should be sorted
# keep the first index and the last index, find the mid and match the numbers,
#if the number is smaller than the mid number then move last to mid -1
# else if the number is greater than the mid number then move the first to mid + 1
# do it until the number is found or the list is done (list is done when first becomes greater than last



def binarySearch(list,num):
    first = 0
    last = len(list)

    while first <= last:   # <= because we want to check the mid when both first and last are at the same position
        mid = (first + last) // 2   # // returns integer division
        if num == list[mid]:
            return True, mid
        elif num < list[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return False, mid

list = [2,4,5,6,9,12,34,54,65,75,77]
num = 8
result, pos = binarySearch(list, num)

if  result == True:
    print("Number {} is found at the {} position".format(num,pos+1))
else:
    print("Number {} is not present in the list".format(num))