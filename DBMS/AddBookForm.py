# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 19:49:06 2022

@author: disha
"""

from tkinter import *
from backend import *

import datetime

ws = Tk()
ws.title("Add New Book")
ws.geometry('500x500')
ws['bg'] = '#00c3ff'

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(ws,text="Add New Book", width=20,font=("bold",20), bg = '#00c3ff')
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=0)

label_1 =Label(ws,text="Book Name", width=10,font=("bold",10), bg = '#00c3ff')
label_1.place(x=60,y=60)

label_2 =Label(ws,text="Author", width=10,font=("bold",10), bg = '#00c3ff')
label_2.place(x=60,y=100)

label_3 =Label(ws,text="Edition", width=10,font=("bold",10), bg = '#00c3ff')
label_3.place(x=60,y=140)

label_4 =Label(ws,text="Publication Year", width=15,font=("bold",10), bg = '#00c3ff')
label_4.place(x=35,y=180)

label_5 =Label(ws,text="Publisher", width=10,font=("bold",10), bg = '#00c3ff')
label_5.place(x=60,y=220)

label_6 =Label(ws,text="Type", width=10,font=("bold",10), bg = '#00c3ff')
label_6.place(x=60,y=260)

label_7 =Label(ws,text="Language", width=10,font=("bold",10), bg = '#00c3ff')
label_7.place(x=60,y=300)

label_8 =Label(ws,text="Purchase Date", width=10,font=("bold",10), bg = '#00c3ff')
label_8.place(x=60,y=340)

label_9 =Label(ws,text="Price", width=10,font=("bold",10), bg = '#00c3ff')
label_9.place(x=60,y=380)

#label_10 =Label(ws,text="Copies", width=10,font=("bold",10), bg = '#00c3ff')
#label_10.place(x=60,y=420)

def printValue():
    
    bookname = book_name.get()
    Author = author.get()
    Edition = edition.get()
    PY = py.get()
    PB = pb.get()
    Typee = Type.get()
    Language = Lang.get()
    PD = pd.get()
    Price = price.get()
    #Copies = copies.get()
    
    Label(ws, text=f'{bookname}, Added!', pady=5,bg = '#00c3ff').place(x=300,y=450)
    
    BOOKname = f'{bookname}' 
    AUTHOR = f'{Author}'
    Pub = f'{PB}'
    TYPE = f'{Typee}'
    LANGUAGE = f'{Language}'
    purDate = datetime.datetime.strptime(PD, "%d/%m/%Y").date()
    
    addBook(BOOKname,AUTHOR,Edition,PY,Pub,TYPE,LANGUAGE,purDate,Price)
    

book_name = Entry(ws)
book_name.place(x=150,y=62)

author = Entry(ws)
author.place(x=150,y=102)

edition = Entry(ws)
edition.place(x=150,y=142)

py = Entry(ws)
py.place(x=150,y=182)

pb= Entry(ws)
pb.place(x=150,y=222)

Type= Entry(ws)
Type.place(x=150,y=262)

Lang= Entry(ws)
Lang.place(x=150,y=302)

pd= Entry(ws)
pd.place(x=150,y=342)

price= Entry(ws)
price.place(x=150,y=382)

#copies= Entry(ws)
#copies.place(x=150,y=422)

Button(
    ws,
    text="Add Book", 
    width=20,
    padx=10, 
    pady=5,
    command=printValue
    ).place(x=150,y=450)


ws.mainloop()