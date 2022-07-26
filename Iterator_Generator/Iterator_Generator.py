# Iterable - Collections which we can iterate.
# eg. List, Set, String

list1 = [10, 20, 3, 40, 5]

print("list1 = ", list1, "of type is", type(list1))

# Iterate the list iterable
print("Iterating the list iterable")
for i in list1:
    print(i)
print("========================================")
# Iterator - An object which we can create using Iterable type eg. list, set, string
# iterator = iter(list)   --- Creating iterator object using 'iter' keyword
# next(iterator) -- To fetch only one element from the iterator object
try:
    iterator = iter(list1)  # Creating iterator object using 'iter' keyword
    print("type(iterator)=", type(iterator))
    print("next(iterator)=", next(iterator))
    print("next(iterator)=", next(iterator))
    print("next(iterator)=", next(iterator))
    print("next(iterator)=", next(iterator))
    print("next(iterator)=", next(iterator))
    print("next(iterator)=", next(iterator))
except StopIteration:
    print("Interator object is empty")
print("==========================")
print("Iterating iterator object using for loop")
iterator1 = iter(list1)
for i in iterator1:
    print(i)
print("==========================================")


# Generator - Object used to generator iterator object
# Create a function and inside the function we will use yield keyword.

def square(n):
    for i in range(n):
        yield i ** 2


print("square(3)=", square(3), "of type =", type(square(3)))

for i in square(3):
    print(i)

'''
# Notes
1. To create iterator, we use iter() and to create generator, we use function along with yield keyword.
2. Generator uses the yield keyword. It save local variables
3. Python iterator is much more memory efficient.
'''

import collections
import types

print("issubclass(types.GeneratorType, collections.Iterator)=", issubclass(types.GeneratorType, collections.Iterator))
