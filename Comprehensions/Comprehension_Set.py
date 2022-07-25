# Set Comprehension
# Create a set which contains Square of all elements present in set
set1 = {2, 3, 4, 5, 6, 7, 8, 9}
squareSet = set()
for i in set1:
    squareSet.add(i**2)
print("squareSet =", squareSet)
print("==============================")
# Using Set Comprehension
squareSet1 = {out**2 for out in set1}
print("squareSet1=", squareSet1)
