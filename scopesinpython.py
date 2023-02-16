#def scope_test():
 #   x = 123

#scope_test()
#print(x)
#NameError: name 'x' is not defined

def scope_test():
    print(x)
x = 123
scope_test()
#The scope of a name (e.g., a variable name) is the part of a code where the name is properly recognizable.
def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
#The answer is: a variable existing outside a function has a scope inside the functions' bodies.

def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
#A variable existing outside a function has a scope inside the functions' bodies
#scope of a variable existing outside a function is supported only when getting its value

