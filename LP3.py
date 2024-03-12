"""Write a Python script to print first 10 odd natural numbers in reverse order"""

def print_odd_numbers_reverse():
    for i in range(19, 0, -2):
        print(i, end=" ")

if __name__ == '__main__':
    print("First 10 odd natural numbers in reverse order:")
    print_odd_numbers_reverse()