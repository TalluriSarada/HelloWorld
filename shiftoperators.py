var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
#Binary left shift and binary right shift 
# 17 >>1 (17 floor-divided by 2 to the power of 1) =8
# (shifting to the right by one bit is the same as integer division by two)
# 17 <<2  17 multiplied by 2 to the power of 2 =68
# (shifting to the left by two bits is the same as integer multiplication by four
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
#logical operator
