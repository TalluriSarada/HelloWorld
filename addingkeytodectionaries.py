dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
dictionary['swan'] = 'cygne'
dictionary.update({"duck": "canard"})
print(dictionary)
# adding new key to dictionaries

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
dictionary['swan'] = 'cygne'
dictionary.update({"duck": "canard"})
del dictionary['dog']
dictionary.popitem() #To remove the last item in a dictionary, you can use the
print(dictionary)
