#ASSIGNMENT OPERATORS
a =3
b="How is Python"
c="Python is Good"


print("value assigned to a: ",a)
a+=3
print("new value of a: ",a)
a-=2
print("new value of a: ",a)
a**=2
print("new value of a: ",a)

#Identity Operator
print(b is not c)
print(b is c)

#Membership Operator
print("H" in b)
print("Y" not in c )

# LOGICAL OPERATORS

print("check for AND operator:" ,a>5 and b>5)
print("check for OR operator:" ,a>2 or b>2)
print("check for NOT operator:" ,not(a>5 and b>5)) # reverse the result


#RELATIONAL OPERATORS

print ("check if a is greater than b: ",str(a>b))
print ("check if a is lesser than b: ",str(a<b))
print("check if a equals b:",str(a==b))
print("check if a not equals b:",str(a!=b))
print("check if a greater than or equals b:",str(a>=b))
print("check if a lesser than or equals b:",str(a<=b))

#ARITHMETIC OPERATORS

print("addition: ",str(a+b))
print("subtraction: ",str(a-b))
print("multiplication: ",str(a*b))
print("division: ",str(a/b))
print("modulo: ", str(a%b))