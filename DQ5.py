"""Write a python script to check whether a given number is divisible by 5 or not"""

def div(n):
    if n % 5 ==0:
        print("Yes")
    else:
        print("NO")


if __name__ == '__main__':
    n = int(input("Enter Num: "))
    v = div(n)
    print(v)

