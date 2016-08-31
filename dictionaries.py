#dictionaries = unorderded data : colection of {'keys':values}
#unique keys!

exDictionary = {'Jack':15,'Bob':22,'Alice':12,'Kevin':17}
exDictionary2 = {'Jack':[15,'blonde'],'Bob':[22,'brown'],'Alice':[12,'black'],'Kevin':[17,'red']}

######
print(exDictionary)
print(exDictionary['Jack'])

exDictionary['Tim'] = 14
print(exDictionary)

exDictionary['Tim'] = 15 # key should be unique
print(exDictionary)

del exDictionary['Tim'] # removes the key:value
print(exDictionary)

######
print(exDictionary2)
print(exDictionary2['Jack'])
print(exDictionary2['Jack'][1])-