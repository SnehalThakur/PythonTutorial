import sqlite3

# Open a Database connection
connection = sqlite3.connect(r"C:\Users\Snehal Thakur\PycharmProjects\pythonProject\SQLite\db\employeeSqlite1.db")
print("connection=", connection)
print("sqlite3.version=", sqlite3.version)

# Getting all tables from sqlite_master
sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

# Creating cursor object using connection object
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Employees
                (EmployeeID int,
                EmployeeName varchar(255),
                Designation varchar(255),
                Address varchar(255),
                City varchar(255)
                );""")

# # executing our sql query
cursor.execute(sql_query)
print("List of tables\n")

# printing all tables list
print(cursor.fetchall())

cursor.execute("""INSERT INTO Employees VALUES (102, "John2", "CEO2", "Church Gate Road", "London2");""")
cursor.execute("""INSERT INTO Employees VALUES (103, "John3", "CEO3", "Church Gate Road", "London3");""")
cursor.execute("""INSERT INTO Employees VALUES (104, "John4", "CEO4", "Church Gate Road", "London4");""")
cursor.execute("""INSERT INTO Employees VALUES (105, "John5", "CEO5", "Church Gate Road", "London5");""")
cursor.execute("""INSERT INTO Employees VALUES (106, "John6", "CEO6", "Church Gate Road", "London6");""")
connection.commit()
cursor.execute("select * from Employees")
print(cursor.fetchall())
# connection.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
# print("Table created successfully");