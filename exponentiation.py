#exponentiation math functions
from math import e, exp, log
#e a constant with a value that is an approximation of Euler's number (e)
#pow(x,y)  finding the value of xy (mind the domains)
print(pow(e, 1) == (log(e)))
#log(x)the natural logarithm of x
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0)) #log(x,b)the logarithm of x to base b
