# Tuple
a = (10, "Python", True, True, False)
print("a=",a,", type(a)=",type(a), ", len(a)=",len(a))
print("==================")
# Method 1. Tuple.index({element}) - it will return index position of an element
print("Method 1. Tuple.index({element}) - it will return index position of an element")
print("a.index(False)=",a.index(False))
print("a.index(10)=",a.index(10))
print("a.index(True)=",a.index(True))
print("a.index('Python')=",a.index("Python"))
print("==================")
# Method 2. Tuple.count({element}) - It return the number of occurance of an element
print("Method 2. Tuple.count({element}) - It return the number of occurance of an element")
print("a.count(True)=",a.count(True))
print("a.count(False)=",a.count(False))
print("a.count(10)=",a.count(10))
