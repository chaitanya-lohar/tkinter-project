import sqlite3
from tkinter import *
root=Tk()
root.geometry("800x800")
l1=Label(root,text="enter name:")
l1.grid(row=0,column=0)
l1=Label(root,text="enter password:")
l1.grid(row=1,column=0)
x=StringVar()
y=StringVar()

db=sqlite3.connect("data1.db")
cr=db.cursor()

def show():
    # cr.execute("insert into login values('" + x.get() + "','" + y.get() + "')")
    r=cr.execute("select * from login")
    for r1 in r:
        print(r1)  #it returned tuple
        print(r1[0],r1[1])
    x.set("")
    y.set("")
    db.commit()
    db.close()
    print("connected")

e1=Entry(root,textvariable=x)
e1.grid(row=0,column=1)
e2=Entry(root,textvariable=y)
e2.grid(row=1,column=1)
b1=Button(root,text="click",command=show)
b1.grid(row=2,columnspan=2)

# x=input("enter your name:")
# number=input("enter your password")
 #cr(object) works as a intermediate
# cr.execute("create table login(uname text,upass text)")
root.mainloop()