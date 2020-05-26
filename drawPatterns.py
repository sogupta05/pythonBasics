#printing pattern
s = '1234'
for i in range(len(s)):
    print(s[i:])


# printing pattern
l1 = 'APQR'
l2 = 'ABCD'
for i in range(4):
    l1 = l1.replace(l1[i],l2[i])
    print(l1)
print()

#printing pattern
for i in range(4):
    for j in range(i+1):
        print(chr(65+j),end="")
    for k in range(i+1,4):
        print(chr(65+14+k), end="")
    print()
print()

# printing pattern
for i in range(4):
    for j in range(4):
        if(j <= i):
            print(chr(65 + j), end="")
        else:
            print(chr(65 + 14 + j), end="")
    print()
print()
# printing pattern
s1 = 'ABCD'
s2 = 'PQR'
for i in range(4):
    for j in range(i+1):
        print(s1[j],end="")
    for k in range(i,3):
        print(s2[k], end="")
    print()
print()
# printing pattern
for i in range(5):
    for j in range(1,5-i):
        print(i+j,end="")
    print()

# printing pattern
k = 4 #int(input("number of rows you want"))

for i in range(k):
    for j in range(i+1,k+1):
        print(j,end=" ")
    print()
print()
#printing pattern
for i in range(4):
    for j in range(4-i,0,-1):
        print(j,end="")
    print()
print()
#printing pattern
for i in range(5,1,-1):
    print((i-1)*"#")
#printing pattern
k = 4 #int(input("number of rows you want"))

for i in range(k):
    for j in range(i+1,k+1):
        print(j,end=" ")
    print()