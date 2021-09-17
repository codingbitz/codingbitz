import array as ar
a =ar.array('i',[1,2,3])
print(a)

print(a.index(2))
a[2]=8
a.insert(1,4)
print(a[1])
a.pop(2)
a.remove(1)

for i in a:
  print(i,end=" ")