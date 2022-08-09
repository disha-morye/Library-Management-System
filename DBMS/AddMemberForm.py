# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:25:54 2022

@author: disha
"""

from tkinter import *
from backend import *
import datetime

ws = Tk()
ws.title("Add New Member")
ws.geometry('500x500')
ws['bg'] = '#00c3ff'

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(ws,text="Add New Member", width=20,font=("bold",20), bg = '#00c3ff')
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=0)

label_1 =Label(ws,text="First Name", width=10,font=("bold",10), bg = '#00c3ff')
label_1.place(x=60,y=77)

label_2 =Label(ws,text="Last Name", width=10,font=("bold",10), bg = '#00c3ff')
label_2.place(x=60,y=117)

label_3 =Label(ws,text="Mobile", width=10,font=("bold",10), bg = '#00c3ff')
label_3.place(x=60,y=157)

label_4 =Label(ws,text="Email", width=10,font=("bold",10), bg = '#00c3ff')
label_4.place(x=60,y=197)

label_5 =Label(ws,text="DOB", width=10,font=("bold",10), bg = '#00c3ff')
label_5.place(x=60,y=237)

label_6 =Label(ws,text="City", width=10,font=("bold",10), bg = '#00c3ff')
label_6.place(x=60,y=277)

def printValue():
    fname = first_name.get()
    lname = last_name.get()
    mobile = mobilenum.get()
    emailid = email.get()
    birth = dob.get()
    addcity = city.get()
    
    Label(ws, text=f'{fname}, Registered!', pady=5,bg = '#00c3ff').place(x=100,y=420)
    
    FName = f'{fname}' 
    LName = f'{lname}'
    MobileNum = mobile
    EmailId = f'{emailid}'
    DOB = datetime.datetime.strptime(birth, "%d/%m/%Y").date()
    City = f'{addcity}'
    
    addMem(FName,LName,MobileNum,EmailId,DOB,City)
    


first_name = Entry(ws)
first_name.place(x=150,y=80)

last_name = Entry(ws)
last_name.place(x=150,y=120)

mobilenum = Entry(ws)
mobilenum.place(x=150,y=160)

email = Entry(ws)
email.place(x=150,y=200)

dob = Entry(ws)
dob.place(x=150,y=240)

city= Entry(ws)
city.place(x=150,y=280)

Button(
    ws,
    text="Register Member", 
    width=20,
    padx=10, 
    pady=5,
    command=printValue
    ).place(x=100,y=380)


ws.mainloop()