from tkinter import*
root=Tk()
root.geometry("700x700")
x=StringVar()
def func1():
    a=int(e1.get())
    # print(a)
    i=1
    fact=1
    while(i<=a):
        fact=fact*(i)

        i+=1
    print(fact)
    x.set(fact)

l1=Label(root,text="Enter any value:")
l1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)

l2=Label(root,text="Factorial is:")
l2.grid(row=1,column=0)
e2=Entry(root,textvariable=x)
e2.grid(row=1,column=1)
b1=Button(root,text="factorial")
b1.grid(row=2,columnspan=2)
b1.config(command=func1)
root.mainloop()