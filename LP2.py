"""Write a Python script to print first N
even natural numbers"""

def print_even_numbers(N):
    for i in range(1, N+1):
        print(2*i, end=" ")

if __name__ == '__main__':
    N = int(input("Enter the value of N: "))
    print("First", N, "even natural numbers:")
    print_even_numbers(N)