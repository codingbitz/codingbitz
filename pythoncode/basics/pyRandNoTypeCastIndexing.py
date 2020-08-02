#Python Random Number
import random
print(random.randrange(1,5))


#Python TypeCasting
x = int(1)
print(x, type(x))

#PythonIndexing

a = "Hello, World!"
print(a)
print("Get 1st idx value of the string: ",a[1])

#Slicing

print("Get 1-2 idx values of the string: ",a[1:3])
print("Get 1-Last idx values of the string: ",a[1:])
print("Get 0-5 idx values of the string: ",a[:6])
print("Get last -2,-3  idx values of the string: ",a[-3:-1])
print("lenth of the string: ",len(a))
print("strip white characters in front/back of the string:","before:",len(" Hello World "),"after:", len(" Hello World ".strip()))
print("lower: " ,a.lower(),"upper: ",a.upper(),"replace: ",a.replace("ello","ola"),"split: ",a.split(","))


a="hola, python is good"
x = "ola" in a
y = "ole" not in a
print("check if string is present:",x)
print("check if string is not present:",x)
print("string concat: ","python","is good")

age=5
txt="his age is {}"
print(txt.format(age))

#Using index for format

qty = 3
ino = 567
price = 12
myordr = "I want to pay {2} rupees for {0} pieces of item {1}."
print(myordr.format(qty, ino, price))