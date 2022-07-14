class Company:
    def __init__(self, companyName):
        self.companyName = companyName

    def getCompanyInfo(self):
        print("This is Company class")


class ThirdPartyVendors(Company):
    def __init__(self, vendorName):
        self.vendorName = vendorName

        # Initializing constructor of super/ parent class i.e Company
        super().__init__("HCL")

    def getThirdPartyCompanyInfo(self):
        print("This is ThirdPartyCompany class")


class Dummy:
    pass


class Employee(ThirdPartyVendors):
    def __init__(self, employeeName):
        self.employeeName = employeeName

        # Initializing constructor of super/ parent class i.e ThirdPartyVendors
        super().__init__("RecruitingCompany")

    def getEmployeeInfo(self):
        print("This is Employee class")


# Creating the object of Employee class
employee = Employee("John")
employee.getCompanyInfo()
employee.getThirdPartyCompanyInfo()
employee.getEmployeeInfo()
print("===============================")
print("employee.vendorName =", employee.vendorName)
print("employee.companyName =", employee.companyName)
print("employee.employeeName =", employee.employeeName)
print("===============================")
# isinstance() -  To check whether the object is an instance of a class
print("isinstance(employee, Employee) =", isinstance(employee, Employee))
print("isinstance(employee, ThirdPartyVendors) =", isinstance(employee, ThirdPartyVendors))
print("isinstance(employee, Company) =", isinstance(employee, Company))
print("isinstance(employee, Dummy) =", isinstance(employee, Dummy))
print("===============================")
# issubclass() - To check whether the class is subclass of other class or not
print("issubclass(Employee, ThirdPartyVendors) = ", issubclass(Employee, ThirdPartyVendors))
print("issubclass(Employee, Company) = ", issubclass(Employee, Company))
print("issubclass(ThirdPartyVendors, Company) = ", issubclass(ThirdPartyVendors, Company))
print("issubclass(Company, ThirdPartyVendors) = ", issubclass(Company, ThirdPartyVendors))
print("issubclass(Company, Employee) = ", issubclass(Company, Employee))
