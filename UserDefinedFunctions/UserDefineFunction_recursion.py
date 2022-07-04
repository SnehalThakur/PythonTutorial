# Recursion -  Function calling function (Function calling itself again and again)
"""
Syntax-
    def func():
        func()
"""
def factorial(num):
    """
    This function will perform the factorial of any number
    """
    if num==0:
        return 1
    else:
        return num*factorial(num-1)


result = factorial(3)
print("Factorial of given number i.e 3 is", result)
result = factorial(5)
print("Factorial of given number i.e 5 is", result)
