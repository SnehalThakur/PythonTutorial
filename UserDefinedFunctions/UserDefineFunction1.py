# Calculator function

"""
Syntax-
 def functionName(argument/s):
     '''Doc String'''
     statements (logic)
     retun value
"""

# Calculator
print("Hey There!! This is basic calculator for addition, subtraction, multiplication, division, modulus, exponential operations")

# Get three arguments from the user i.e num1, num2, operator
numberInput1 = int(input("Enter 1st number: ")) # typecasting number1 string type to int type
numberInput2 = int(input("Enter 2nd number: ")) # typecasting number2 string type to int type
operation = input("Which operation you want to perform? (+ , - , / , * , % , **): ")

def calculator(num1, num2, operation):
    """
    This Calculator performs basic operations like + , - , / , * , % , ** 
    """
    if operation == "+": # Addition operation
        summation = num1 + num2
        return summation
    
    elif operation == "-":  # Subtraction operation
        difference = num1 - num2
        return difference
    
    elif operation == "*":  # Multiplication operation
        multiplication = num1 * num2
        return multiplication
    
    elif operation == "/": # Division operation
        division = num1 / num2
        return division
    
    elif operation == "%": # Mod operation
        modulus = num1 % num2
        return modulus
    
    elif operation == "**": # Exponent (power) operation
        power = num1 ** num2
        return power

print("result = calculator(numberInput1, numberInput2, operation)")
result = calculator(numberInput1, numberInput2, operation)
print("Result of \'",operation, "\' operation of two numbers i.e number1=",numberInput1,
      "and number2=", numberInput2,"is", result)


        
        
    
    
