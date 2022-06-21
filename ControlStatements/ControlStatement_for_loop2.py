print("""
range() in for loop
range(stop)
range(start, stop)
range(start, stop, step""")

numberInput = int(input("Enter any number "))

print("1. range(5)")
for i in range(5):  # 0, 1 , 2, 3, 4
    print(i)
print("=======================")
print("2. range(1,11)")
print("Multiplication table of",numberInput)
for i in range(1,11):
    print(numberInput,"x",i,"=",i*numberInput)
print("=======================")
print("3. range(1,100,5)")
for i in range(1,100,5):
    print(i)
print("====================")
print("4. reversed(range(5))")
for i in reversed(range(5)): 
    print(i)            # 4, 3, 2, 1, 0
