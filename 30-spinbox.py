from tkinter import *
root=Tk()
root.geometry("800x800")
x=StringVar()
y=IntVar()
def show1():
    # root.configure(bg=x.get())
    y.set(f"you have selected{x.get()}")
s1=Spinbox(root,font="Arial 15 bold",textvariable=x,from_=1,to=10,command=show1)
s1.pack()
# ,values=["red","blue","green","white","black"]
# b1=Button(root,text="color change",command=show1)
# b1.pack()
l1=Label(root,textvariable=y)
l1.pack()

root.mainloop()