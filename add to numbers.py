"""
ways to add various numbers :

Using “+” operator
Defining a function that adds two number
Using operator.add method
Using lambda function
Using Recursive function

"""
# Using “+” operator

a = int(input("1st num").strip())
b = int(input("2nd num").strip())

c = int(a+b)

print("total is",c)

#Defining a function that adds two number

def sum (a,b):
    return (a + b)

SumOfTwo = sum(a,b)

print("sume using function",SumOfTwo)

#Using operator.add method

import operator

SumUsingOperator = operator.add(a,b)
print("add using operator.add",SumUsingOperator)

#Using lambda function

"""Python Lambda Functions are anonymous functions means that the function is without a name. 
As we already know the def keyword is used to define a normal function in Python. 
Similarly, the lambda keyword is used to define an anonymous function"""

addtwo = lambda a, z:a+b

addtwotwo = addtwo(a,b)

print("add using lambda func",addtwotwo)

#Using Recursive function

def add_numbers_recursive(a, b):
    if b == 0:
        return a
    else:
        return add_numbers_recursive(a + 1, b - 1)


result = add_numbers_recursive(a, b)

print("add using recursive func",result)






