# events of tkinter
from assistent import *
from tkinter import *
root=Tk()
# def show(a):
#     root.configure( background="lightblue")

# show=lambda a:root.configure( background="lightblue")

def show1(a):
    root.configure( background="blue")

def show2(a):
    root.configure( background="lightyellow")

root.geometry("700x700")
root.resizable(0,0)
root.title("")
b1=Button(root,text="Click",font="Arial 14 bold")
b1.bind("<Double-1>",lambda a:root.configure( background="lightblue"))  # left
# b1.bind("<Double-2>",show1) #wheel ("<Button-1>",show)
# b1.bind("<Double-3>",show2) #right
# b1.bind("<Enter>",show1)    # work on cursor move
# b1.bind("<Leave>",show2)
b1.bind("<Button>",show1)
b1.bind("<ButtonRelease>",show2)
b1.pack()
l1=Entry(root)
l1.bind("<FocusIn>",show1)
l1.pack()
l2=Entry(root)
l1.bind("<FocusOut>",show2)
l2.pack()
root.mainloop()