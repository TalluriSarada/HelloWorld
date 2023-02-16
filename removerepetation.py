my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = my_list[2:9]
# Write your code here.
for i in my_list:
    if i in newList:
       del my_list[i]
print("The list with unique elements only:")
print(my_list)
#write a program which removes all the number repetitions from the list