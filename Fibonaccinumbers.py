def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))
#sequence of integer numbers-Fibonacci numbers
#the first element of the sequence is equal to one (Fib1 = 1)
#the second is also equal to one (Fib2 = 1)
#every subsequent number is the the_sum of the two preceding numbers:(Fibi = Fibi-1 + Fibi-2)

#The Fibonacci numbers definition is a clear example of recursion. Fibi = Fibi-1 + Fibi-2 -recursion
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))

#factorial function recursion
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)



