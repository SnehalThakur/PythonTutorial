# For Loop
'''
Syntax:
    for value in values(iterable type):
        print(value)
'''
# Iterating String with for loop
print("Iterating String with for loop")
string1 = "Python"
counter = 1
print("string1=",string1)
for value in string1:
    print("string1 Val=",value,"in iteration",counter)
    counter+=1 # counter = counter + 1
print("====================")
# Iterating tuple with for loop
print("Iterating tuple with for loop")
tuple1 = ("Python","Program")
print("tuple1=",tuple1)
counter = 1
for val in tuple1:
    print("tuple1 Val=",val,"in iteration",counter)
    counter+=1 # counter = counter + 1
print("====================")
# Iterating List with for loop
print("Iterating List with for loop")
list1 = ["Python","ML","DL","Statistics"]
print("list1=",list1)
counter = 1
for val in list1:
    print("list1 Val=",val,"in iteration",counter)
    counter+=1 # counter = counter + 1
print("====================")
# Iterating Dictionary with for loop
print("Iterating Dictionary with for loop")
dict1 = {"Course1": "Python","Course2": "Statistics","Course3":"ML"} 
print("dict1=",dict1)
# We can print elements of the dictionary by 3 ways
# 1. dict[key] -> value
print("Printing Dict elements in multiple ways")
print("1. dict[key] -> value")
counter = 1
for val in dict1:
    print("Key=",val,", Value=",dict1[val],"in iteration",counter)
    counter+=1 # counter = counter + 1
print("----------------")
# 2. dict.get(key) -> value
print("2. dict.get(key) -> value")
counter = 1
for val in dict1:
    print("Key=",val,", Value=",dict1.get(val),"in iteration",counter)
    counter+=1 # counter = counter + 1
print("----------------")
# 3. dict.items() -> key, value
print("3. dict.items() -> key, value")
counter = 1
for key, value in dict1.items():
    print("Key=",key,", Value=",value,"in iteration",counter)
    counter+=1 # counter = counter + 1
print("====================")






