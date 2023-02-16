#the name of a list is the name of a memory location where the list is stored
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
#the name of an ordinary variable is the name of its content;
#the name of a list is the name of a memory location where the list is stored
# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
#The in and not in operators
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
my_list = [0, 3, 12, 8, 2]

#list largest
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
#If you need to save computer power, you can use a slice:
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

