a = [1,2,3,4,5,6]

val = 3

""" DELETE """

#delete aaray with an element

if val in a:
    a.remove(val)
    print(a)

#delete and array with index

del a[3]
print("2nd deleted array: ",a)

""" SORT """

b = [3,6,4,3,8,9,0]

sort = sorted(b)
print("sorted array: ",sort)

reverse = sorted(sort,reverse=True)
print("reverse sort: ",reverse)


""" SEARCH """

c = [4,2,2,4,5,6,9]
se = 4

if se in c:
    print("number present")
else:
    print("number NOT present")