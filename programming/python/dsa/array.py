import array

# initializes array with signed integers
arr = array.array('i', [1, 2, 3])

# printing array
print ("array is : ",end=" ")
for i in range (0, 3):
	print (arr[i], end=" ")

print("\r")

# using append()
arr.append(4);

# printing array
print("The appended array is : ", end="")
for i in range (0, 4):
	print (arr[i], end=" ")
	
# using insert()
arr.insert(2, 5)

print("\r")

# printing array
print ("Insert: ", end="")
for i in range (0, 5):
	print (arr[i], end=" ")

# Using Pop
print (arr.pop(2));
print ("Pop : ",end="")
for i in range (0,4):
    print (arr[i],end=" ")
 
print("\r")

# Using Remove
print (arr.remove(1));
print ("Remove : ",end="")
for i in range (0,3):
    print (arr[i],end=" ")
 
print("\r")

# Using Index
print (arr.index(2))

# Using Reverse

arr.reverse()
print ("Reverse : ",end="")
for i in range (0,3):
    print (arr[i],end=" ")
 
print("\r")