from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
root=Tk()
root.geometry("800x800")
root.resizable(0,0)
n=ttk.Notebook()
n.place(x=0,y=0,height=800,width=800)
f1=Frame(bg="lightblue")
n.add(f1,text="login")
# f1.pack()
# db = sqlite3.connect("logg.db")
# cr = db.cursor()
# cr.execute("create table log(uname text,upassword text)")

def show():

    # cr.execute("insert into log values('"+e1.get()+"','"+e2.get()+"')")
    # print(f"{e1.get()},{e2.get()}")
    db = sqlite3.connect("logg.db")
    cr = db.cursor()

    data=cr.execute("select * from log")
    for da in data:
        if(da[0]==e1.get() and da[1]==e2.get()):
            messagebox.showinfo("login","you successfully logged in")
        else:
            messagebox.showinfo("login", "sorry wrong name and password")
    db.commit()
    db.close()
    f2 = Frame(bg="lightblue")
    n.add(f2, text="Student Registration")
    m1 = Label(f2, text="Student name:")
    m1.place(x=10, y=10)
    E1 = Entry(f2)
    E1.place(x=50, y=10)


l1=Label(f1="Login Form",font="times 20 italic",bg="lightblue")
l1.grid(row=0,columnspan=2)
l2=Label(f1,text="Enter your name:",font="times 15 italic",bg="lightblue")
l2.grid(row=1,column=0)
l3=Label(f1,text="Enter your password:",font="times 15 italic",bg="lightblue")
l3.grid(row=2,column=0)
e1=Entry(f1)
e1.grid(row=1,column=1)
e2=Entry(f1)
e2.grid(row=2,column=1,pady=10)
b1=Button(f1,text="login",font="times 15 italic")
b1.grid(row=3,columnspan=2)
b1.config(command=show)



root.mainloop()