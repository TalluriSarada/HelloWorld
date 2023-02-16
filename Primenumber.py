def is_prime(num):
    divisor =2
    while divisor < num:
       if num % divisor ==0:
           return False
       divisor += 1
    return True
# Write your code here.
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
#is called prime  takes one argument (the value to check)
#returns True if the argument is a prime number, and False otherwise.