"""write a program to calculate sum of 1st N natural numbers"""

n= int(input("Enter Num: "))
a = 1
j=0
while a<=n:
    j = j + a
    a +=1
print(j)
