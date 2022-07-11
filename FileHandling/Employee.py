# Read the employee file data and find following questions-
# 1. Maximum Age
# 2. Maximum Salary
# 3. Employee Name with Maximum Age
# 4. Employee Name with Maximum Salary
# 5. Minimum Age
# 6. Minimum Salary
# 7. Employee Name with Minimum Age
# 8. Employee Name with Minimum Salary
# Assignment ???
# 9. Second Maximum Age
# 10. Second Maximum Salary
# 11. Employee Name with Second Maximum Age
# 12. Employee Name with Second Maximum Salary
# 13. Second Minimum Age
# 14. Second Minimum Salary
# 15. Employee Name with Second Minimum Age
# 16. Employee Name with Second Minimum Salary

# Step 1 -  Read Employee data
employee = open(r"C:\Users\Snehal Thakur\Desktop\PythonClass\FileHandling\employeeData.txt")
#print(employee.readlines())
counter = 1
emply = []
employeeName = []
employeeId = []
employeeAge = []
employeeSalary = []
empData = employee.readlines()
print("empData = ",empData)
print("len(empData) = ",len(empData))

for emp in empData:
    if counter !=1: # Skip the header line
        #print(emp,"and type is", type(emp))
        employeedata = emp.strip().split("\t")
        print("Employee data = ",employeedata)
        employeeName.append(employeedata[0]) # Name
        employeeId.append(employeedata[1])  # Id
        employeeAge.append(int(employeedata[2]))    # age
        employeeSalary.append(int(employeedata[3])) # salary
    counter+=1
print("---------------------")
print("employeeName=",employeeName)
print("employeeId=",employeeId)
print("employeeAge=",employeeAge)
print("employeeSalary=",employeeSalary)
print("===========================")
print("1. Maximum Age")
maxAge = max(employeeAge)
print("Employee with Maximum Age=", maxAge)
print("--------------------------")
print("2. Maximum Salary")
maxSalary = max(employeeSalary)
print("Employee with Maximum Salary=", maxSalary)
print("===========================")
print("3. Employee Name with Maximum Age")
employeeAgeIndex = employeeAge.index(maxAge) # index position of maximum age employee
print("employeeAgeIndex = ",employeeAgeIndex)
empNameWithMaxAge = employeeName[employeeAgeIndex] # employee name from the list of index position
print("Employee name is",empNameWithMaxAge,"having maximum age of",maxAge,"years")
print("===========================")
print("4. Employee Name with Maximum Salary")
employeeMaxSalaryIndex = employeeSalary.index(maxSalary) # index position of maximum salary
print("employeeMaxSalaryIndex =",employeeMaxSalaryIndex)
empNameWithMaxSalary = employeeName[employeeMaxSalaryIndex] # emp name w.r.t index
print("Employee name is",empNameWithMaxSalary,"have maximum salary of Rs.",maxSalary)
print("===========================")
print("5. Minimum Age")
minAge = min(employeeAge)
print("Employee with Minimum Age=",minAge)
print("===========================")
print("6. Minimum Salary")
minSalary = min(employeeSalary)
print("Employee with Minimum Salary=",minSalary)
print("===========================")
print("7. Employee Name with Minimum Age")
employeeWithMinAgeIndex = employeeAge.index(minAge) # index position of minimum age employee
print("employeeWithMinAgeIndex = ",employeeWithMinAgeIndex)
empNameWithMinAge = employeeName[employeeWithMinAgeIndex] # employee name from the list of index position
print("Employee name is",empNameWithMinAge,"having minimum age of",minAge,"years")
print("===========================")
print("8. Employee Name with Minimum Salary")
employeeMinSalaryIndex = employeeSalary.index(minSalary) # index position of minimum salary
print("employeeMinSalaryIndex =",employeeMinSalaryIndex)
empNameWithMinSalary = employeeName[employeeMinSalaryIndex] # emp name w.r.t index
print("Employee name is",empNameWithMinSalary,"have minimum salary of Rs.",minSalary)
print("===========================")
'''
for emp in empData:
    if counter !=1:
        print("Employee data line = ",emp)
        """
        Stripping the employee string and splitting it with tab \t seperator
        as we have tab seperated data in employee.txt
        """
        employeedata = emp.strip().split("\t")
        print("Employee data = ",employeedata)
        employeeName.append(employeedata[0]) # Name
        employeeId.append(employeedata[1])  # Id
        employeeAge.append(int(employeedata[2]))    # age
        employeeSalary.append(int(employeedata[3])) # salary
        emply.append(employeedata)
    counter+=1 # increment counter
print("Employee data outside for loop= ",emply)
print("employeeName=",employeeName)
print("employeeId=",employeeId)
print("employeeAge=",employeeAge)
print("employeeSalary=",employeeSalary)
print("===========================")
print("1. Maximum Age")
print("Employee with Maximum Age=",max(employeeAge))
print("--------------------------")
print("2. Maximum Salary")
print("Employee with Maximum Salary=",max(employeeSalary))
print("--------------------------")
print("===========================")
print("5. Minimum Age")
print("Employee with Minimum Age=",min(employeeAge))
print("--------------------------")
print("6. Minimum Salary")
print("Employee with Minimum Salary=",min(employeeSalary))
print("--------------------------")
'''
