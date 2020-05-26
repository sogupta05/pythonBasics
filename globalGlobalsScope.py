#scope of the variable: global and local varibales
#global variable can be accessed inside the function too, when there is no local varibale with the same name is not defined

a = 10
print('Id of global a ',id(a))
def something():
    a = 9
   # global a - gives access to the global a
    x = globals()['a'] # gives the address of all the global variables, in this case we specify a as that is the only global variable
    print("address of x", id(x))
    print('x',x)
    print('in function a',id(a))
    # to change the value of x, do not assign a new value to x, as it will create a new address
    globals()['a'] = 15 #globals can be used to change the value of the global variable
    print('in function a', a)
    print(x,'x')
    print("address of x after globals()['a']", id(x))
    print("address of globals()['a']", id(globals()['a']))

something()
print('outside',a)
print('Id of global a after something() ',id(a))
