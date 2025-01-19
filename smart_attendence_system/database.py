from library import mysql
from library import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "charusat_students"
)

mycursor = mydb.cursor()
db_name = datetime.date.today()
# db_name = 'temp'
db_name = db_name.strftime('%Y_%m_%d')


#mycursor.execute(f"CREATE DATABASE charusat_students")            
mycursor.execute(f"CREATE TABLE {str(db_name)} (stu_name VARCHAR(255), present_date DATE)")
