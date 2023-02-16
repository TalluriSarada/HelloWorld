hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# Step 1: write a line of code that prompts the user
hatReplace = int (input("What number should be in the  middle? "))
# to replace the middle number with an integer number entered by the user.
hatList[2] =hatReplace
# Step 2: write a line of code that removes the last element from the list.
del hatList[-1]
# Step 3: write a line of code that prints the length of the existing list.
print("New list length: ", len(hatList))
print(hatList)
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
###
numbers.append(4)
print(len(numbers))
print(numbers)
###append() and insert()
numbers.insert(0, 222)
print(len(numbers))
print(numbers)
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)
#Adding elements to a list: continued
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
#Making use of lists
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)
# swap the list's elements to reverse their order
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

