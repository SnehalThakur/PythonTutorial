# While loop
'''
Syntax:
    initialize variable
    while (Condition):
        line of statements
        increament variable     
'''
"""
# Create a Counter
counterInputMaxLimit = int(input("Enter maximum limit of the Counter"))
counter = 1
while(counter <= counterInputMaxLimit):
    print("Counter = ", counter)
    counter = counter + 2
    #counter +=1
"""


# Multiplication Table
# 5 x 1 =  5
# |   |    |
# 5 x 10 = 50
number = int(input("Enter the number for which you want multiplication table: "))
counter = 1
print("Multiplication Table of",number)
while(counter <= 10):
    print(number,"x",counter,"=",number * counter)
    counter = counter + 1

