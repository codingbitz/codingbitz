#Accessing private variable
class A:
  
  __amount = 45
  def __info(self):
    print("I am in Class A")

  def hello(self):
    print("Amount is ",A.__amount)
a = A()
a.hello()
a._A__info()
a._A__amount
#HowNotToAccess
class Person:

  def __init__(self):
    self.first_name = 'Random'
    self.__last_name ='Guy'
  
  def PrintName(self):
    return self.first_name + self.__last_name
P = Person()

print(P.first_name)
print(P.PrintName())
print(P.__last_name)

#HowToAccess

class Person:

  def __init__(self):
    self.first_name = 'Random'
    self.__last_name ='Guy'
  
  def PrintName(self):
    return self.first_name + self.__last_name
P = Person()

print(P.first_name)
print(P.PrintName())
print(P._Person__last_name)



#OneMoreExample - Encapsulation

#Public
class Modifiers:
    def __init__(self,name):
        self.public_member = name

mod = Modifiers("PUBLIC_GUY")
print(mod.public_member)
mod.public_member = "NONPUBLIC_GUY"
print(mod.public_member)

#Protected
class Modifiers:
    def __init__(self,name):
        self._protected_member = name

mod = Modifiers("PROTECTED_GUY")
print(mod._protected_member)
mod._protected_member = "NONPROTECTED_GUY"
print(mod._protected_member)

#Private
class Modifiers:
    def __init__(self,name):
        self.__private_member = name

mod = Modifiers("PRIVATE_GUY")
print(mod._Modifiers__private_member)
mod._Modifiers__private_member = "NONPRIVATE_GUY"
print(mod._Modifiers__private_member)