"""Write Python script to count digits in a given number."""

def countdigit(N):
    return len(str(N))

if __name__ == '__main__':
    N = int(input("num: "))
    print(countdigit(N))

