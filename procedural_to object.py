class Stack: #Defining the stack class.
    def __init__(self): #Defining the consturctor function.
        print("Hi")

stack_object =Stack() #Instantiating the objects.

#object approach
class Stack:
    def __init__(self):
        self.stack_list = []


stack_object =Stack()
print(len(stack_object.stack_list))
