mydict = {"brand": "Ford", "model": "Mustang","year": 1964,"color":"red"}
print(mydict,"||length",len(mydict),"||access :",mydict["model"],"||use get: ",mydict.get("model"))

mydict["year"] =2018
print("after changed: ",mydict)

#loop thru dict & print k,v pairs
for i in mydict:
    print(i,":",mydict[i])

for i,j in mydict.items():
    print("using items() method:",i,":",j)

# to check if key exists
if "models" in mydict:
    print("yes, key ''models'' exists in dict")
else:
    print("no, key ''models'' dont exists in dict")

#adding items to dict
mydict["color"] ='red'
print(mydict)

#copy dict
mynewdict = mydict.copy()
mynewdict_1 = dict(mynewdict)
print(mynewdict)
print(mynewdict_1)
#remove items from dict
# #pop
mynewdict.pop("year")
print("pop: ",mynewdict)
#del
del mynewdict_1["year"]
print("using del:",mynewdict_1)


# Nested Dict

swift ={"oem":"maruti","price":"519000"}
triber ={"oem":"renault","price":"499000"}
baleno ={"oem":"maruti","price":"570000"}
kwid ={"oem":"renault","price":"305000"}
altroz ={"oem":"tata","price":"529000"}
tiago ={"oem":"tata","price":"460000"}
elite_i20 ={"oem":"hyundai","price":"650000"}
grand_i10 ={"oem":"hyundai","price":"508000"}

hatchback_india ={"swift":swift,"triber":triber,"baleno":baleno,"kwid":kwid,"altroz":altroz,"tiago":tiago,"elite_i20":elite_i20,"grand_i10":grand_i10}
#print(hatchback_india)

# dict constructor
dict_constr = dict(brand="Ford", model="Mustang", year=1964)
print("from dict constructor:" ,dict_constr)

#Python Docstrings
def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)