class Employee:
    company = "JetBrains"
    numberOfEmployee = 0

    def __init__(self):  # Default Constructor
        self.employeeId = None
        self.employeePlace = None
        self.name = None
        self.age = None
        self.employeeDetails = []
        self.numberOfEmployee += 1

    # Setter method
    def setEmployeeDetails(self, empId, empPlace):
        self.employeeId = empId
        self.employeePlace = empPlace

    # Getter Method
    def getEmployeeDetails(self):
        print("Employee Detail ")
        print("Employee Company:", self.company, ", Employee Id:", self.employeeId,
              ", Employee Name:", self.name, ", age:", self.age, ", place:", self.employeePlace)

    def appendEmployeeDetails(self, emplyId, emplyName, emplyAge, emplyPlace):
        self.employeeId = emplyId
        self.name = emplyName
        self.age = emplyAge
        self.employeePlace = emplyPlace
        self.employeeDetails.append(self.employeeId)
        self.employeeDetails.append(self.name)
        self.employeeDetails.append(self.age)
        self.employeeDetails.append(self.employeePlace)
        return self.employeeDetails


employeeNumber = int(input("How many Employee details you want to store: "))

employeeDict = {}

for i in range(1, employeeNumber + 1):
    print(i)
    # Object 1 creation
    print("Enter Employee Details: ", i)
    empId = input("Enter Employee ID: ")
    empName = input("Enter Employee Name: ")
    empAge = int(input("Enter Employee Age: "))
    empCountry = input("Enter Employee Country: ")

    employee = Employee()  # Object creation of Employee class
    employeeDetail = employee.appendEmployeeDetails(empId, empName, empAge, empCountry)  # calling append employee
    # method
    print(employeeDetail)
    employeeDict[i] = employeeDetail
    #
    """
    {
        'employeeKey':[id, name, age, place]
    }
    
    from numpy import size
    f=open('Taxation.txt','a')
    # list1 =[]
    for i in range(5):
        roll_no=int(input(' Roll no: '))
        name=input('Enter the name: ')
        marks=float(input('Enter the marks: '))
        reco=(f'roll_no {roll_no} '+'name {name},'+' marks{marks} ')
        f.write(reco)
    f.close()
    """
print("employeeDetail = ", employeeDict)
