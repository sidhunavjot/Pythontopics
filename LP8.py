"""Write a Python script to calculate sum all the digits of a given number"""

def sum_digits(number):
    return sum(int(digit) for digit in str(number))

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    digit_sum = sum_digits(number)
    print("Sum of digits:", digit_sum)
