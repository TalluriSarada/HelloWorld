def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2

# the test invocation ensures that the protection works properly - the output is:none
print(bmi(352.5, 1.65))
def lb_to_kg(lb):
    return lb * 0.45359237
print(lb_to_kg(1)) 
#o/p 0.45359237
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(1, 1)) #0.3302
print(ft_and_inch_to_m(6, 0)) #1.8288000000000002

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(6)) #1.8288000000000002

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))) #27.565214082533313







