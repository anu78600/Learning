import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor() # apne table me data store kar rhe h , column wise
mycursor.execute("insert into test2.test_table values(123,'anup',234.56,45,'kumar')")
# multiple insert  v ham kar skte h
mycursor.execute("insert into test2.test_table values(123,'anup',234.56,45,'kumar')")
mycursor.execute("insert into test2.test_table values(123,'anup',234.56,45,'kumar')")
# data table me turant nhi dikhta h , uske liye hme commit krna pdhta h

mydb.commit()

mydb.close()