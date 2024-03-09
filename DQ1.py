"""write a python script to calculate area of a rectangle"""

a,b = map(int, input("Enter sides of rectangle ").split(','))


def area(a,b):
    ar = a*b
    return ar
print(area(a,b))
