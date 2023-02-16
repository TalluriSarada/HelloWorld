def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
#meaning of the argument is dictated by its name, not by its position 
#- it's called keyword argument passing.
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(surname="Skywalker", first_name="Luke")
#TypeError: introduction() got an unexpected keyword argument 'surname'

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Call the adding function here.
adding(1, 2, 3)
#mixing positional and keyword arguments