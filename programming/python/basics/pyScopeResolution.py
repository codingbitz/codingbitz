 #Python Scope Resolution

#LEGB Scope
# Built-in Scope 
from math import pi 
  
#pi = 'global pi variable' 
  
def outer(): 
    #pi = 'outer pi variable' 
    def inner(): 
        #nonlocal pi
        #pi = 'inner pi variable' 
        print(pi) 
        #print("from enclosed:",pi) 
    inner() 
  
outer()
#print("from global:",pi) 

#Example2
def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)