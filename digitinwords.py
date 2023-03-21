text = (input("Please enter your birthday as numbers only: "))
if len(text) != 8 or not text.isdigit():
    print("Date format is invalid")
else:
    while len(text) > 1:
        the_sum = 0
        for i in text:
            the_sum += int(i)
        text = str(the_sum)
    print(text)
#method 2
# date of birth
dob = input("Please enter your birthday as numbers only: ")
# digit of life
dol = 0 
for num in dob:
    dol += int(num)
       
    if dol > 9:
        dol = dol % 10 + dol // 10
# printing result
print("The Digit of Life Number: " + str(dol))
