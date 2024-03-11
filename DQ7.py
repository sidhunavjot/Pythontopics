"""Write a python script to check whether a given number is a three digit
number
or not"""
#question update
def threedigit(num):
    return 100 <= num <=999


if __name__ =='__main__':
    num = int(input("Enter the number: "))
    if threedigit(num):
        print("3 digit num")
    else:
        print("Not a 3 digit")



