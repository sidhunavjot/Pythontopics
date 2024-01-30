from array import *

# 1. define integer type
arr = []

# 2. ask how many values to be entered into array

n = int(input("how may values of array to be added"))

# 3. iterate 'i' for the size of array

for i in range(n):
    x = int(input("enter value in array: "))
    arr.append(x)

# 4. print the array

print(arr)

