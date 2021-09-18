print("hello".capitalize()) # Output: Hello
print("Hello".casefold())# Output: hello
print("Hello".center(20)) # O/P:        Hello
print("hello".count("l")) # O/P:2
print("hello".encode()) # O/P:b'hello'
print("hello".endswith("o")) # O/P:True
print("hello".find('e')) # O/P:1
print("hello".index('l'))
print("hello".islower())
print("hello".upper())

a=("apple","orange","pineapple")
x="/".join(a)
print(x)

a="apple is good.\npineapple is good"
print(a.splitlines())

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)