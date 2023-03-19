from platform import platform
from platform import machine
from platform import processor
from platform import system
from platform import version

from platform import python_implementation, python_version_tuple


print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system())

print(version())

print(python_implementation())

for atr in python_version_tuple():
    print(atr)   #the major part of Python's version;-3
                 #the minor part; 11 --the patch level number.1

