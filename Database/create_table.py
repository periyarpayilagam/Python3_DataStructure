import mysql.connector
db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="3edge"
)

cursor=db.cursor()
cursor.execute("create table trainees(name varchar(30), age varchar(30))")

#use db;
#show tables;