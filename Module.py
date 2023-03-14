#import math
#print(math.sin(math.pi/2))
import math
#how the two namespaces (yours and the module's one) can coexist.
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

