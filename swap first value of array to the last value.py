arr = [2,3,4,6,7,9]

#Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.

print("aroiginal array: ",arr)
def swaparray(arr):
    size = len(arr)
    temp = arr[0]
    arr[0] = arr[size-1]
    arr[size-1] = temp
    return arr
print("swapped array: ",swaparray(arr))

# Approach #2: The last element of the list can be referred as list[-1].
# Therefore, we can simply swap list[0] with list[-1].

def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
