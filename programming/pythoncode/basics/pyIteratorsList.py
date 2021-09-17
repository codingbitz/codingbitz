#Iterating List
#Method 1 - using normal iterator

mylist =["apple","banana","strawberry"]

for i in mylist:
  print(i)
  
#Method 2 - Using Range
for i in range(len(mylist)):
  print(mylist[i])
  
#Method 3 - While Loop
i=0
while i < len(mylist):
  print(mylist[i])
  i+=1
  
#Method 4 - Comprehension
mylist_1 =["apple","banana","strawberry"]
[print(i) for i in mylist_1]

#Method 5  - Enumerate
for i,val in enumerate(mylist):
  print(i,",",val)
  
#Iterate over multiple lists

fruit =["apple","orange","peaches"]
veggie =["potato","onion"]

import itertools

for (f,v) in zip(fruit,veggie):
  print ("zip",f,v)

for (f,v) in itertools.zip_longest(fruit,veggie,fillvalue="NoValue"):
  print("zip_longest",f,v)
  
#Iterate tuple list of list
import itertools

fruit =[[("banana"),("orange")],[("apple"),("peaches")]]
print("initial list: ",fruit)

final_fruits_compr = [item for t in fruit for item in t]
final_fruits_itertools = list(itertools.chain(*fruit))
final_fruits_lambda = list(filter(lambda x : x,itertools.chain(*itertools.zip_longest(*fruit))))

print("final list - compre:",final_fruits_compr,
      '\n'"final list - itertools:",final_fruits_itertools,
      '\n'"final list - lambda:",final_fruits_lambda )

final_fruits_iter =[]

for t in fruit:
  for item in t:
    final_fruits_iter.append(item)
print("final list - iter:",final_fruits_iter)

#convert numbers to list of integers

i= 2019
comp_j =[int(j) for j in str(i)] # Using COmprehension
map_j = list(map(int,str(i))) #Using Map
print(comp_j)
print(map_j)


#Convert tuple list into list

fruit =[("banana","orange"),("apple","peaches")]
fruit_lst = list(sum(fruit,()))
print("using sum:",fruit_lst) # costly operation

#Using Operator
import operator
from functools import reduce
fruit_red = list(reduce(operator.concat,fruit))
print("fruit_red: ",fruit_red)

#Using Lambda

fruit_lambda_fil = list(filter(lambda x : x,itertools.chain(*itertools.zip_longest(*fruit))))
fruit_lambda_map =reduce(lambda x,y: x+y,map(list,fruit))
print("fruit_lambda_fil: ",fruit_lambda_fil)
print("fruit_lambda_map: ",fruit_lambda_map)