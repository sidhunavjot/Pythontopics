"""
Check if an element exists in a list in Python

Using “in” Statement
Using a loop
Using any() function
Using count() function
Using sort with bisect_left and set()
Using find() method
Using Counter() function
Using try-except block

"""

# Using “in” Statement

a = [3,4,2,3,5,6,7]
i = 3

if i in a:
    print(i,"Exists in array",a)
else:
    print(i,"Does not Exists in array",a)

# Using a loop

for i in a:
    if (i == 3):
        print("exits")
    else:
        print("does not exist")


""" 

For more methods check url >> 
https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/?ref=lbp 

"""





