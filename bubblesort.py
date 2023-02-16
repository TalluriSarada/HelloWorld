#bubble sort 8 10 6 2 4 -- we compare the adjacent elements, and by swapping some of them
#8 6 10 2 4 - 8 6 2 10 4 --8 6 2 4 10 -- 6 8 2 4 10 --6 2 8 4 10 --6 2 4 8 10 --2 6 4 8 10 --2 4 6 8 10
my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  
        # If we end up here, we have to swap the elements.

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

