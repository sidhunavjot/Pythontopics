#Factorial of a Number Using Recursive approach

n = int(input("enter number ").strip())

def factorial(n):

    return 1 if (n==1 or n==0) else n*factorial(n-1)

result = factorial(n)

print("factorial  of ",n," with Recursive approach is ",result)

#Using Iterative approach

def factorial_iterative(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)

facto = factorial_iterative(n)
print("factorial with iterative ",facto)

#Using using In-built function

import math

facto_math = math.factorial(n)
print("facotrial using math func ",facto_math)

#using numpy

"""
import numpy
n=5
x=numpy.prod([i for i in range(1,n+1)])
print(x) 

"""