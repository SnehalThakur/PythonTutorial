# User defined Function - Swap 2 numbers
"""
Syntax-

def functionName(args):
    '''Doc String'''
    funcation statements/ logic
    return value

input-
a = 10
b = 20

output-
a =20
b = 10

logic-
temp = a
a = b
b = temp
"""
# Function Defination
def swapNumberUsingThirdVariable(number1, number2):
    """
    This function will take 2 inputs and it will swap
    the values using third variable
    """
    print("Before Swapping","number1=",number1,"number2=",number2)
    temp = number1
    number1 = number2
    number2 = temp
    print("After Swapping","number1=",number1,"number2=",number2)

# Function Call
print("swapNumberUsingThirdVariable(10, 20)")
swapNumberUsingThirdVariable(10, 20)
print('-----------------------------')
print("swapNumberUsingThirdVariable(50, 100)")
swapNumberUsingThirdVariable(50, 100)
print("=============================")

# Logic to swap numbers without using 3rd variable
"""
STEP 1: START.
STEP 2: ENTER x, y.
STEP 3: PRINT x, y.
STEP 4: x = x + y.
STEP 5: y= x - y.
STEP 6: x =x - y.
STEP 7: PRINT x, y.
STEP 8: END.
"""

def swapNumberWithoutThirdVariable(x, y):
    """
    This function will take 2 inputs and it will swap
    the values without using third variable
    """
    print("Before Swapping","number1=",x,"number2=",y)
    x = x + y
    y = x - y
    x = x - y
    print("After Swapping","number1=",x,"number2=",y)

# Function Call
print("swapNumberWithoutThirdVariable(10, 20)")
swapNumberWithoutThirdVariable(10, 20)
print("--------------------------")
print("swapNumberWithoutThirdVariable(1000, 5000)")
swapNumberWithoutThirdVariable(1000, 5000)
print("=====================================")

