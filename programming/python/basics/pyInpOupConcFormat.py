#Python Input

#Using Input Function
num = input('Enter a number: ')
print(num)

#Input Function in Loop

while True:
    data = input("Please enter the message:\n")
    if 'Exit' == data:
        break
    print(f'Processing Message from input() *****{data}*****')

print("Done")

#Using sys.stdin

import sys
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')

print("Exit")

# From Files

import fileinput 

with fileinput.input(files = ('sample_data/california_housing_test.csv', 'sample_data/california_housing_train.csv')) as f: 
	for line in f: 
		print(line)

#Python Output

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')

x = 5
y = 10
print('\nThe value of x is {} and y is {}'.format(x,y))
print('I love {1} and {0}'.format('bread','butter'))

print('Hello {name}, {greeting}'.format(greeting = 'Good Morning', name = 'John'))

#Python Impor

from math import pi
print("value of pi:",pi)
import sys
sys.path

#Python Concatenation

a ="hi,"
b = "how are you?"

#Using + Operator
c = a+b
d='-'
print(c)

#Using Join
print("".join([a,b]))
print(d.join(b))
#using format
print("{} {}".format(a,b))


#Python Formatting

def unorganized(a, b): 
    for i in range (a, b): 
        print ( i, i**2, i**3, i**4 ) 
  
# Function prints the organized set of values 
def organized(a, b): 
    for i in range (a, b): 
  
        print("{:6d} {:6d} {:6d} {:6d}".format(i, i ** 2, i ** 3, i ** 4)) 
  
# Input
n1 = int(input("Enter lower range :-\n")) 
n2 = int(input("Enter upper range :-\n")) 
  
print("------Before Using Formatters-------") 
  
unorganized(n1, n2) 
  
print() 
print("-------After Using Formatters---------") 
print() 
  
organized(n1, n2)

# Error

my_string = "{}, is a {} {} for daily consumption but take only {}"
  
print (my_string.format("Apple", "good", "fruit")) 

IndexError                                Traceback (most recent call last)
<ipython-input-8-0172d1fccb80> in <module>()
     25 my_string = "{}, is a {} {} for daily consumption but take only {}"
     26 
---> 27 print (my_string.format("Apple", "good", "fruit"))

IndexError: tuple index out of range