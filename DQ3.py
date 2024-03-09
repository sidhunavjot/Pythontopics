"""Write a python script to remove the last digit from a given number."""

a = int(input("Enter number"))

def remove(a):
    b = int(str(a)[:-1])
    return b
print(remove(a))