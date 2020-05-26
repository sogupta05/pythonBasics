a = 5    #101
b = 6    #110
print('Initial a = ',a,'  Binary a = ',bin(a))
print('Initial b = ',b,'  Binary b = ',bin(b))

a =  a ^ b
print(a)
print('After first XOR a = ',a,'  Binary a = ',bin(a))
print('After first XOR b = ',b,'  Binary b = ',bin(b))
b = a ^ b
print(b)
print('After second XOR b = ',b,'  Binary b = ',bin(b))
print(a)
print('After second XOR a = ',a,'  Binary a = ',bin(a))

a = a ^ b
print(a)
print('After final XOR a = ',a,'  Binary a = ',bin(a))
print('After final XOR b = ',b,'  Binary b = ',bin(b))

c = 7
d = 9

print('Initial c = ',c,'  Binary a = ',bin(c))
print('Initial d = ',d,'  Binary b = ',bin(d))
c,d = d,c
print('Final c = ',c,'  Binary a = ',bin(c))
print('Final d = ',d,'  Binary b = ',bin(d))

print()

#swapping with extra variable
a = 5
b = 7

a = a+b
b = a-b
a = a-b

print(a,end=" ")
print(b)