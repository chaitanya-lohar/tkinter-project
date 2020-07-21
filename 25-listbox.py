from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x700")
def add():
    l1.insert(ACTIVE,e1.get())
    p=l1.size()
    messagebox.showinfo("itmes",f"items count:{p}")
def DELETE():
    l1.delete(ACTIVE)
    l1.
    # l1.deletecommand(e1.get())
l1=Listbox(root)
l1.pack()
e1=Entry(root)
e1.pack()
b1=Button(root,text="add item",command=add)
b1.pack()
b2=Button(root,text="delete item",command=DELETE)
b2.pack()


root.mainloop()