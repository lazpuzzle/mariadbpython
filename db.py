import mysql.connector
from dotenv import load_dotenv
import os

env_path=os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

mydb = mysql.connector.connect(
  host=os.environ.get("HOST"),
  port=os.environ.get("PORT"),
  user=os.environ.get("USER"),
  password=os.environ.get("PASSWORD"),
  database="superset"
)

mycursor = mydb.cursor()
# print(mydb)
sql = "select * from ab_role"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)