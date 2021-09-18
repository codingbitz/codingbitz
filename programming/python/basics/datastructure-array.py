
# Array datastructure

exp =[2200,2350,2600,2130.2190]
print(type(exp)) # <class 'list'>
# #  In Feb, how many dollars you spent extra compare to January?
print("compared to jan i spent "+ str(exp[1] - exp[0]) + " in feb") #compared to jan i spent 150 in feb

# # Find out your total expense in first quarter (first three months) of the year.
print("total expenses for 1st 3 months "+ str(sum(exp[:3]))) # total expenses for 1st 3 months 7150
# # Find out if you spent exactly 2000 dollars in any month
if exp == 2000:
  print("on some month 2000 was spent")
else:
  print("2000 exactly wasn't spent on any month")
# # June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.insert(5,1980)
print(exp) # [2200, 2350, 2600, 2130.219, 1980]

# # You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
exp[1] = exp[1]-200
print(exp)


#You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

# #Length of the list
print("lenth of list: "+str(len(heros)))

# Add 'black panther' at the end of this list
heros.insert(5,'black panther')
print(heros)

# #You realize that you need to add 'black panther' after 'hulk',   so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)

# Now you don't like thor and hulk because they get angry easily :)  So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)
## Sort the heros list in alphabetical order 
heros.sort()
print(heros)

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_no = int(input("max input no: "))
odd_no =[]

for nos in range(max):
  if nos%2 == 1:
    odd_no.append(nos)

print("odd number list : ", odd_no)

from operator import itemgetter
aapl_stk_price = [100,101,103,104,105]

# price on day 1 & day 3
x = int(input("enter 1st day:"))-1
y = int(input("enter 2nd day:"))-1

print([aapl_stk_price[i] for i in (x, y)])
print(itemgetter(x,y)(aapl_stk_price)) # BigO =o(n) Using itemgetter
print(list(map(aapl_stk_price.__getitem__, (x,y)))) # using map

# what day price was 104
for i in range(len(aapl_stk_price)):
  if aapl_stk_price[i] == 104:
    print(i) # BigO =o(n)
# print all prices

for i in aapl_stk_price:
  print(i)  # BigO =o(n)

# insert
aapl_stk_price.insert(1,99)
print(aapl_stk_price)   # BigO =o(n)

# delete
aapl_stk_price.remove(99)
print(aapl_stk_price)   # BigO =o(n)

# Dynamic Array vs Static Array, geometric progression
