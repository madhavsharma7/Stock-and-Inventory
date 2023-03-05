from tkinter import*
from tkinter import messagebox
import sqlite3
import pymysql.cursors
import os 

win=Tk()
win.geometry("510x420")
win.title("Change Password")
win.resizable(False,False)
win.config(bg="sky blue")

def update():
    a=str(num.get())#username
    b=str(num1.get())#oldps
    c=str(num2.get())#newps
    d=str(num3.get())#renp
    try:
        if(d==c):
            conn = sqlite3.connect(database=r'stock.db')
            mydb=conn.cursor()
            mydb.execute("update login set password='"+c+"' where username='"+a+"'")
            conn.commit()
            messagebox.showinfo("Message","password Updated")
        else:
            messagebox.showinfo("Message","Not Match")
    except:
        print("Not Changed")
    conn.close()

lb=Label(win,text="User Name",font=20,width=20).grid(row=0,column=0,padx=20,pady=20)

lb2=Label(win,text="Enter Old Password",font=20,width=16).grid(row=1,column=0,padx=20,pady=20)

lb3=Label(win,text="Enter New Password",font=20,width=16).grid(row=2,column=0,padx=20,pady=20)

lb4=Label(win,text="Re Enter New Password",font=20,width=20).grid(row=3,column=0,padx=20,pady=20)

num=StringVar()
tx=Entry(win,font=10,width=20,textvariable=num).grid(row=0,column=1)
num1=StringVar()
tx2=Entry(win,font=10,width=20,textvariable=num1).grid(row=1,column=1)
num2=StringVar()
tx3=Entry(win,font=10,width=20,textvariable=num2).grid(row=2,column=1)
num3=StringVar()
tx4=Entry(win,font=10,width=20,textvariable=num3).grid(row=3,column=1)

btn=Button(win,text="Change",relief="raised",bd=10,font=20,command=update,highlightbackground="blue",highlightthickness=10).place(x=200,y=310)

win.mainloop()
