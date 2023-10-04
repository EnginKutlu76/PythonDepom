import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("select FirstName,LastName from customers where city = 'London'")

#order by firstName    like %a%    str(row[1])

for row in cursor:
    print("First Name = " + row[0])
    print("Last Name = " + row[1])
    print("*************")
    
connection.close()