"""use following ways to find max:

using if-condition
using def function if-condition
using max function
using Ternary operator
Using lambda function
Using list comprehension
Using sort() method

"""


#using if-condition

a = int(input("enter your 1st int number").strip())
b = float(input("enter 2nd float number").strip())

c = float(a)

if c > b:
    print("a is grater then c")
elif c==b:
    print("a and b are equal")
else:
    print("b is greater than a")

# using def function if-condition

def GNum(c,b):
    if c > b:
        return (print("a is grater then c using def function",a))
    elif c == b:
        return (print("a and b are equal using def function",a))
    else:
        return (print("b is greater than a using def function",b))
GNumVal = GNum(c,b)

print(GNumVal)

# using max function

maxNum = max(c,b)
print("Max using max function",maxNum)

#using Ternary operator

"""This operator is also known as conditional expression are operators that evaluate something based on a condition being true or false. 
It simply allows testing a condition in a single line"""

print("using ternary operator",a if c>=b else b)

#Using lambda function

maxLamb = lambda c,b: a if c>=b else b
maxLambResult = maxLamb(c,b)
print("max using lambda",maxLambResult)

#Using list comprehension

x = [a if c>=b else b]
print("using list comprehension",x)

#Using sort() method

y = [c,b]
y.sort()
print("using sort",y[-1])






