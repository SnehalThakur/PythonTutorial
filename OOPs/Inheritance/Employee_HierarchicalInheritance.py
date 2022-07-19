class Company:
    def getCompanyInfo(self):
        print("This is Company class")


class HR(Company):
    def getHRInfo(self):
        print("This is HR class")


class Accounts(Company):
    def getAccountsInfo(self):
        print("This is Accounts class")


class Management(Company):
    def getManagementInfo(self):
        print("This is Management class")


# Creating class objects of HR, Accounts, Management
hr = HR()
print("hr object =", hr)
hr.getHRInfo()
hr.getCompanyInfo()
print("==========================")
accounts = Accounts()
accounts.getAccountsInfo()
accounts.getCompanyInfo()
print("accounts object =", accounts)
print("==========================")
management = Management()
print("management object =", management)
management.getManagementInfo()
management.getCompanyInfo()
