a = 5
b = "name"
print(a)
print(b)

# assign to multiple variables
x,y,z = "apple","banana","figs"
print("print fruit names:",x,y,z)

#output variables
x='python'
print(x,"is programming language")
y = x+' is'
print(y,"programming language")

#global variables
x=5
def myfunc():
    print("i got",x,"apples")
myfunc()

x=5
def myfunc():
    x = 4
    print("i got",x,"apples")
myfunc()

def myfunc():
    global x
    x = 4
myfunc()
print("Output based on global word:","i got",x,"apples")