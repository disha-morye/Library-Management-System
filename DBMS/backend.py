# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:01:18 2022

@author: disha
"""

import pyodbc
from datetime import date, timedelta
import math

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\disha\OneDrive\Desktop\DBMS\Test.accdb;')
cursor = conn.cursor()

cursor.execute('SELECT MAX(MemberId) FROM Members')
meme = cursor.fetchall()

lastMemId = meme[0][0]

def addMem(Fname,LName,MobileNum,EmailId,DOB,City):
    
    MemberId = lastMemId + 1
    Address = City
    MobileNo = MobileNum
    Email = EmailId
    DoB = DOB
    Fee = 100.00
    RenewalDate = date.today() + timedelta(180)
    FName = Fname
    LName = LName
    
    if(date.today()>RenewalDate):
        Fine = 5 * (date.today() - timedelta(RenewalDate))
    else:
        Fine = 0
    
    if(date.today() > RenewalDate):
        Status = "Deactivated"
    else:
        Status = "Activated"
    
    sql = "INSERT INTO Members VALUES (?,?,?,?,?,?,?,?,?,?,?);"
    cursor.execute(sql,(MemberId,Address,MobileNo,Email,DoB,Fee,Fine,RenewalDate,Status,FName,LName))
    
    #delete = "DELETE * FROM Members WHERE MemberId IN (17);"
    #cursor.execute(delete)
    
    conn.commit() 
    

cursor.execute('SELECT MAX(bookId) FROM Books')
books = cursor.fetchall()

lastBookId = books[0][0]
    
def addBook(bookName, Author, Edition, PublicationYear,Publisher,Type,Language,PurchaseDate,Price):
    
    bookId = lastBookId +1
    #getCopies = Copies
    sql = "INSERT INTO Books VALUES (?,?,?,?,?,?,?,?,?,?);"
    cursor.execute(sql,(bookId,bookName,Author,Edition,PublicationYear,Publisher,Type,Language,PurchaseDate,Price))
    
    #delete = "DELETE * FROM Books WHERE bookId IN (17);"
    #cursor.execute(delete)
    
    conn.commit() 
    

cursor.execute('SELECT MAX(SrNo) FROM Transactions')
srno = cursor.fetchall()

lastSrNo = srno[0][0]    
    
def issueBook(bookId,MemberId,IssueDate):
    SrNo = lastSrNo + 1
    ReturnDate = IssueDate + timedelta(30)
    #if(addBook.getCopies != 0):
    sql = "INSERT INTO Transactions VALUES (?,?,?,?,?);"
    cursor.execute(sql,(bookId,MemberId,SrNo,IssueDate,ReturnDate))      

    conn.commit()
    
    
"""
cursor.execute('select * from Members')
result = cursor.fetchall()
    
for row in result:
    print(row)
    print(" ")
"""

    