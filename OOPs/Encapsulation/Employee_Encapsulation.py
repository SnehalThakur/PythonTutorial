class Employee:

    def __init__(self, name, salary, address):
        self.name = name
        self.__salary = salary
        self._address = address

    def employeeDetail(self):
        print("Employee Name:", self.name, "Salary:", self.__salary, "Address:", self._address)


employee = Employee("John", "$50000", "Church Gate")
employee.employeeDetail()

print("employee.name =", employee.name)
print("employee.__salary=", employee.__salary)