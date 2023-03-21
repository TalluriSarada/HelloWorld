# Caesar cipher.
#This cipher was (probably) invented and used by Gaius Julius Caesar 
#and his troops during the Gallic Wars
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
#it accepts Latin letters only 
#all letters of the message are in upper case  Romans knew only capitals
