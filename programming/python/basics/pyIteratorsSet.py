#Iterate set

word = "cat"
word_set =set(word)

for w in word_set:
  print(w)
  
for k,v in enumerate(word_set):
  print("enumerate:",k,v)
  
#Iterating over a set as indexed list.
word_list =list(word_set)

for i in range(len(word_list)):
  print("indexList",word_list[i])
  
#comprehension
word_comp =[print("compre: ",val) for val in word_set]

#Using Map,Lambda
word_set = set(word)
print("lamb",'\n'.join(map(lambda x: x, word_set)))

listOfLambdas = map(lambda i: i,word_set)
for f in listOfLambdas:
    print("lambForLoop",f)
    
#Iter
for f in iter(word_set):
    print("iter",f)
    
# Using WHile Loop
iter_gen = iter(word_set) 

while True:
  try:
    print("whileLoop",next(iter_gen))
  except StopIteration:
    break