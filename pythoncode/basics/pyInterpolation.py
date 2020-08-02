n1 ="Hello"
n2 = "How are you"
#Option 1:
print("%s, %s?"%(n1,n2))
#Option 2
print("{}, {}?".format(n1,n2))
#Option 3 > f-strings
print(f"{n1}, {n2}?")
#import string template
from string import Template   
n = Template('$n3, $n4?')
print(n.substitute(n3=n1,n4=n2))