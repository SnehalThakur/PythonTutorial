import time

t = time.time()
print("time=", t)

lt = time.localtime()
print("time=", lt)

ct = time.ctime()
print("time=", ct)

print("==================================")
startTime = time.time()
print("startTime=", startTime)

def calculateSquare(number):
    list1 = []
    for i in range(number):
        list1.append(i ** 2)
    return list1

square = calculateSquare(1000)
print("Square=", square)
endTime = time.time()
print("endTime=", endTime)
print("Execution time for calculateSquare() = ", endTime - startTime)

print("==================================")

startTime = time.time()
print("startTime=", startTime)
def calculateCube(number):
    list2 = []
    for i in range(number):
        list2.append(i ** 3)
    return list2

cube = calculateCube(1000)
print("Cube=", cube)
endTime = time.time()
print("endTime=", endTime)
print("Execution time for calculateCube() = ", endTime - startTime)

print("====================")
for i in range(1,101):
    time.sleep(5)
    print(i)