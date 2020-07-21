from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("700x700")
db=sqlite3.connect("stddatabase.db")
cr=db.cursor()
# cr.execute("create table stddata(firstname text,lastname text, password text, confirmpassword text)")
# db.commit()
# db.close()
firstname1=StringVar()
lastname1=StringVar()
password1=StringVar()
confirmpassword1=StringVar()

names=StringVar()
passwords=StringVar()

fullname=StringVar()
mobnumber=StringVar()
addr=StringVar()
schoolname=StringVar()

def show(a):
    if(a=="login"):
        f1=Frame(root,bg="lightblue")
        f1.place(x=0,y=0,height=700,width=700)
        Button(f1, text="back", font="times 15 italic",command=back).place(x=0, y=0)
        Label(f1,text="username",font="times 15 italic",bg="lightblue").place(x=100,y=100)
        Entry(f1,textvariable=names).place(x=300,y=100)
        Label(f1, text="userpassword",font="times 15 italic",bg="lightblue").place(x=100, y=150)
        Entry(f1,textvariable=passwords).place(x=300, y=150)
        Button(f1,text="login",font="times 15 italic",command=log).place(x=300,y=200)

    elif(a=="signup"):
        f2=Frame(root,bg="cyan")
        f2.place(x=0,y=0,height=700,width=700)
        f1 = Frame(root, bg="lightblue")
        f1.place(x=0, y=0, height=700, width=700)
        Button(f1, text="back", font="times 15 italic", command=back).place(x=0, y=0)
        Label(f1, text="first name", font="times 15 italic", bg="lightblue").place(x=100, y=100)
        Entry(f1,textvariable=firstname1).place(x=300, y=100)
        Label(f1, text="last name", font="times 15 italic", bg="lightblue").place(x=100, y=150)
        Entry(f1,textvariable=lastname1).place(x=300, y=150)
        Label(f1, text="password", font="times 15 italic", bg="lightblue").place(x=100, y=200)
        Entry(f1,textvariable=password1).place(x=300, y=200)
        Label(f1, text="confirm password", font="times 15 italic", bg="lightblue").place(x=100, y=250)
        Entry(f1,textvariable=confirmpassword1).place(x=300, y=250)

        Button(f1, text="Sign up", font="times 15 italic",command=sign).place(x=300, y=300)

def log():
    db = sqlite3.connect("stddatabase.db")
    cr = db.cursor()
    r=cr.execute(f"select * from stddata where firstname='{names.get()}' and password='{passwords.get()}'")
    db.commit()
    names.set("")
    passwords.set("")
    print("login")
    num=len(r.fetchall())
    if(num==1):
        f3=Frame(root,bg='cyan')
        f3.place(x=0,y=0,height=700,width=700)
        b1=Button(f3,text="logout",command=back).place(x=590,y=5)
        l1=Label(f3,text="Student Registration",font="times 20 italic",bg="cyan")
        l1.place(x=200,y=100)
        Label(f3,text="full name:",font="times 15 italic",bg="cyan").place(x=150,y=150)
        Entry(f3,textvariable=fullname).place(x=300,y=150)
        Label(f3, text="mobile number:",font="times 15 italic",bg="cyan").place(x=150, y=200)
        Entry(f3, textvariable=mobnumber).place(x=300, y=200)
        Label(f3, text="address:",font="times 15 italic",bg="cyan").place(x=150, y=250)
        Entry(f3, textvariable=addr).place(x=300, y=250)
        Label(f3, text="SchoolName:",font="times 15 italic",bg="cyan").place(x=150, y=300)
        Entry(f3, textvariable=schoolname).place(x=300, y=300)
        Button(f3,text="Submit",font="times 15 bold",bg="gray",fg="black",command=stddetails).place(x=200,y=400)

        Button(f3,text="export",font="times 15 bold",bg="gray",fg="black",command=fetch).place(x=300,y=400)
        Button(f3,text="fetch by name",font="times 15 bold",bg="gray",fg="black",command=fetchbyname).place(x=400,y=400)
        Button(f3,text="update",font="times 15 bold",bg="gray",fg="black",command=update).place(x=550,y=400)
        Button(f3,text="delete",font="times 15 bold",bg="gray",fg="black",command=deleted).place(x=200,y=500)
        # Button(f3,text="pending",font="times 15 bold",bg="gray",fg="black",command=update).place(x=550,y=400)


    else:
        messagebox.showerror("password","username and password doesn't match")

    db.close()

