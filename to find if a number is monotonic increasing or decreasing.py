# logic : https://www.youtube.com/watch?v=kn0XlPs9llY

"""

Approach : Using extend() and sort()

First copy the given array into two different arrays using extend()
Sort the first array in ascending order using sort()
Sort the second array in descending order using sort(reverse=True)
If the given array is equal to any of the two arrays then the array is monotonic


"""

arr = []
n = int(input("length of array: "))

for i in range(n):
    x = int(input("enter value in array: "))
    arr.append(x)

print("array: ",arr)

def isMonotonic(arr):

    o , p = [], []
    o.extend(arr)
    p.extend(arr)

    o.sort()
    p.sort(reverse=True)

    if (o==arr or p ==arr):
        return True
    return False
print("Is Monotonic ? ",isMonotonic(arr))