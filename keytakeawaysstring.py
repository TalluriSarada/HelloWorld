#Python strings are immutable sequences and can be indexed, sliced
#There are two kinds of strings in Python:
#one-line 'string' or "string"
#multi-line strings  ''' string '''

print(len("\n\n"))

#Strings can be concatenated using the + operator, and replicated using the *

asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)

#The pair of functions chr() and ord() can be used to create a character using its codepoint

#chr(ord(character)) == 'b' #character
#ord(chr(codepoint)) == ' ' #codepoint

#list() – create a list consisting of all the string's characters;
#max() – finds the character with the maximal codepoint;
#min() – finds the character with the minimal codepoint.
#The method named index() finds the index of a given substring inside the string.

#What is the length of the following string

#"""
#"""  o/p 1

s = 'yesteryears'
the_list = list(s)
print(the_list[3:6])  #['t', 'e', 'r']

for ch in "abc":
    print(chr(ord(ch) + 1), end='') #bcd

