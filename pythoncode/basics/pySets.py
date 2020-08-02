myset = {"apple","orange","strawberry"}
print(myset,"length of set:",len(myset))

for fruit in myset:
    print("accessing set:",fruit)

print("check for element presence: ","banana" in myset)

#adding elements
myset.add("banana");myset.update(["figs","peach"]);print("after adding new elements",myset)

#remove elements
myset.remove("orange");myset.discard("figs");myset.pop();print("after removing: ",myset)

# del,clear works in same manner as list
#Joining 2 sets
myfruitset ={"apple","figs","orange"}
fruit_union = myset.union(myfruitset) # myset.update(myfruitset)
print("union of 2 sets: ",fruit_union)