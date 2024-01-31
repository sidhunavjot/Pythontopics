

arr = []
n = int(input("enter the length of array: "))

for i in range(n):
    x = int(input("enter value of array: "))
    arr.append(x)

print(arr)

# Using Native Approach

def largest(arr,n):
    max = arr[0]

    for i in range (n):
        if arr[i] > max :
            max = arr[i]
    return max

print("max from native approach: ",largest(arr,n))

# Using built-in function max()

def large(arr,n):
    ans = max(arr)
    return ans;
print("max from max function : ", large(arr,n))

# Using built-in function sort()

def sort(arr,n):
    arr.sort()
    return arr[n-1]
print("max from sort: ",sort(arr,n))

# Using reduce() function
from functools import reduce
def sortreduce(arr):
    ans = reduce(max,arr)
    return ans
print("max from resuce: ",sortreduce(arr))






