from tkinter import*
import sqlite3
import pymysql.cursors
import os
from tkinter import messagebox

win=Tk()
win.config(bg="skyblue")
win.geometry("350x350")
win.resizable(False,False)
win.title("Forget Password Page")

def insert():
   #a=str(num1.get())
    conn = sqlite3.connect(database=r'stock.db')
    mydb=conn.cursor()
    mydb.execute("select password from login where username='"+num1.get()+"'")
    conn.commit()
    result=mydb.fetchall()
    count=mydb.rowcount
    print(result)
    print(count)
    if count>0:
        for row in result:
            {
                messagebox.showinfo("Message",row)
            }
    else:
        messagebox.showerror("Message","Fill Details")
  
frame=Frame(win,bd=10,relief="raised",width=350,height=50,bg="grey").grid(row=0)
lb=Label(frame,text="FORGET PASSWORD",font=40,bg="grey").grid(row=0)

lb3=Label(win,text="User Name",width=15,font=('arial',18,'bold')).place(x=60,y=100)


num1=StringVar()
tx3=Entry(win,textvariable=num1,font=40).place(x=80,y=180)

btn=Button(win,text="Submit",bd=5,relief="raised",command=insert,font=20).place(x=130,y=250)

win.mainloop()
