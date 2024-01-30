
#creating an array with user input

arr = []
n = int(input("how many value array ? "))
for i in range(n):
    x= int(input("enter value in array: "))
    arr.append(x)
print(arr)

#create a def function to add array items using for loop

def sum(arr):
    sum = 0
    for j in arr:
        sum = sum +j

    return (sum)

print("Value of sum: ",sum(arr))

# sum using sum() function

m = sum(arr)
print("value of sum from sum function: ",m)

# Sum of Array Using reduce method

"""Array.reduce() method is used to iterate over the array and 
get the summarized result from all elements of array."""
from functools import reduce
def sum2(arr):

    add = reduce(lambda a,b: a+b,arr)
    return add
print("sum from reduce method: ",sum2(arr))

# Using enumerate function

"""The enumerate () method adds a counter to an iterable and 
returns it in the form of an enumerating object."""
s=0
for i,a in enumerate(arr):
  s+=a
print("su,m with enumerate function: ",s)



