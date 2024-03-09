"""Write a program to check whether a given number is prime number or not"""

n = int(input("Enter number: "))
i = 2

while i <= n-1:
    if n % i == 0:
        break
    i+=1
if i == n:
    print("PRIME")
else:
    print("NOT PRIME")


