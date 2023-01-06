from django.shortcuts import render
from akvap2.models import User
import sqlite3

# Create your views here.

con=sqlite3.connect('db.sqlite3')

def insertData(name,age,city):
    qry="insert into t_users (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("User Details Added")

def updateData(age,id):
    qry="update t_users set AGE=? where id=?;"
    con.execute(qry,(age,id))
    con.commit()
    print("User Details Updated")
    
def deleteData(id):
    qry="delete from t_users where id=?;"
    con.execute(qry,(id))
    con.commit()
    print("User Details Deleted")
    
def selectData(id):
    qry="select id,name from t_users where id=?;"
    #con.execute(qry)
    #con.commit()
    result=con.execute(qry,(id))
    print("User Details Selected")
    for row in result:
        print(row)
       
    
print(""" 
      1.Insert
      2.Update
      3.Delete
      4.Select 
      """)
ch=1
while ch==1:
    c=int(input("Select Your Choice : "))
    if(c==1):
        print("Add New Record")
        name=input("Enter Name : ")
        age=input("Enter Age : ")
        city=input("Enter City : ")
        insertData(name,age,city)
    elif (c==2):
        print("Edit A Record")
        id=input("Enter ID : ")
        #name=input("Enter Name : ")
        age=input("Enter Age : ")
        #city=input("Enter City : ")
        updateData(age,id)
    
    elif (c==3):
        print("Delete A Record")
        id=input("Enter ID : ")
        deleteData(id)
        
    elif (c==4):
        print("Print A Record")
        id=input("Enter ID : ")        
        selectData(id)
    else:
        print("Invalid Selection")
    ch=int(input("Enter 1 To Continue : "))
print("Thank You")
