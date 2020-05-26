import math

for i in range(1,501,1):
    if(pow(i,2) <= 500):
        print('square root of',pow(i,2), 'is',i)

for i in range(1,501,1):
    if(i % math.sqrt(i) == 0):
        print(i, end="  ")
print()

for i in range(1,501,1):
    x = int(math.sqrt(i))
    if(i/x == x):
        print(i, end="  ")
print()

print(math.ceil(math.sqrt(501)))


for i in range(1,math.ceil(math.sqrt(501))):
    print(i**2, end= "  ")

print()
for i in range (1,501):
    if math.sqrt(i) % 1 == 0:
        print(i,end="  ")