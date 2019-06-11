import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root"
)
cursor=db.cursor()
cursor.execute("create database 3edge")

#show databases;

#pip install mysql-connector-python