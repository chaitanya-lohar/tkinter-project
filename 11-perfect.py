from tkinter import *
root=Tk()
root.geometry("700x700")
x=StringVar()
def func1():
    a=int(e1.get())
    sum=0
    for i in range(1,a):
        if(a%i==0):
            sum=sum+i
    if(sum==a):
        x.set(f"perfect number:{a}")
    else:
        x.set(f"Not perfect:{a}")


l1=Label(root,text="enter any value:")
l1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
l2=Label(root,text="Perfect number is:")
l2.grid(row=1,column=0)
e2=Entry(root,textvariable=x)
e2.grid(row=1,column=1)
b1=Button(root,text="Perfect")
b1.grid(row=2,columnspan=2)
b1.config(command=func1)


root.mainloop()