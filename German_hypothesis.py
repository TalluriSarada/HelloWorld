c0 = int (input("Enter a number: "))
if c0 < 1:
    print("Use a non-negative, non-zero number")
    exit
steps = 0

while c0 != 1:
      if c0 % 2 == 0:
         c0 = int(c0 /2)
      else:
          c0 = 3 * c0 + 1
      print(c0)
      steps += 1
print("Total number of steps:", steps)
#In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven)
#which can be described in the following way:
#take any non-negative and non-zero integer number and name it c0
#if it's even, evaluate a new c0 as c0 ÷ 2;
#otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
#if c0 ≠ 1, skip to point 2