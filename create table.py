import sqlite3

def create_db():
    con = sqlite3.connect(database=r'stock.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS login(username text, password text)')
    con.commit()
    cur.execute("insert into login values('admin','admin')")
    cur.execute('CREATE TABLE IF NOT EXISTS stock( product_id int,name text,quantity text, price text)')
    con.commit()
    con.close()


create_db()
con = sqlite3.connect(database=r'stock.db')
cur = con.cursor()
cur.execute("select * from stock")
res=cur.fetchall()
if len(res)==0:
    create_db()
else:
    print("Already exist")

    
