# create a 2D array

row = int(input("Enter number of rows in an array: "))
column = int(input("Enter number of columns in an array: "))
arr = []

for i in range (row):
    row1 = []
    for j in range(column):
        cell = int(input(" Enter the element: "))
        row1.append(cell)
    arr.append(row1)

print("array: ")
for row1 in arr:
    print(row1)








