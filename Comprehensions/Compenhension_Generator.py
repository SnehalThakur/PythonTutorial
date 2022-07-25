# Generator Comprehension

l1 = [10, 20, 30, 40 , 50]

generatorOut = (out**3 for out in l1)
print("generatorOut=", generatorOut, "and type(generatorOut)=",type(generatorOut))
for i in generatorOut:
    print(i)
