#"""  method 2 - reversed() function"""

text = input("Enter a text\n")
text = text.lower().replace(" ", "")
rev_text = "".join(reversed(text))

while not text:
    print("It's not a palindrome")
    break
else:
    if text.casefold() == rev_text.casefold():
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
