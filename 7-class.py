from tkinter import *
root=Tk()
root.geometry('700x700')
def func1(a):
    print("my name is chetan")

f1=Frame(root,bg="lightblue",borderwidth=5,relief=GROOVE)
f1.pack(side=LEFT)
# b1=Button(f1,text="submit",bg="red",fg="white" ,command=func1)
b1=Button(f1,text="submit",bg="red",fg="white")
# b1.config(command=func1)
b1.pack()
b1.bind("<Button-1>",func1)
root.mainloop()