fruits = ["banana","apple","grapes","papaya","orange"]
fruitInput = input("Enter fruit name ")
#print("fruitInput=",fruitInput)
print("'break' keyword# break the execution of loop")
for fruit in fruits:
    if fruitInput == fruit:
        print("fruit found=",fruit)
        break # break the execution of loop
    else :
        print("fruit not found!!")
print("For loop execution completed")
print("==========================")
print("'continue' keyword# continue the execution of loop")
for fruit in fruits:
    if fruitInput == fruit:
        continue
        print("fruit found=",fruit)
        print("fruit found=",fruit)
        print("fruit found=",fruit)
    else :
        print("fruit not found!!")
print("==========================")

