"""Write a Python script to print squares of first
N natural numbers."""

def naturalnumbers(N):
    for i in range (1, N+1):
        print(i**2)

if __name__=='__main__':
    N = int(input("Enter the num: "))
    naturalnumbers(N)