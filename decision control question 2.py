"""print grade obtained in a test. Take marks obtained by user and display the grade

90 <marks<=100 -> A
80 <marks<=90 -> B
70 <marks<=80 -> C
60 <marks<=70 -> D
50 <marks<=60 -> E
below 50       -> F

"""

Marks = int(input("Enter marks of student: "))

if 90 < Marks <= 100:
    print("Grade A")
elif 80 < Marks <= 90:
    print("Grade B")
elif 70 < Marks <= 80:
    print("Grade C")
elif 60 < Marks <= 70:
    print("Grade D")
elif 50 < Marks <= 60:
    print("Grade E")
else:
    print("Grade F")