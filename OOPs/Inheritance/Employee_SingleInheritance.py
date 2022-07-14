class Company:
    def getCompanyInfo(self):
        print("This is Company class and Company Name is Jetbrains")


class Employee(Company):
    def getEmployeeInfo(self):
        print("This is Employee class")


# Creating object of Company Class
company = Company()
print(company)
company.getCompanyInfo()

# Creating object of Employee Class
employee = Employee()
print(employee)
employee.getEmployeeInfo()
employee.getCompanyInfo()
