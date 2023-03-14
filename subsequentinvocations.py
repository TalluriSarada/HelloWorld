from random import randint
#program very likely outputs a set of numbers in which some elements are not unique:
for i in range(10):
    print(randint(1, 10), end=',')

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))


