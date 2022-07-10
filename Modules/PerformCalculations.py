import Calculator

print("To perform calculation, you will have to Enter two numbers")
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

# Summation operation
summation = Calculator.sum(num1, num2)
print("Summation of num1=",num1,"and num2=", num2,"is",summation)

# Difference operation
Difference = Calculator.difference(num1, num2)
print("Difference of num1=",num1,"and num2=", num2,"is",Difference)

# Multiply operation
multiplication = Calculator.multiply(num1, num2)
print("multiplication of num1=",num1,"and num2=", num2,"is",multiplication)

# Divide Operation
division = Calculator.divide(num1, num2)
print("division of num1=",num1,"and num2=", num2,"is",division)

# Mod Operation
modulus = Calculator.mod(num1, num2)
print("modulus of num1=",num1,"and num2=", num2,"is",modulus)
