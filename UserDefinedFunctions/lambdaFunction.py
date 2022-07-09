# Lambda functions - nameless/ anonymus/ one line function
"""
Syntax:
    lambda arguments: expression/condition
"""
print("Normal User defined Function to perform cube operation")
def cube(num):
    return num ** 3

c = cube(4)
print("c = cube(4)")
print("Cube of 4 = ", c)
print("=======================")

print("Lambda Function to perform cube operation")

cubeLambda = lambda num : num ** 3
print("cubeLambda = lambda num : num ** 3")
print("cubeLambda(5)")
print("Cube of 5 = ",cubeLambda(5))

print("===========================")

print("Function will tell greater number - Normal approach")
def getBiggerNum(num1, num2):
    if num1 > num2 :
        return num1
    else:
        return num2

print("getBiggerNum(33, 55)")
print("Greater number between 33 and 55 =", getBiggerNum(33, 55))
print("===========================")

print("Function will tell greater number - Lambda approach")
findBiggerNum = lambda num1, num2 : num1 if num1 > num2 else num2
print("findBiggerNum(33, 55)")
print("Greater number between 33 and 55 =", findBiggerNum(33, 55))










