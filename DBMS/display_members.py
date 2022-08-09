# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:19:39 2022

@author: disha
"""

from tkinter import *
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\disha\OneDrive\Desktop\DBMS\Test.accdb;')
cursor = conn.cursor()

ws = Tk()
ws.title("Display Members")
ws.geometry('1000x700')
ws['bg'] = '#00c3ff'

def giveMems():
    i=0
    #arr1 = ['Book ID','Book Name','Author','Edition','Publication Year','Pusblisher','Type','Language','Purchase Date','Price','Copies']
    arr = []
    data=cursor.execute('''SELECT * FROM Members''')
    for column in data.description:
        arr.append(column[0])
    for mem in cursor:
        for j in range(len(mem)):
            #print(book[j],end=' ')
        #i += 1
        #print()
            x = Label(ws,width=12,text=arr[j],fg = 'black',bg='#00c3ff')
            x.grid(row=0,column=j)            
            e = Entry(ws,width=14,fg = 'black')
            e.grid(row=i+4,column=j)
            e.insert(END,mem[j])
            
        i += 1
        
giveMems()


ws.mainloop()