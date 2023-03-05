from tkinter import*
from tkinter import messagebox
import sqlite3
import pymysql.cursors
import os
win= Tk()
win.geometry("500x500")
win.resizable(False,False)
win.title("ADMIN LOGIN")

def admin():
    conn = sqlite3.connect(database=r'stock.db')
    mydb=conn.cursor()
    #a=str(num1.get())
    #b=str(num2.get())
    #email="admin"
    #passs="123456"
    try:

        mydb.execute("select * from login where username=? and password = ?",(num1.get(),num2.get()))
        result=mydb.fetchone()
        count=mydb.rowcount  
        print(result)      
        if result:

            os.system('admin.py')
        else:
            messagebox.showerror("Message","Invalid userid & password")
    except:
         messagebox.showerror("Message","DATABASE NOT CONNECTED")
    conn.close()

frame=Frame(win,bd=10,relief="raised",width=500,height=50,bg="grey").grid(row=0)
lb=Label(frame,text="INVENTORY MANAGEMENT SYSTEM",font=('arial',20,'bold'),bg="grey").grid(row=0)
frame2=Frame(win,bd=10,relief="raised",width=400,height=400,bg="skyblue").place(x=50,y=75)
frame3=Frame(win,bd=9,relief="raised",width=350,height=60).place(x=75,y=100)
lb2=Label(frame3,text="ADMIN LOGIN",font=('arial',20,'bold')).place(x=155,y=110)

lb=Label(frame2,text="Username",width=10,font=40).place(x=120,y=200)
lb2=Label(frame2,text="Password",width=10,font=40).place(x=120,y=250)

num1=StringVar()
tx=Entry(frame2,textvariable=num1,font=50,width=15).place(x=240,y=200)
num2=StringVar()
tx2=Entry(frame2,textvariable=num2,font=50,width=15).place(x=240,y=250)

btn=Button(frame2,text="Submit",font=30,command=admin,bd=5,relief="groove",width=10).place(x=195,y=300)

def forget():
    os.system("forgetpassword.py")

btn=Button(frame2,text="Forget Password",font=30,bd=5,relief="sunken",command=forget).place(x=170,y=370)

win.mainloop()
