import sqlite3
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("400x400")
fname = StringVar()
lname = StringVar()
password = StringVar()
confirmpassword = StringVar()
username=StringVar()
userpassword=StringVar()
db=sqlite3.connect("temp.db")
# db.execute("create table regist(firstname text,lastname text,password text,confirmpassword text)")
# db.commit()
def register():
    if(password.get()==confirmpassword.get()):
        db = sqlite3.connect("temp.db")
        db.execute("insert into regist values('" + fname.get() + "','" + lname.get() + "','" + password.get() + "','" + confirmpassword.get() + "')")
        db.commit()
        db.close()
    else:
        messagebox.showerror('password','password and confirm password does not match')
def login():
    db=sqlite3.connect("temp.db")
    cr=db.cursor()
    r=cr.execute(f"select * from regist where firstname='{username.get()}'and password='{userpassword.get()}'")
    db.commit()
    num=(len(r.fetchall()))
    print(num)
    if(num==1):
        messagebox.showinfo('password','successfully logged in ')
    else:
        messagebox.showerror('password','sorry password does not match')
def show(a):
    if(a=="login"):

        f1=Frame(root,bg="cyan",height=400,width=400)
        Button(f1, text="back",command=home).place(x=0,y=0)
        Label(f1,text="login",font="times 20 italic",bg="cyan").place(x=150,y=0)
        Label(f1, text="username", font="times 15 italic", bg="cyan").place(x=150, y=50)
        Entry(f1,textvariable=username).place(x=150,y=100)
        Label(f1, text="password", font="times 15 italic", bg="cyan").place(x=150, y=150)
        Entry(f1,textvariable=userpassword).place(x=150, y=200)
        Button(f1,text="login",command=login).place(x=150,y=300)
        f1.place(x=0,y=0)


    elif(a=="Register"):

        f3 = Frame(root, bg="cyan", height=400, width=400)
        Button(f3, text="back", command=home).place(x=0, y=0)
        l1 = Label(f3, text="Register", font="times 20 italic", bg="cyan").place(x=150, y=0)
        Label(f3,text="first name",font="times 15 italic",bg="cyan").place(x=150,y=50)
        Entry(f3,textvariable=fname).place(x=150, y=90)
        Label(f3, text="last name",font="times 15 italic", bg="cyan").place(x=150, y=130)
        Entry(f3,textvariable=lname).place(x=150, y=170)
        Label(f3, text="password",font="times 15 italic", bg="cyan").place(x=150, y=210)
        Entry(f3,textvariable=password).place(x=150, y=250)
        Label(f3, text="Confirm password", font="times 15 italic", bg="cyan").place(x=150, y=290)
        Entry(f3,textvariable=confirmpassword).place(x=150, y=330)
        Button(f3, text="Register",command=register).place(x=150, y=370)
        f3.place(x=0, y=0)


def home():
    f2 = Frame(root, bg="cyan", height=390, width=390)
    Button(root,text="login",command=lambda :show('login')).place(x=120,y=150)
    Button(root,text="Register",command=lambda :show('Register')).place(x=220,y=150)
    f2.place(x=0,y=0)
home()
root.mainloop()
