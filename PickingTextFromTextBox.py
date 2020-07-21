from tkinter import *
from SR import *
root=Tk()
root.geometry("500x500")
x=StringVar
def show():
    # data=var.get()
    x.set(listening())

# f1=Frame(root,bg='grey',borderwidth=5,relief=GROOVE)
# f1.pack(side=LEFT)

e1=Entry(root, textvariable=x)
e1.pack()

b1=Button(root, text="Submit",bg="red",fg="white",command=show)
b1.pack()

root.mainloop()