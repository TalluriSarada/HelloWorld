#tuples and dictionaries
#tuple_1 = (1, 2, 4, 8) A tuple is an immutable sequence type.
#sequence types and mutability
#A sequence type is a type of data in Python which is able to store more than one value 
# (or less than one, as a sequence may be empty), 
# and these values can be sequentially (hence the name) browsed, element by element.
#mutability - is a property of any of Python's data that describes its readiness to be freely changed during
#  program execution. 
# There are two kinds of Python data: mutable and immutable.
#Mutable data can be freely updated at any time list.append(1)
my_tuple = (1, 10, 100, 1000)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])
for elem in my_tuple:
    print(elem)
