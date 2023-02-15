# Prompt the user to enter a word
# and assign it to the user_word variable.

userWord =input("Enter a word")
userrWord = userWord.upper()

# Complete the body of the for loop.
    
for letter in userWord:
    if letter in "AEIOU":
       continue
    print(letter)
#using the continue statement in loops;
#reflecting real-life situations in computer code.