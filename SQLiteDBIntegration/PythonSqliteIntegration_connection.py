import sqlite3

sqlConnection = sqlite3.connect(r"C:\Users\Snehal Thakur\PycharmProjects\pythonProject\SQLite\db\company.db")
print(sqlConnection)

sqlConnection.execute("""
                CREATE TABLE IF NOT EXISTS CompanyNew
                    (CompanyID int PRIMARY KEY,
                    CompanyName varchar(255),
                    CEO varchar(255),
                    Address varchar(255),
                    Country varchar(255)
                    );
                """)

cursor = sqlConnection.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
print(cursor.fetchall())

CompanyID = input("Please enter company id")
CompanyName = input("Please enter company name")
CEO = input("Please enter company CEO")
Address = input("Please enter company address")
Country = input("Please enter company country")

sqlConnection.execute(
    "insert into Company(CompanyID, CompanyName,CEO, Address, Country) values (?, ?, ?, ?, ?)",
    (CompanyID, CompanyName, CEO, Address, Country))

cursor = sqlConnection.execute("select * from Company")
sqlConnection.commit()

print(cursor.fetchall())
