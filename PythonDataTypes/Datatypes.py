# Single line comment
'''
Multi
line
comment
'''
"""
Multi
line
comment
"""

# Integer Data type
num =10
print('num = ',num)
print('type(num) = ', type(num))

# Float Data type
num1 = 10.5
print("num1 = ",num1)
print("type(num1) = ",type(num1))

# Complex data type
num2 = 10j
print('num2 = ',num2)
print("type(num2) = ",type(num2))

print('======================')
print("Different ways to print any statement")
print("Using Comma ',' operator")
print('num = ',num) # comma operator
print('======================')
print("Using + operator")
print('num = '+str(num)) # + operator
print("Using Comma ',' to concatinate multiple variable")
print('num=',num,', num1=',num1,', num2=',num2)
print('======================')
print("Using .format method")
print('num = {}'.format(num))
print('num= {0} num1= {1} num2= {2}'.format(num,num1,num2))



