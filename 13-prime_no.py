
from tkinter import *
root=Tk()
root.geometry("700x700")
x=StringVar()
def func1():
    n=int(e1.get())
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1

    if(count==2):
        x.set(f"Yes,{n} is Prime number")
    else:
        x.set(f"No,{n} is not Prime number")

l1=Label(root,text="enter any value:")
l1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
l2=Label(root,text="Prime number is:")
l2.grid(row=1,column=0)
e2=Entry(root,textvariable=x)
e2.grid(row=1,column=1)
b1=Button(root,text="Prime")
b1.grid(row=2,columnspan=2)
b1.config(command=func1)
root.mainloop()