def deleted():
    db = sqlite3.connect("studentdetail.db")
    cr = db.cursor()
    # if(fullname.get()=="",mobnumber.get()=="",addr.get()=="",schoolname.get()==""):
    #     messagebox.showwarning("warning",f"please enter student name whose entery you want to delete1")
    # else:
    cr.execute(f"delete from stddetail where fullname='{fullname.get()}'")
    db.commit()
    db.close()
    messagebox.showinfo("delete",f"Entry deleted by name{fullname.get()}")
    fullname.set("")
    mobnumber.set("")
    addr.set("")
    schoolname.set("")

def fetch():
    f4=Frame(root,bg="cyan").place(x=0,y=0,height=700,width=700)
    b1=Button(f4,text="logout",command=back).place(x=590,y=5)
    db = sqlite3.connect("studentdetail.db")
    cr = db.cursor()
    Label(f4,text="full name     mobile number          address          schoolname",font="times 15 bold",bg="cyan").place(x=100,y=50)
    r=cr.execute("select * from stddetail")
    db.commit()
    n=100
    m=100
    for data in r:
        Label(f4,text=f"{data[0]}         {data[1]}            {data[2]}            {data[3]}",font="times 15 italic",bg="cyan").place(x=n,y=m)
        m+=50
    db.close()
def fetchbyname():
     db = sqlite3.connect("studentdetail.db")
     cr=db.cursor()
     r=cr.execute(f"select * from stddetail where fullname='{fullname.get()}'")
     db.commit()
     for data in r:
         fullname.set(data[0])
         mobnumber.set(data[1])
         addr.set(data[2])
         schoolname.set(data[3])

def update():
         db = sqlite3.connect("studentdetail.db")
         cr=db.cursor()
         r=cr.execute("update stddetail set fullname='"+fullname.get()+"',mobnumber='"+mobnumber.get()+"',addr='"+addr.get()+"',schoolname='"+schoolname.get()+"'")
         db.commit()
         db.close() 
         fullname.set("")
         mobnumber.set("")
         addr.set("")
         schoolname.set("")
         messagebox.showinfo("Entry","student database updated...")
def stddetails():
    db=sqlite3.connect("studentdetail.db")
    cr=db.cursor()
    # cr.execute("create table stddetail(fullname text,mobnumber text,addr text,schoolname text)")
    # db.commit()
    if(fullname.get()=="" and mobnumber.get()=="" and addr.get()=="" and schoolname.get()==""):
        messagebox.showwarning("warning","please fill all entries..")
    else:
        cr.execute(f"insert into stddetail (fullname,mobnumber,addr,schoolname)values('"+fullname.get()+"','"+mobnumber.get()+"','"+addr.get()+"','"+schoolname.get()+"')")
        db.commit()
        messagebox.showinfo("entry","your data has been saved..")
        fullname.set("")
        mobnumber.set("")
        addr.set("")
        schoolname.set("")




def sign():
    if(password1.get()==confirmpassword1.get()):
        cr.execute(f"insert into stddata (firstname,lastname,password,confirmpassword) values('"+firstname1.get()+"','"+lastname1.get()+"','"+password1.get()+"','"+confirmpassword1.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo("password","data inserted.....")
        firstname1.set("")
        lastname1.set("")
        confirmpassword1.set("")
        password1.set("")
    else:
        messagebox.showerror("error","password and confirm password doesn't match")
def back():
    f2=Frame(root,height=700,width=700,bg="cyan")
    Label(root,text="Login and Sign-Up page",font="times 20 italic",bg="cyan").place(x=200,y=50)
    Button(root,text="login",command=lambda :show("login"),bg="black",fg="red",activebackground="red",font="times 15 italic").place(x=200,y=400)
    Button(root,text="Sign up",command=lambda :show("signup"),bg="black",fg="red",activebackground="red",font="times 15 italic").place(x=400,y=400)
    f2.place(x=0,y=0)
back()
root.configure(bg="lightblue")

root.mainloop()