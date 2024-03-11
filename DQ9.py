"""Write a Python script to check whether a given number is positive, negative or
zero"""

def check(num):
    return num >0

def check2(num):
    return num <0

if __name__ == '__main__':
    num = int(input("Enter Num: "))
    if check(num):
        print("+ve")
    elif check2(num):
        print("-ve")
    else:
        print("zero")