from tkinter import *
from tkinter import ttk
root=Tk()

root.geometry("800x800")
n=ttk.Notebook()
n.place(x=0,y=0,height=800,width=800)
f1=Frame(bg="cyan")
n.add(f1,text="Insert")
# b1=Button(f1,text="submit1")
# b1.pack()
l1=Label(f1,text="enter your name:",bg="cyan")
l1.grid(row=0,column=0)
e1=Entry(f1)
e1.grid(row=0,column=1)
l2=Label(f1,text="enter your contact number:",bg="cyan")
l2.grid(row=1,column=0)
e2=Entry(f1)
e2.grid(row=1,column=1)
b1=Button(f1,text="submit1")
b1.grid(row=2,columnspan=2)

f2=Frame(bg="lightblue")
n.add(f2,text="Search")
b2=Button(f2,text="submit2")
b2.pack()

f3=Frame(bg="green")
n.add(f3,text="Show all")
b3=Button(f3,text="submit3")
b3.pack()



root.mainloop()