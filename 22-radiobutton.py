from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x700")
root.resizable(0,0)
var1=StringVar()
var1.set("Radio")
def fun1():
    messagebox.showinfo("order received",f"we have received your order for {var1.get()}")


l1=Label(root,text="what would you like to have ?",font="times 20 italic",padx=15,justify="left")
l1.pack()
r1=Radiobutton(root,text="Coffee",padx=15,value="Coffee1",variable=var1)
r1.pack(anchor="w")
e1=Entry(root)
e1.pack()
r1=Radiobutton(root,text="Tea",padx=15,value="Tea",variable=var1)
r1.pack(anchor="w")
r1=Radiobutton(root,text="Juice",padx=15,value="Juice",variable=var1)
r1.pack(anchor="w")
r1=Radiobutton(root,text="Water",padx=15,value="Water",variable=var1)
r1.pack(anchor="w")

b1=Button(root,text="order now",command=fun1)
b1.pack()
root.mainloop()