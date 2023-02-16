word_without_vowels = ""
# Prompt the user to enter a word
# and assign it to the user_word variable.
userWord =input("Enter a word")
userrWord = userWord.upper()
for letter in userWord:
# Complete the body of the loop.
  if letter in "AEIOU":
       continue
  word_without_vowels += letter
# Print the word assigned to word_without_vowels.
print(word_without_vowels)