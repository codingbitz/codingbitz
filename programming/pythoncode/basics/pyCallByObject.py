#Python is call by object

#Call by Value

string = "orange"
def test(string): 
      
    string = "apple"
    print("call by value","Inside Function:", string) 
test(string) 
print("call by value","Outside Function:", string) 


#Call by Reference

def add_more(list): 
    list.append(50) 
    print("call by ref","Inside Function", list) 
  
mylist = [10,20,30,40] 
add_more(mylist) 
print("call by ref","Outside Function:", mylist)

#Binding Names to Objects
a="hi";b="hi"
print(id(a))
print(id(b))
print(a is b)
c=[1,2]
d=[1,2]
print(id(c))
print(id(d))
print(c is d)