# List Comprehension
# Create new list with all odd numbers

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddNumbersList = []
for i in list1:
    if i % 2 !=0:
        oddNumbersList.append(i)

print("List of all odd numbers = ", oddNumbersList)
print("=====================================")

# Using list comprehension
'''
Syntax:
[ output  for element in actual_sequence  if (condition) ]
'''
oddNumbersList1 = [out for out in list1 if out % 2 != 0 if out < 5]
print("List of all odd numbers using List comprehension = ", oddNumbersList1)

evenNumbersList1 = [out for out in list1 if out % 2 == 0]
print("List of all even numbers using List comprehension = ", evenNumbersList1)