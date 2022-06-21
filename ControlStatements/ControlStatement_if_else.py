# if - else
'''
userInput = input("Enter any value- ")
print("userInput=",userInput)
print("type(userInput)=",type(userInput))
print("len(userInput)=",len(userInput))

userInputInt = int(userInput)
print("userInputInt after type casting to int type=",userInputInt)
print("type(userInputInt)=",type(userInputInt))
'''
userAge = input("Enter your age- ")
print("userAge=",userAge)
#print("type(userAge)=",type(userAge))
#print("len(userAge)=",len(userAge))
print("Type casting String to int userAgeInt = int(userAge)")
userAgeInt = int(userAge)
#print("userAgeInt after type casting to int type=",userAgeInt)
#print("type(userAgeInt)=",type(userAgeInt))

'''
Syntax
if {Condition}:
    line of statement1
    line of statement2
    line of statement3
elif {condition}:
    line of statement1
else:
    line of statement1
'''
if userAgeInt >= 18:
    print("Congrats!! You are Eligible for Driving Licence")
elif userAgeInt < 18 and userAgeInt >= 16:
    print("You can only obtain a license for driving two-wheelers with an engine capacity of less than 50 cc")
else:
    print("Sorry!! You are not Eligible for Driving Licence")

