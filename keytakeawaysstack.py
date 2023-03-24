#there is a class named Snakes, write the very first line of the Python class declaration,
#expressing the fact that the new class is actually a subclass of Snake.

class Python(Snakes):


#Something is missing from the following declaration – what?
class Snakes:
    def __init__():
        self.sound = 'Sssssss'
#self

#Modify the code to guarantee that the venomous property is private.

class Snakes:
    def __init__(self):
        self.venomous = True
# self._venomous
