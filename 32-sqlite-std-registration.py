import sqlite3
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("800x800")
root.resizable(0,0)
x1=IntVar()
s=StringVar()
variable=StringVar()
db=sqlite3.connect("stdregistration.db")
# cr=db.cursor()
def fun1():
    # db.execute("create table std(name text,father text,addr text,sex text,state text,city text,pin number,course text,mobile number,id text)")
    # db.commit()
    # db.close()
    db = sqlite3.connect("stdregistration.db")
    x=""
    if(x1.get()==1):
       x="Male"
    if(x1.get()==2):
        x="Female"
    if(x1.get()==3):
        x="trangender"
    db.execute("insert into std (name,father,addr,sex,state,city,pin,course,mobile,id) values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"','"+x+"','"+s.get()+"','"+e4.get()+"',"+e5.get()+",'"+variable.get()+"',"+e6.get()+",'"+e7.get()+"')")
    db.commit()
    db.close()
    messagebox.showinfo("tkinter","data inserted......")
def fun2():
    db = sqlite3.connect("stdregistration.db")
    r=db.execute(f"select * from std where name='{E.get()}'")
    db.commit()
    for data in r:
        print(f"name:{data[0]}\n father name:{data[1]}\n address:{data[2]}\n Sex:{data[3]}\n State:{data[4]}\n City:{data[5]}\n Pincode:{data[6]}\n Course:{data[7]}\n Mobile number:{data[8]}\nEmail id{data[9]}\n")
        print("----------------------------------------------------------")
    messagebox.showinfo("tkinter", "data fetched......")
E=StringVar()
def fun3():
    db = sqlite3.connect("stdregistration.db")
    db.execute(f"delete from std where name='{E.get()}'")
    db.commit()
    db.close()
    messagebox.showinfo("tkinter", f"Entry deleted from database of name:{E.get()}......")
    E.set("")

E1 = StringVar()
E2 = StringVar()
E3 = StringVar()
E4 = IntVar()
E5 = IntVar()
E6 = StringVar()
def fun4():

    db=sqlite3.connect("stdregistration.db")
    db.execute("update std set father='"+e2.get()+"',addr='"+e3.get()+"',state='"+s.get()+"',city='"+e4.get()+"',pin="+e5.get()+",course='"+variable.get()+"',mobile="+e6.get()+",id='"+e7.get()+"' where name='"+E.get()+"'")
    db.commit()
    db.close()
    messagebox.showinfo("tkinter", f"Entry updated of name:{E.get()}......")
    E.set("")
    E1.set("")
    E2.set("")
    s.set("")
    E3.set("")
    E4.set("")
    E5.set("")
    E6.set("")

l11=Label(root,text="Student Registration Form",font="times 20 italic")
l11.grid(row=0,columnspan=2)
l1=Label(root,text="Name",padx=5,pady=5,font="times 15 italic")
l1.grid(row=1,column=0)
e1=Entry(root,textvariable=E)
e1.grid(row=1,column=1)
l2=Label(root,text="Father's Name",padx=5,pady=5,font="times 15 italic")
l2.grid(row=2,column=0)
e2=Entry(root,textvariable=E1)
e2.grid(row=2,column=1)
l3=Label(root,text="Address",padx=5,pady=5,font="times 15 italic")
l3.grid(row=3,column=0)
e3=Entry(root,textvariable=E2)
e3.grid(row=3,column=1)
l4=Label(root,text="Sex",font="times 15 italic",padx=5,pady=5)
l4.grid(row=4,column=0)
r1=Radiobutton(root,text="Male",variable=x1,value=1,font="times 15 italic")
r1.grid(row=4,column=1)
r2=Radiobutton(root,text="Female",variable=x1,value=2,font="times 15 italic")
r2.grid(row=4,column=2)
r3=Radiobutton(root,text="Transgender",variable=x1,value=3,font="times 15 italic")
r3.grid(row=4,column=3)
l5=Label(root,text="State",font="times 15 italic",padx=5,pady=5)
l5.grid(row=5,column=0)
s1=Spinbox(root,values=["Rajasthan","MP","UP","MH"],textvariable=s,font="times 15 italic")
s1.grid(row=5,column=1)
l6=Label(root,text="City Name",font="times 15 italic",padx=5,pady=5)
l6.grid(row=6,column=0)
e4=Entry(root,textvariable=E3)
e4.grid(row=6,column=1)
l7=Label(root,text="Pincode",font="times 15 italic",padx=5,pady=5)
l7.grid(row=7,column=0)
e5=Entry(root,textvariable=E4)
e5.grid(row=7,column=1)
l8=Label(root,text="Course",font="times 15 italic",padx=5,pady=5)
l8.grid(row=8,column=0)
option=["BCA","MCA","B.tech","M.tech","Diploma CS"]
variable.set(option[0])

d1=OptionMenu(root,variable,*option)
d1.grid(row=8,column=1)
l9=Label(root,text="Mobile",font="times 15 italic",padx=5,pady=5)
l9.grid(row=9,column=0)
e6=Entry(root,textvariable=E5)
e6.grid(row=9,column=1)
l10=Label(root,text="Email ID",font="times 15 italic",padx=5,pady=5)
l10.grid(row=10,column=0)
e7=Entry(root,textvariable=E6)
e7.grid(row=10,column=1)
b1=Button(root,text="Insert",font="times 15 italic",bg="black",fg="white",padx=5,pady=5)
b1.grid(row=11,column=0)
b1.config(command=fun1)

b2=Button(root,text="Fetch",font="times 15 italic",bg="black",fg="white",padx=5,pady=5)
b2.grid(row=11,column=1)
b2.config(command=fun2)

b3=Button(root,text="Delete",font="times 15 italic",bg="black",fg="red",padx=5,pady=5,activebackground="red")
b3.grid(row=11,column=2)
b3.config(command=fun3)

b4=Button(root,text="Update",font="times 15 italic",bg="black",fg="white",padx=5,pady=5)
b4.grid(row=11,column=3)
b4.config(command=fun4)


root.mainloop()