import datetime as dt

curentdatetime = dt.datetime.now()
print("Current Date and Time=", curentdatetime)

currentDate = dt.date.today()
print("Current Date =", currentDate)

currentDateYear = dt.date.today().year
print("Current Year =", currentDateYear)

currentDateMonth = dt.date.today().month
print("Current Month =", currentDateMonth)

currentDateDay = dt.date.today().day
print("Current Day =", currentDateDay)


dt = dt.date(year=2022, month=7, day=20)
print("Custom date=", dt)
