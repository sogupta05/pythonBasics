# finding if the given number is prime or not
import math as m
x = 17
for i in (2,m.ceil(m.sqrt(x))):
    if (x%i == 0):
        print(x,' is Not Prime')
        break
else:
    print(x,' is a Prime Number')
print()
#finding first 100 prime numbers by diving by numbers so far and declaring number to be composite if more than 2 factors
#a = int(input('Enter a number'))
primeNumber = []
count = 0
primeCount = 0
i = 1
print('First hundred prime numbers')

while (primeCount < 100):
    i += 1
    for j in range(1, i+1):
        if(i%j==0):
            count += 1
            if count > 2:
                #print(i, 'is a Composite number.')
                count = 0
                break
    if count == 2:
        #print(i, 'is a Prime number.')
        if primeCount%10 == 0:
            print()
        #print(i,end=' ')
        primeNumber.append(i)
        count = 0
        primeCount += 1
print(primeNumber)
print('Completed')

# first 100 prime number using a list, and using list created at run time to check whether the next number is prime or not
#a = int(input('Enter a number'))
primeNumber = []
primeCount = 0
count = 0
i = 1
prime = 'True'
print('First hundred prime numbers')

while (primeCount < 100):
    i += 1
    for j in primeNumber:
        if(i%j==0):
            prime = 'False'
            break
    if (prime == 'True'):
        primeNumber.append(i)
        primeCount += 1
    prime = 'True'

for i in primeNumber:
    print(i, end=" ")
    count +=1
    if (count%10 == 0):
        print()
print('Completed')


# first hundred prime numbers, we are ignoring one and trying division only until number/2 coz after that number is only divisible by itself,
# this saves lot of computation

primeNumber = []
count = 0
primeCount = 0
i = 1
print('First hundred prime numbers')

while (primeCount < 100):
    i += 1
    for j in range(2,int(i/2)+1):
        if(i%j==0):
            break
    else:
        primeNumber.append(i)
        primeCount += 1
print(primeNumber)
print('Completed')

