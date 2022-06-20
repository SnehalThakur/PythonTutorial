# Dictionary - {key (should be unique): value} - Collection of key and value pair
dict1 = {1 : "Python", 2 : "Statistics", "ML": ["Linear Regression", "Logistics Regression", "Decision Tree"]}
dict2 = {1: 100, 2: 200, 3 : 300, 4: 400, 5: 500}
dict3 = {}
print("dict1=",dict1,", type(dict1)=", type(dict1), ", len(dict1)=", len(dict1))
print("dict2=",dict2,", type(dict2)=", type(dict2), ", len(dict2)=", len(dict2))
print("========================")
# Fetch any value with respect to key from any dictionary - dict[key]
print("Fetch any value with respect to key from any dictionary - dict[key]")
print("dict1[1] = ",dict1[1])
print("dict1[2] = ",dict1[2])
print("dict1['ML'] = ",dict1["ML"])
print("========================")
# Add key, value pair to the dictionary - dict[key]= value
print("Add key, value pair to the dictionary - dict[key]= value")
dict1[3]= "DL"
print("dict1=", dict1,", len(dict1)=", len(dict1))
print("=========================")
# Method 1. dict.get(key) - To get the value w.r.t key
print("Method 1. dict.get(key) - To get th value w.r.t key")
print("dict1.get(3)=",dict1.get(3))
print("dict1.get(4)=",dict1.get(4))
print("=========================")
# Method 2. dict.keys() - TO get all keys present in the dictionary
print("Method 2. dict.keys() - TO get all keys present in the dictionary")
print("dict1.keys()=",dict1.keys())
print("=========================")
# Method 3. dict.values() - To get all values present in the dictionary
print("Method 3. dict.values() - To get all values present in the dictionary")
print("dict1.values()=",dict1.values())
print("=========================")
# Method 4. dict1.update(dict2) - TO add another dict to original dictionary
print("dict1=",dict1, ", len(dict1)=", len(dict1))
print("dict2=",dict2, ", len(dict2)=", len(dict2))
dict1.update(dict2)
print("dict1 after dict1.update(dict2)=",dict1)
print("=========================")
# Add element to the dictionary - dict[key]= value
print("dict3 = ", dict3)
dict3["Course"]="Python"
dict3["Duration"]="2months"
dict3["Version"]="3.9.1"
print("dict3 after adding key,value pairs= ", dict3)
print("==========================")
# To convert list to dictionary dict4 = dict(list[(key, value),(key, value)])
list4 = [(1,10.5),(2,50.5),(3,60.2)]
print("list4=",list4,"type(list4)=",type(list4), "len(list4)=",len(list4))
dict4 = dict(list4)
print("dict4 = dict(list4)")
print("dict4=",dict4,"type(dict4)=",type(dict4), "len(dict4)=",len(dict4))
print("===========================")
# dict.pop(key) - To remove any key-value pair w.r.t key
print("dict.pop(key) - To remove any key-value pair w.r.t key")
print("dict1=",dict1)
dict1.pop("ML")
print("dict1.pop('ML')")
print("dict1=",dict1)
print("===========================")
# dict.popitem() -  TO remove last key-value pair
print("dict.popitem() -  TO remove last key-value pair")
print("dict1=",dict1)
print("dict1.popitem()=",dict1.popitem())
print("dict1=",dict1)
print("===========================")
# dict.fromkeys(keys, value) key = ( key1 , key2, key3) - TO create new dictionary with key list and value
print("dict.fromkeys(keys, value) key = ( key1 , key2, key3) - TO create new dictionary with key list and value")
dict5 = {}
dict6 = {}
dict7 = {}
keys= ['a','b','c','d']
value1 = [100, 200, 300, 400]
value2 = 100
print("keys=",keys)
print("value1=",value1)
print("value2=",value2)
print("dict5=",dict5)
dict5 = dict5.fromkeys(keys)
print("dict5.fromkeys(keys)")
print("dict5=",dict5)
print("dict6=",dict6)
dict6 = dict6.fromkeys(keys, value2)
print("dict6.fromkeys(keys, value2)")
print("dict6=",dict6)
print("dict7=",dict7)
dict7 = dict7.fromkeys(keys, value1)
print("dict7.fromkeys(keys, value1)")
print("dict7=",dict7)
print("===========================")
# dict.items() -  To return all key-value pairs
print("dict.items() -  To return all key-value pairs")
print("dict1=",dict1)
print("dict1.items()=",dict1.items())
print("===========================")
# dict.setdefault(keyname, value) - To set default value in the dictionary, it will create new key-value pair if not present in dict
print("dict.setdefault(keyname, value) - To set default value in the dictionary, it will create new key-value pair if not present in dict")
print("dict1=",dict1)
print("dict1.setdefault(5, 500)=",dict1.setdefault(5, 500))
print("dict1=",dict1)
print("dict[5]=",dict1[5])
print("dict1.setdefault(4, 4)=",dict1.setdefault(4, 4))
print("dict[4]=",dict1[4])
print("==========================")
# dict.copy() - TO copy dict (key-value pairs) to new dict
print("dict.copy() - TO copy dict (key-value pairs) to new dict")
dict8 = dict3.copy()
print("dict3=",dict3)
print("dict8 = dict3.copy()")
print("dict8=",dict8)
print("==========================")
# dict.clear() -  TO remove all elements from the dictionary
print("dict.clear() -  TO remove all elements from the dictionary")
dict8.clear()
print("dict8.clear()")
print("dict8=",dict8)






    

    
