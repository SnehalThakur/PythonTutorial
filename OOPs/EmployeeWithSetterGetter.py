class Employee:
    company = "JetBrains"

    def __init__(self, name, age):  # Parameterized Constructor
        self.employeeId = None
        self.employeePlace = None
        self.name = name
        self.age = age

    # Setter method
    def setEmployeeDetails(self, empId, empPlace):
        self.employeeId = empId
        self.employeePlace = empPlace

    # Getter Method
    def getEmployeeDetails(self):
        print("Employee Detail ")
        print("Employee Company:", self.company, ", Employee Id:", self.employeeId,
              ", Employee Name:", self.name, ", age:",
              self.age, ", place:", self.employeePlace)


# Object 1 creation
print("Enter Employee Details")
empId = input("Enter Employee ID")
empName = input("Enter Employee Name")
empAge = int(input("Enter Employee Age"))
empCountry = input("Enter Employee Country")

employee1 = Employee(empName, empAge)  # Object creation of Parameterized Constructor
employee1.setEmployeeDetails(empId, empCountry)  # Calling setter method
employee1.getEmployeeDetails()  # calling getter method
