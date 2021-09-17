mylist = ["apple","banana","figs","orange"]

print("length of list: ",len(mylist))
print ("access by index no: ", mylist[1])
print("access last element by negative index: ",mylist[-1])
print("range index in given range: ",mylist[1:3])
print("range index from start: ",mylist[:3])
print("range index to end: ",mylist[1:])
print("negative range index: ",mylist[-3:-1])
mylist[1] = 'strawberry'
print("change item value: ",mylist)

#loop through list
for fruit in mylist:
    print("looping:",fruit)

#check for presence
if "banana" in mylist:
    print("banana is present in list")
else:
    print("banana is not present")


mylist.append("banana")
print("append banana to list",mylist)

mylist.insert(1,"pineapple")
print("insert pineapple on 1st index",mylist)

mylist.remove("figs")
print("remove figs from list",mylist)

mylist.append("figs")
print("append figs to list",mylist)

mylist.pop()
print("remove based on index else remove last element: ",mylist)

mylist.append("figs");print("append figs to list",mylist)
del mylist[5]
print("delete based on index else remove last element: ",mylist) #del without index,clear empties the list

fruit_list = mylist.copy()
print("copied list: ",fruit_list) # if value added to main list wont be reflected in copied list

conso_list = mylist + fruit_list
print("join 2 list: ",conso_list)
for x in fruit_list:
    mylist.append(x)
print("using append to join lists: ",mylist)
mylist.extend(fruit_list)
print("extend the list: ",mylist)

mynewlist = list(("apple","orange"))
print("build list using list constructor: ",mynewlist)