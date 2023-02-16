for i in range(0, 11):
    if i % 2 != 0:
        print(i)
# for loop that counts from 0 to 10, and prints odd numbers to the screen
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1
# while loop to print odd numbers
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
# The program should iterate over characters in an email address, exit the loop when it reaches the @
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
#The program should iterate over a string of digits, replace each 0 with x