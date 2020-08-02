a = 10;b = 5

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  if 5 > 2:
      print("Five is greater than two!")

#Functions can return bool:

def myFunc():
    return True
if myFunc():
    print("YES")
else:
    print("NO")

#To check for the datatype of the passed value
x = 200
print(isinstance(x, int))