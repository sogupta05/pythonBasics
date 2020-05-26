# list, send to function and return the number of odd and even numbers in that list

def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

lst = [20,25,14,19,16,24,28,47,26]

#lst = [int(input('Enter one number and press enter: ')) for x in range(10)]

even, odd = count(lst)

#print('Even : {} and Odd : {}'.format(even, odd))
print(f'Even : {even} and Odd : {odd}')

def person(lst):
    bigNames = []
    for e in lst:
        if len(e) > 5:
            bigNames.append(e)
    return bigNames,len(bigNames)


names = input('Enter all the names separated by a comma: ')
namesLst = names.split(',')
for name in namesLst:
    print(name)
print(namesLst)
bignames, len = person(namesLst)
print(bignames, len)