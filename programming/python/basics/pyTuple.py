mytuple =("apple","banana","orange")
print("type of data stored:",type(mytuple),"length of tuple:",len(mytuple))
print("access tuple: ",mytuple[1])
print("access tuple negative index: ",mytuple[-1])
print("range: ",mytuple[1:2])

#change tuple value - workaround for adding values to immutable tuple
mytuplelist = list(mytuple)
mytuplelist[1] = 'figs'
mytuple = tuple(mytuplelist)
print("add value to tuple: ",mytuple)

for tup in mytuple:
    print("elements in tuple: ",tup)

#check for value existence

if "strawberry" in mytuple:
    print("strawberry is in tuple")
else:
    print("no present")