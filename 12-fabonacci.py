# 0,1,1,2,3,5,8,13,21
from tkinter import *
root=Tk()
root.geometry("700x700")
x=StringVar()

def func1():
    str1 = [0,1]
    a=0
    b=1
    n=int(e1.get())
    for i in range(1,n):
        c=a+b
        str1.append(c)

        # str1=str1+","+str(c)
        a=b
        b=c
    str1=str(str1)
    # str1.replace('['," ")
    x.set(str1)

l1=Label(root,text="enter any value:")
l1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
l2=Label(root,text="Fabonacci series:")
l2.grid(row=1,column=0)
e2=Entry(root,textvariable=x)
e2.grid(row=1,column=1)
b1=Button(root,text="Fabonacci")
b1.grid(row=2,columnspan=2)
b1.config(command=func1)
root.mainloop()