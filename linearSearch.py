#checking for each and every element, if its a match

pos = -1
def linearSearch(list,num):
    for i in range(len(list)):
        if list[i]==num:
            globals()['pos'] = i  # for accessing global varibales
            return True
    else:
        return False



list = [9,8,4,2,9,65,77,83,9,4,90,-2]
num = 9


if  linearSearch(list, num) == True:
    print("Number {} is found at the {} position".format(num,pos+1))
else:
    print("Number {} is not present in the list".format(num))