list1 = [10, 20, 60 ,30, 70, 40, 20, 50, 70, 60]
set1 = {10, 20, 60 ,30, 20, 40}
set2 = {70, 40, 20, 50}
set3 = {}
print("list1 =",list1,"len(list1)=",len(list1),"type(list1)=",type(list1))
print("set1 =",set1,"len(set1)=",len(set1),"type(set1)=",type(set1))
print("set2 =",set2,"len(set2)=",len(set2),"type(set2)=",type(set2))
list1 = set(list1) # converting list to set to get only unique elements 
print("list1 = set(list1)")
print("list1 =",list1,"len(list1)=",len(list1),"type(list1)=",type(list1))
list1 = list(list1) # converting set back to list
print("list1 = list(list1)")
print("list1 =",list1,"len(list1)=",len(list1),"type(list1)=",type(list1))
print("=========================")
# Method 1 set.add({element}) - To add element to the set
print("Method 1. set.add({element}) - To add element to the set")
set2.add(100)
print("set2.add(100)")
print("set2=",set2,"len(set2)=",len(set2),"type(set2)=",type(set2))
print("=========================")
# Method 2. set.pop() -  To remove element from the set
print("Method 2. set.pop() -  To remove element from the set")
set2.pop()
print("set2.pop()")
print("set2=",set2)
print("=========================")
# Method 3. set.discard({element}) - To remove element from the set
print("Method 3. set.discard({element}) - To remove element from the set")
set2.discard(40)
set2.discard(60)
print("set2.discard(40)")
print("set2.discard(60)")
print("set2=",set2)
print("=========================")
# Method 4. set.remove() - TO remove element from the set
print("Method 4. set.remove() - TO remove element from the set")
set2.remove(50)
print("set2.remove(50)")
# set2.remove(60)
#print("set2.remove(60)")
print("set2=",set2)
print("=========================")
a = {10,20,30,40,50}
b= {30,40,50,60,70}
c = {60,70,80,90,100}
print('a =',a, ", len(a)=",len(a))
print('b =',b, ", len(b)=",len(b))
# Method 5. set1.update(set2) - To update the set
print("Method 5. set1.update(set2) - To update the set")
a.update(b)
print("a.update(b)")
print('set a after update=',a, ", len(a)=",len(a))
print("=========================")
# Method 6. set1.issuperset(set2) - To check whether set contains another set
print("Method 6. set1.issuperset(set2) - To check whether set contains another set")
print('a.issuperset(b) =',a.issuperset(b))
print('b.issuperset(a) =',b.issuperset(a))
print("=========================")
# Method 7. set1.issubset(set2) -  To check whether another set contains this set
print("Method 7. set1.issubset(set2) -  To check whether another set contains this set")
print('a.issubset(b) =',a.issubset(b))
print('b.issubset(a) =',b.issubset(a))
print('==============================')
print('==============================')
# Method 8. set1.union(set2) or set1|set2 -  return all elements from both sets
print("Method 8. set1.union(set2) or set1|set2 - return all elements")
print("b = ",b)
print("c = ",c)
print('b|c =',b|c)
print('b.union(c) =',b.union(c))
print('==============================')
# Method 9. set1.intersection(set2) or set1&set2 - return only common elements from both sets
print("Method 9. set1.intersection(set2) or set1&set2 - return only common elements from both sets")
print("b = ",b)
print("c = ",c)
print('b&c =',b&c)
print('b.intersection(c) =',b.intersection(c))
print('==============================')
# Method 10. set1.difference(set2) or set1-set2
print("Method 10. set1.difference(set2) or set1-set2")
print("b = ",b)
print("c = ",c)
print('b-c =',b-c) # b-c = {40, 50, 30}
print('b.difference(c) =',b.difference(c))  # b.difference(c) = {40, 50, 30}
print('c-b =',c-b)      # {80, 90, 100}
print('c.difference(b) =',c.difference(b))
print('==============================')
# Method 11. set1.symmetric_difference(set2) or set1^set2
print("b = ",b)
print("c = ",c)
print('b^c =',b^c)      # {100, 40, 80, 50, 90, 30}
print('b.symmetric_difference(c) =',b.symmetric_difference(c))



