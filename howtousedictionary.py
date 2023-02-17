dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}
words = ['cat', 'lion', 'horse']
# Print the values here.
print(dictionary['cat'])
print(phone_numbers['Suzy'])
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

#for key in dictionary.keys():
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])
#How to use a dictionary: the keys()

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

#There is also a method named values(), which works similarly to keys(), 
#but returns values.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)