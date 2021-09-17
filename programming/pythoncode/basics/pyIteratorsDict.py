#Iterate Dict

swift ={"oem":"maruti","price":"519000"}
print(swift)

from collections import OrderedDict
swift_order =OrderedDict(swift)

for feature_desc,feature_value in swift_order.items():
  print(feature_desc,":",feature_value)

# Iterate through value lists dictionary

test_dict = {'python' : [1, 2], 'is' : [4, 5], 'gud' : [7, 8]}
print(test_dict)
res =[[i for i in test_dict[x]] for x in  test_dict.keys()]
print(str(res))

#Using from_iterable() + product() + items()
res =[]
for k,v in (itertools.chain.from_iterable([itertools.product((k,),v) for k,v in test_dict.items()])):
  res.append(v)
print(res)

#another implementation
res2 = []
for value in test_dict.values():
  for val in value:
    res2.append(val)
print(res2)

test_dict = {'python' : [1, 2], 'is' : [4, 5], 'gud' : [7, 8]}
print(test_dict)

res1 =[]
for k in test_dict:
  for x in test_dict[k]:
    res1.append(x)
print(res1)