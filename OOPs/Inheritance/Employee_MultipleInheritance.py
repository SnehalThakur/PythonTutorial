class ThirdPartyCompany:
    def getThirdPartyCompanyInfo(self):
        print("This is ThirdPartyCompany class")


class Company:
    def getCompanyInfo(self):
        print("This is Company class")


class Employee(ThirdPartyCompany, Company):
    def getEmployeeInfo(self):
        print("This is Employee class")

thirdPartyCompany = ThirdPartyCompany()
print(thirdPartyCompany)
thirdPartyCompany.getThirdPartyCompanyInfo()
print("===================================")
company = Company()
print(company)
company.getCompanyInfo()
print("===================================")
employee = Employee()
print(employee)
employee.getEmployeeInfo()
employee.getCompanyInfo()
employee.getThirdPartyCompanyInfo()