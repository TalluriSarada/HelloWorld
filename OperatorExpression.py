hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

#For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

mins = mins + dura
hour = hour + mins //60
print(hour,":",mins % 60, sep="")