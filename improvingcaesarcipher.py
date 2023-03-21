text = input("Enter your message: ")
shift_value = int(input("Please Enter a Shift Value from 1 - 25: "))

def encryped(text , shift_value):
    cipher = ''
    for char in text:
        if char == ' ':
            cipher += char
        elif char.isdigit():
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + shift_value - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + shift_value - 97) % 26 + 97)
    return cipher
print("The Encrypted string is:\n ", encryped(text, shift_value))
