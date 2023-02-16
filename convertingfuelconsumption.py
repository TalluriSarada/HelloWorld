def liters_100km_to_miles_gallon(liters):
    miles = 100 * 1000 /1609.344 #62.1371
    gallons = liters / 3.785411784
    return miles /gallons
# Write your code here.
def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    kilometers = miles * 1609.344  / 1000
    km100 = kilometers /100
    return liters / km100
# Write your code here
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
#1 American mile = 1609.344 metres;
#1 American gallon = 3.785411784 litres.
#in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
#In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.