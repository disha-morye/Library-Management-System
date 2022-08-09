# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 09:49:32 2022

@author: disha
"""

from tkinter import *
from backend import *
import datetime

ws = Tk()
ws.title("Transactions")
ws.geometry('500x500')
ws['bg'] = '#00c3ff'

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(ws,text="Issue a Book", width=20,font=("bold",20), bg = '#00c3ff')
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=0)

label_1 =Label(ws,text="Book Id", width=10,font=("bold",10), bg = '#00c3ff')
label_1.place(x=60,y=77)

label_2 =Label(ws,text="Member Id", width=10,font=("bold",10), bg = '#00c3ff')
label_2.place(x=60,y=117)

label_3 =Label(ws,text="Issue Date", width=10,font=("bold",10), bg = '#00c3ff')
label_3.place(x=60,y=157)


def issue():
    BookId = book_id.get()
    MemberId = member_id.get()
    IssueDate = issue_date.get()
    
    Label(ws, text='Issued!', pady=5,bg = '#00c3ff').place(x=100,y=420)
    ID = datetime.datetime.strptime(IssueDate, "%d/%m/%Y").date()
    
    issueBook(BookId,MemberId,ID)
    


book_id = Entry(ws)
book_id.place(x=150,y=80)

member_id = Entry(ws)
member_id.place(x=150,y=120)

issue_date = Entry(ws)
issue_date.place(x=150,y=160)


Button(
    ws,
    text="Issue", 
    width=20,
    padx=10, 
    pady=5,
    command=issue
    ).place(x=100,y=380)


ws.mainloop()