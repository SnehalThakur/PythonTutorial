# Map function - will apply logic to each and every element of the list
"""
Syntax:
    map(lambda expression, list)
"""
list1 = [1,2,3,4,5,6,7,8,9,10]
print("list1 = [1,2,3,4,5,6,7,8,9,10]")
print("Original list")
for mul in list1:
    print(mul)
print("----------------------")

print("Map function")
multiplication = map(lambda a: a* 2, list1)

print("multiplication = map(lambda a: a* 2, list1)")

print("New list multiplication")
for mul in multiplication:
    print(mul)
print("==========================")

# Filter function - filter the values that satifies the condition
"""
Syntax:
    filter (lambda expression, list)
"""
print("Filter function to filter all even number")

filteredEvenValues = filter(lambda a: a%2==0, list1)

print("filteredEvenValues = filter(lambda a: a%2==0, list1)")

for val in filteredEvenValues:
    print(val)
print("---------------------")

print("Filter function to filter all odd number")
filteredOddValues = filter(lambda a: a%2!=0, list1)
print("filteredOddValues = filter(lambda a: a%2!=0, list1)")
for val in filteredOddValues:
    print(val)
print("=============================")
# Reduce function
"""
Syntax:
    reduce (lambda expression, list)
"""
from functools import reduce
list2 = [10, 20, 30, 40, 50]
print("Reduce function to reduce all numbers to one number")

reduceSum = reduce(lambda a, b : a + b, list2)
print("reduceSum = reduce(lambda a, b : a + b, list2)")
print("reduceSum =", reduceSum)
print("============================")
# Summation of all elements in the list
sum = 0
for l in list2:
    sum+=l
print("Sum of list = ", sum)











