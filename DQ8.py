"""Write a Python script to check whether a given year is a leap year or not"""

def leapyear(year):
    return (year%4==0 or year%400==0)

if __name__ == '__main__':
    year = int(input("Enter Year: "))
    if leapyear(year):
        print("Leap Year")
    else:
        print("Not a leap year")