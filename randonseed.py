from random import random, seed # will produce five pseudorandom values 
seed(0)# fact that the seed is always set with the same value, the sequence of generated values always looks the same.
for i in range(5):
    print(random())
