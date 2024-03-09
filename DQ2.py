"""White a python script to calculate simple interest."""

p,a,t = map(int, input("Enter p, a, t : ").split(','))

def SI(p,a,t):
    si = (p*a*t)/100
    return si

print(SI(p,a,t))