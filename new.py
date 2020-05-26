# compile time error - syntatical error
# logical error - error in logic like, instead of modulo you used division
# runtime error - like expecting int input from user but user enters character/string

a = 3
b = 9

try:
    print("Resource opened")
    print(a/b)
    x = input("enter a number: ")
    y = input("enter a number: ")
    z = y + z
except ZeroDivisionError as e:
    print("Hey, you are trying division by zero", e)
except ValueError as e:
    print("Hey you entered a string literal instead of an interger", e)
except Exception as e:
    print("Hey there is an error", e)
finally:
    print("Resource Closed")
print('bye')