from tkinter import*
from tkinter import messagebox
import sqlite3
import pymysql.cursors
import os
win= Tk()
win.geometry("1372x710")
win.title("CUSTOMER")
win.resizable(False,False)


frame=Frame(win,bd=10,relief="raised",width=1368,height=60,bg="grey").grid(row=0)
lb=Label(frame,text="SALES MANAGEMENT SYSTEM",font=('arial',20,'bold'),bg="grey").grid(row=0)

#AVAILABLE ITEMS
frame1=Frame(win,bd=10,relief="raised",width=550,height=647,bg="sky blue").place(x=0,y=60)
frame2=Frame(win,bd=10,relief="raised",width=550,height=60).place(x=0,y=60)
lb=Label(frame2,text="AVAILABLE ITEMS",font=('arial',18,'bold')).place(x=150,y=70)
def data():
    
    conn = sqlite3.connect(database=r'stock.db')
    mydb=conn.cursor()
    mydb.execute("select * from stock")
    result=mydb.fetchall()
    count=mydb.rowcount
    print(result)
    #print(count)
    num=16
    tx=Text(frame2,font="vendata 15",width=44,height=15)
    tx.insert(END,"\nCode\tName\t\tQuantity\tPrice")
    tx.place(x=num,y=250)
    for i in result:
        tx.insert(END,"\n{0}\t{1}\t\t{2}\t{3}".format(i[0],i[1],i[2],i[3]))
        num+=1
    
#List
btn4=Button(frame2,text="Show Items",command=data,font=('arial',15,'bold'),bd=5,relief="raised",width=15).place(x=180,y=150)

#CART
def amount():
    a=int(pq.get())
    b=int(pp.get())

   
    messagebox.showinfo("Payment", a * b)

def cart():
    conn = sqlite3.connect(database=r'stock.db')
    mydb=conn.cursor()
    
    try:
        
        mydb.execute("update stock set quantity = quantity - '"+pq.get()+"' where product_id ='"+pc.get()+"'")
        conn.commit()
        messagebox.showinfo("Message","Added to Cart")

    except:
        messagebox.showerror("error","cart not updated")
    conn.close()
frame3=Frame(win,bd=10,relief="raised",width=450,height=647,bg="sky blue").place(x=550,y=60)
frame4=Frame(win,bd=10,relief="raised",width=450,height=60).place(x=550,y=60)

lb=Label(frame4,text="CART",font=('arial',18,'bold')).place(x=750,y=70)

lb=Label(frame4,text="Product Code",font=('arial',18,'bold')).place(x=590,y=150)
pc=StringVar()
tx=Entry(frame4,font=70,width=15,textvariable=pc).place(x=810,y=160)
lb=Label(frame4,text="Product Name",font=('arial',18,'bold')).place(x=590,y=220)

tx=Entry(frame4,font=70,width=15).place(x=810,y=220)
lb=Label(frame4,text="Product Quantity",font=('arial',18,'bold')).place(x=590,y=290)
pq=StringVar()
tx=Entry(frame4,font=70,width=15,textvariable=pq).place(x=810,y=290)
lb=Label(frame4,text="Price Per Unit",font=('arial',18,'bold')).place(x=590,y=360)
pp=StringVar()
tx=Entry(frame4,font=70,width=15,textvariable=pp).place(x=810,y=360)
btn=Button(frame4,text="Confirm",font=('arial',15,'bold'),bd=5,relief="sunken",width=7,command=cart).place(x=730,y=450)
btn=Button(frame4,text="Total Amount to be Paid",font=('arial',15,'bold'),bd=5,relief="sunken",width=20,command=amount).place(x=650,y=550)


    
#CUSTOMER DETAILS
frame5=Frame(win,bd=10,relief="raised",width=368,height=450,bg="sky blue").place(x=1000,y=60)
frame6=Frame(win,bd=10,relief="raised",width=368,height=60).place(x=1000,y=60)
lb=Label(frame6,text="CUSTOMER DETAILS",font=('arial',18,'bold')).place(x=1080,y=70)
lb=Label(frame6,text="Order Date",font=('arial',18,'bold')).place(x=1045,y=160)
tx=Entry(frame6,font=70,width=15).place(x=1188,y=165)
lb=Label(frame6,text="Name",font=('arial',18,'bold')).place(x=1045,y=220)
tx=Entry(frame6,font=70,width=15).place(x=1188,y=225)
lb=Label(frame6,text="Phone No",font=('arial',18,'bold')).place(x=1045,y=280)
tx=Entry(frame6,font=70,width=15).place(x=1188,y=285)
lb=Label(frame6,text="Address",font=('arial',18,'bold')).place(x=1045,y=340)
tx=Entry(frame6,font=70,width=15).place(x=1188,y=345)
lb=Label(frame6,text="Email",font=('arial',18,'bold')).place(x=1045,y=400)
tx=Entry(frame6,font=70,width=15).place(x=1188,y=405)



frame9=Frame(win,bd=10,relief="raised",width=366,height=197,bg="sky blue").place(x=1000,y=510)
btn=Button(frame9,text="EXIT",font=('arial',20,'bold'),bd=5,relief="sunken",width=10,command=win.destroy).place(x=1090,y=570)


win.mainloop()
