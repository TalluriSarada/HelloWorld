#""" method 1 - detailed variables"""
text = input("Enter a text\n")
a_string = text.lower().replace(' ', '')
b_string = a_string[::-1]                     

while not text:
    print("It's not a palindrome")
    break
else:
    if a_string == b_string:
        print("It's a palindrome")

    else:
        print("It's not a palindrome")
#https://ilpd-ms.blogspot.com/2022/02/python-2517-lab-palindromes.html
