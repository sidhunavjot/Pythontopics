"""Write a python script to calculate sum of first N natural numbers."""

def nat(N):
    j=0
    for i in range (1, N+1):
        j +=i
    print(j)

if __name__=='__main__':
    N = int(input("Enter num: "))
    nat(N)