"""
choose install 1 command:
    python -m pip install mysql-connector-python   : (reccomend command)
    pip install mysql-connector-python
"""


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

print(mydb) # check connection


mycursor = mydb.cursor()

# -----------------  Create database ---------------------
#-------------------------------------------------------
mycursor.execute("CREATE DATABASE mydatabase")
#-------------------------------------------------------
#-------------------------------------------------------

# Create table
#-------------------------------------------------------
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#-------------------------------------------------------
#-------------------------------------------------------

# Insert data
#-------------------------------------------------------
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21") # insert 1 value
# insert more value
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345')
]
mycursor.execute(sql, val)

mydb.commit() # close session and return memory
#-------------------------------------------------------
#-------------------------------------------------------

# Select data
#-------------------------------------------------------
sql = "SELECT * FROM customers"
mycursor.execute(sql)

myresult = mycursor.fetchall() # select all row
myresult = mycursor.fetchone() # select 1 row

# loop for print data
for x in myresult:
  print(x)
#-------------------------------------------------------
#-------------------------------------------------------