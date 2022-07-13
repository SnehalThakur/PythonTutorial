class Employee:
    company = "JetBrains"   # class level variable

    # def __init__(self):  # Default Constructor
    #     pass

    def __init__(self, name, age):  # Parameterized Constructor
        self.name = name
        self.age = age


# Object Creation
# employee1 = Employee() # Object creation of Default Constructor

# Object 1 creation
employee1 = Employee("Sam", 30)  # Object creation of Parameterized Constructor

# Object 2 creation
employee2 = Employee("John", 40)

print("Employee1 Object", employee1)
print("Employee1 Detail-", "Employee Company:", employee1.company, ",Employee Name:", employee1.name, ", age:",
      employee1.age)
print("========================================")

print("Employee2 Object", employee2)
print("Employee2 Detail-", "Employee Company:", employee2.company, ",Employee Name:", employee2.name, ", age:",
      employee2.age)
