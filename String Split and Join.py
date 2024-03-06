"""n Python, a string can be split on a delimiter."""
def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a


    # write your code here

if __name__ == '__main__':
    line = input("Enter a string: ")
    result = split_and_join(line)
    print(result)