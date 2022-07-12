# Exception handling

input1 = input("Enter first number: ")
input2 = input("Enter second number: ")
try:
    result = int(input1) / int(input2)
    file = open("file.txt")
    print(file)

except ZeroDivisionError as ze:     # catch ZeroDivisionError
    print("Exception occured of type", type(ze), "and message is", ze)
    print("Don't enter zero value")
    result = None
    
except ValueError as ve:            # catch ValueError
    print("Exception occured of type", type(ve), "and message is", ve)
    print("Enter only digits/numbers, not string/char")
    result = None

except FileNotFoundError as fe:     # catch FileNotFoundError
    print("Exception occured of type", type(fe), "and message is", fe)
    print("File is not present. Please give the correct path.")
    result = None

except Exception as e:              # catch All other Exception
    print("Exception occured of type", type(e), "and message is", e)
    result = None
   
print("result=",result)

