#IterCheck
class IterTest:

    # Define Constructor
    def __init__(self,limit):
      self.limit =limit
    
    # Iterator
    def __iter__(self):
      self.x =10
      return self
    
    def __next__(self):
      x =self.x

      if x> self.limit:
        raise StopIteration

      else:
       self.x =x+2
       return x
for i in IterTest(15):
  print(i)
  
#Iterate using While Loop & raise exception

mylist_iterable =["apple","banana","strawberry"]
mylist_iter_obj = iter(mylist_iterable)

#Iterate list using While loop

while True:
  try:
    i = next(mylist_iter_obj)
    print(i)
  except StopIteration:
    print("I'm done, no more fruits in mylist_iterable")
    break
    
# to check if object is iterable or not
mynew_iterbale = [['list','tuple','dict'],('list','tuple','dict'),{'list','tuple','dict'},"list_tuple_dict",314,3.14]
def iter_check(obj):
  try:
    iter(obj)
    return True
  except  TypeError:
    return False

for elem in mynew_iterbale:
  print(elem, "is iterable",iter_check(elem))
  
#Iterate over characters in string

#Iterare over characters in word

word ="dog"
for alphabets in word:
  print("option1:", alphabets)

for alphabets in range(0,len(word)):
  print("option2:", word[alphabets])
for i,v in enumerate(word):
  print(i,':',v)
for alphabets in reversed(range(0,len(word))):
  print(word[alphabets])
# reverse the list & append character in said index  
no =[1,4,7,0]
inv_no = no[::-1]
for i, item in enumerate(inv_no):
    if item ==0:
        inv_no[i] += 100
        break
print(inv_no)

#Iterating over string

#Iterate over words of a String in Python

#Using split()

pygud_opt1 ="Python is a good programming language"
pygud_split =pygud_opt1.split()

for word in pygud_split:
  print("words in pygud: ",word)


#using re.findall
import re
pygud_opt2 ="Python is a good programming language"
pygud_findall =re.findall(r'\w+',pygud_opt2)

for word in pygud_findall:
  print(word)