from tkinter import*
from tkinter import messagebox
import sqlite3
import pymysql.cursors
import os

 
def up():
    os.system("change.py")

    
win= Tk()

win.geometry("1359x720")

win.resizable(False,False)

win.title("ADMIN PAGE")


frame=Frame(win,bd=10,relief="raised",width=1365,height=80,bg="grey").grid(row=0)

lb=Label(frame,text="INVENTORY MANAGEMENT SYSTEM",font=('arial',20,'bold'),bg="grey").grid(row=0)

frame2=Frame(win,bd=10,relief="raised",width=800,height=300,bg="sky blue").place(x=0,y=80)

frame10=Frame(win,bd=10,relief="raised",width=800,height=60).place(x=0,y=80)

lb=Label(frame10,text="AVAILABLE ITEMS",font=('arial',18,'bold')).place(x=300,y=90)



#delete item
def delete():
    conn=sqlite3.connect(database=r'stock.db')
    mycursor=conn.cursor()
    try:

        mycursor.execute("delete from stock where product_id ='"+de.get()+"'")
        conn.commit()
        messagebox.showinfo("Message","Deleted")
    except:
        messagebox.showerror("Message","Product Not Deleted")
    conn.close()                    
                           
frame3=Frame(win,bd=10,relief="raised",width=565,height=300,bg="sky blue").place(x=800,y=80)

frame9=Frame(win,bd=10,relief="raised",width=565,height=60).place(x=800,y=80)

lb=Label(frame9,text="DELETE ITEM",font=('arial',18,'bold')).place(x=1020,y=90)

lb=Label(frame9,text="Product Code",font=('arial',18,'bold')).place(x=950,y=200)
de=StringVar()
tx=Entry(frame9,font=100,width=15,textvariable=de).place(x=1140,y=205)

btn=Button(frame9,text="DELETE ITEM",font=('arial',13,'bold'),bd=5,relief="sunken",width=15,command=delete).place(x=1030,y=270)

#add item
def add():
    conn=sqlite3.connect(database=r'stock.db')
    mycursor=conn.cursor()
 
    try:
        
        mycursor.execute("insert into stock(product_id,name,quantity,price) values('"+pc.get()+"','"+pn.get()+"','"+pq.get()+"','"+pp.get()+"')")
        conn.commit()
        messagebox.showinfo("Message","Submitted")
    except:
        messagebox.showerror("Message","Not Submitted")
    conn.close()                    
                         
frame4=Frame(win,bd=10,relief="raised",width=480,height=325,bg="sky blue").place(x=0,y=380)

frame7=Frame(win,bd=10,relief="raised",width=480,height=60).place(x=0,y=380)

lb=Label(frame7,text="ADD NEW ITEM",font=('arial',18,'bold')).place(x=150,y=390)

lb=Label(frame7,text="Product Code",font=('arial',18,'bold')).place(x=55,y=460)

pc=StringVar()
tx=Entry(frame7,font=70,width=15,textvariable=pc).place(x=300,y=463)

lb=Label(frame7,text="Product Name",font=('arial',18,'bold')).place(x=55,y=500)
pn=StringVar()
tx1=Entry(frame7,font=70,width=15,textvariable=pn).place(x=300,y=503)

lb=Label(frame7,text="Product Quantity",font=('arial',18,'bold')).place(x=55,y=540)
pq=StringVar()
tx2=Entry(frame7,font=70,width=15,textvariable=pq).place(x=300,y=543)

lb=Label(frame7,text="Product Price",font=('arial',18,'bold')).place(x=55,y=580)
pp=StringVar()
tx3=Entry(frame7,font=70,width=15,textvariable=pp).place(x=300,y=585)

btn=Button(frame7,text="SUBMIT",command=add,font=('arial',15,'bold'),bd=5,relief="sunken",width=15).place(x=150,y=640)


#update item
def update():
    #f=code.get()
    #g=np.get()
    conn=sqlite3.connect(database=r'stock.db')
    mycursor=conn.cursor()
    try:
        mycursor.execute("update stock set price='"+np.get()+"' where  product_id='"+code.get()+"'")
        conn.commit()
        messagebox.showinfo("Message","Price Updated")
    except:
        messagebox.showerror("Message","Price Not Updating")
    conn.close()
frame5=Frame(win,bd=10,relief="raised",width=480,height=325,bg="sky blue").place(x=480,y=380)

frame8=Frame(win,bd=10,relief="raised",width=480,height=60).place(x=480,y=380)

lb=Label(frame8,text="UPDATE PRICE",font=('arial',18,'bold')).place(x=630,y=390)

lb=Label(frame7,text="Product Code",font=('arial',18,'bold')).place(x=550,y=480)
code=StringVar()
tx=Entry(frame7,font=90,width=15,textvariable=code).place(x=750,y=483)

lb=Label(frame7,text="New Price",font=('arial',18,'bold')).place(x=550,y=550)
np=StringVar()
tx=Entry(frame7,font=90,width=15,textvariable=np).place(x=750,y=553)

btn=Button(frame7,text="SUBMIT",font=('arial',15,'bold'),bd=5,command=update,relief="sunken",width=15).place(x=610,y=630)

 

frame6=Frame(win,bd=10,relief="raised",width=405,height=325,bg="sky blue").place(x=960,y=380)

btn=Button(frame6,text="Change Password",command=up,font=('arial',20,'bold'),bd=5,relief="sunken",width=15).place(x=1020,y=450)

btn=Button(frame6,text="Log out",font=('arial',20,'bold'),bd=5,relief="sunken",width=10,command=win.destroy).place(x=1070,y=550)

#textarea for the items

def data():
    
    conn = sqlite3.connect(database=r'stock.db')
    mydb=conn.cursor()
    mydb.execute("select * from stock")
    result=mydb.fetchall()
    count=mydb.rowcount
    print(result)
    print(count)
    num=20
    tx=Text(frame10,font="vendata 15",width=50,height=8)
    tx.insert(END,"\n\tCode\tName\tQuantity\tPrice")
    tx.place(x=num,y=150)
    for i in result:
        tx.insert(END,"\n\t{0}\t{1}\t{2}\t{3}".format(i[0],i[1],i[2],i[3]))
        num+=1
    
#List
btn4=Button(frame10,text="REFRESH",command=data,font=('arial',15,'bold'),bd=5,relief="raised",width=15).place(x=580,y=220)

   
win.mainloop()
