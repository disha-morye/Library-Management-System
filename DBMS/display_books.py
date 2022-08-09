# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 13:25:22 2022

@author: disha
"""

from tkinter import *
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\disha\OneDrive\Desktop\DBMS\Test.accdb;')
cursor = conn.cursor()

ws = Tk()
ws.title("Display Books")
ws.geometry('1000x700')
ws['bg'] = '#00c3ff'

def giveBooks():
    i=0
    #arr1 = ['Book ID','Book Name','Author','Edition','Publication Year','Pusblisher','Type','Language','Purchase Date','Price','Copies']
    arr = []
    data=cursor.execute('''SELECT * FROM Books''')
    for column in data.description:
        arr.append(column[0])
    for book in cursor:
        for j in range(len(book)):
            #print(book[j],end=' ')
        #i += 1
        #print()
            x = Label(ws,width=12,text=arr[j],fg = 'black',bg='#00c3ff')
            x.grid(row=0,column=j)            
            e = Entry(ws,width=14,fg = 'black')
            e.grid(row=i+4,column=j)
            e.insert(END,book[j])
            
        i += 1
    """
def searchBook():
    search_result = search.get()
    cursor.execute('SELECT * FROM Books WHERE Author IN (search_result)')
    result = cursor.fetchall()
    s = Entry(ws,width=12,fg = 'blue',bd=2)
    s.place(x=100,y=420)
    s.grid(row=i+20,column=j)
    s.insert(END,result)
    
    for i in cursor:
        for j in range(len(i)):
            t1 = result[i][j]
            if (t1 == search_result):
                s = Entry(ws,width=12,fg = 'blue',bd=2)
                s.grid(row=i+20,column=j)
                s.insert(END,book[j])
                break
            else:
                 y = Label(ws,width=12,text='Invalid',fg = 'blue',bg='yellow')
                 y.grid(row=i+20,column=j)
                 
    
search = Entry(ws,width=30)
search.place(x=175,y=657)
    
Button(
    ws,
    text="Search", 
    width=20,
    #padx=10, 
    #pady=5,
    command=searchBook
    ).place(x=10,y=655)
"""

giveBooks()


ws.mainloop()