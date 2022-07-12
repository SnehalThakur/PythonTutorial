# Custom Exception - "raise"


'''
Age Problem which expects age greater than 18
'''
age = int(input("Enter the age of the person"))
try:
    if age<18:
        raise ValueError("Age should be greater than 18")
    else:
        print("You are Matured!!!")
finally:
    print("This is finally block!")
