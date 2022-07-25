# Dictionary Comprehension
# Create a dictionary of State and Capital

state = ["Maharashtra", "MP", "Rajastan"]
capital = ["Mumbai", "Bhopal", "Jaipur"]
dict1 = zip(state, capital)
stateCapitalDict = {}
for (key, value) in dict1:
    stateCapitalDict[key] = value
print("stateCapitalDict =>", stateCapitalDict)
print("=================================")
# Using Dictionary Comprehension

stateCapitalDict1 = {key : value for (key, value) in zip(state, capital)}
print("stateCapitalDict1 =>", stateCapitalDict1)
