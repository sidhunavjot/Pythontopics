arr = []
x = int(input("length of array: "))

for i in range(x):
    val = int(input("enter number in array: "))
    a = arr.append(val)

print(arr)

n =int(input("a number 'n' to devide with: "))
def rem(arr,n):
    pro = 1
    for num in arr:
        pro = pro * num
    return pro%n

print("value needed: ",rem(arr,n))




