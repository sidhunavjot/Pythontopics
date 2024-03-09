"""Write python script to swap data of two
variables"""


def swaping(a, b):
    temp = a
    a = b
    b = temp
    return a, b



if __name__ == '__main__':

    a = int(input("Enter a number : "))
    b = input("Enter text: ")
    a,b = swaping(a,b)
    print("After swap: ")
    print("a = ",a)
    print("b = ", b)
