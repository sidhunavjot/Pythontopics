#simple interest
#formula = (P*R*T)/100

P = int(input(" Enter principle").strip())
R = int(input(" Enter rate").strip())
T = int(input(" Enter time").strip())

def si(P,R,T):
    si_value = (P * R * T) / 100
    return si_value

try:
    valcatch = si(P,R,T)
    print("simple interest of principle ",P," is",valcatch)

except ValueError:
    print("invalid input")


