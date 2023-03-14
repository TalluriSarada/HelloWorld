from math import pi, radians, degrees, sin, cos, tan, asin
#pi → a constant with a value that is an approximation of π;
ad = 90
ar = radians(ad)#radians a function that converts x from degrees to radians;
ad = degrees(ar)#degrees acting in the other direction (from radians to degrees)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))#acos(x)the arccosine of x; atan(x)the arctangent of x.
print(asin(sin(ar)) == ar)#asin(x)the arcsine of x
