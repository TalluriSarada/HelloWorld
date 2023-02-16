def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

# parameterized Functions
def message(what, number):
    print("Enter", what, "number", number)

# invoke the function
message("telephone", 11)
message("price", 5)
message("number", "number")
#parameters live inside functions (this is their natural environment)
#arguments exist outside functions, and are carriers of values passed to
# A function is a block of code that performs a specific task when the function is called (invoked).
#built-in functions which are an integral part of Python (such as the) print() input()
#user-defined functions which are written by users for users  lambda
def hello(name):    # defining a function
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function
#name error
hi()

def hi():
    print("hi!")
    #type error
    def hi():
    print("hi")

hi(5)