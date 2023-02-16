def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()

def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")

def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")
#syntax error a non-default argument c  follows a default argument b
def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)