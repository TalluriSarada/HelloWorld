def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 :     
       return True 
    elif year % 400 == 0 :
       return True
    else :
       return False
# Your code from LAB 4.3.1.6.
def days_in_month(year, month):
    monthDays=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month ==2:
       return 29
    return monthDays[month-1]
# Your code from LAB 4.3.1.7.
def day_of_year(year, month, day):
    if  year <1582:
         return None
    if  month > 12 or month < 1:
         return None
    if  day > days_in_month(year,month) or day < 1:
         return None
#calculate days
    totaldays=day
    month = month -1
    while month > 0:
        totaldays +=days_in_month(year,month)
        month -=1
    return totaldays

print(day_of_year(2000, 11, 30))
# write and test a function which takes three arguments (a year, a month, and a day of the month) and 
# returns the corresponding day of the year, or returns None if any of the arguments is invalid.
#projecting and writing parameterized functions;
#utilizing the return statement;
#building a set of utility functions;
#utilizing the student's own functions.
