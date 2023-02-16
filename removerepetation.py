my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = my_list[2:9]
# Write your code here.
for i in my_list:
    if i in newList:
       del my_list[i]
print("The list with unique elements only:")
print(my_list)
#write a program which removes all the number repetitions from the list

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)

list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # outputs True
print("A" in my_list)  # outputs True
print(3  in my_list)  # outputs True
print(False in my_list)  # outputs False