year = int(input("Enter a year: "))

#if the year number isn't divisible by four, it's a common year;
#otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, if the year number isn't divisible by 400, it's a common year;
#otherwise, it's a leap year.
# Write your code here.
if year < 1582:
       print("Not within the Gregoriam calendar period")
else:
    if year % 4 !=0:
         print("Common year")
    elif year % 100 !=0:
         print("Leap year")

    elif year % 400 !=0:
         print("Common year")
    else:
         print("Leap year")