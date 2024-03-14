"""Write a Python script to calculate factorial of a number."""

def factorial(N):
    j = 1
    for i in range (1,N+1):
        j = j*i
    return j

if __name__ == '__main__':
    N = int(input("Enter Num: "))
    if N <0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("Factorial of", N, "is", factorial(N))