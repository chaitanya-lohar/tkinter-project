from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x700")
# x=IntVar()
# y=IntVar()
# z=IntVar()
# a=StringVar()
# def show():
#     x1=""
#     if(x.get()==1):
#         x1=x1+"python "
#     if (y.get() == 1):
#         x1 = x1 + "Java "
#     if (z.get() == 1):
#         x1 = x1 + "C++ "
#     a.set(x1)
#
# c1=Checkbutton(root,text="python",font="times 20 italic",padx=10,pady=10,variable=x,command=show)
# c1.pack()
# c1=Checkbutton(root,text="java",font="times 20 italic",padx=10,pady=10,variable=y,command=show)
# c1.pack()
# c1=Checkbutton(root,text="c++",font="times 20 italic",padx=10,pady=10,variable=z,command=show)
# c1.pack()
# e1=Entry(root,textvariable=a)
# e1.pack()
#------------------------------------------------------------------------------------------------
# from tkinter import ttk
#
# n=ttk.Notebook()
# n.place(x=0,y=0,height=700,width=700)
# f1=Frame(bg="cyan")
# n.add(f1,text="file")
# f2=Frame(bg="lightgreen")
# n.add(f2,text="Edit")
#--------------------------------------------------------------------------------------------------


# x=StringVar()
# def show():
#      messagebox.showinfo("alert",f" you selected {x.get()} in spinbox")
#
#
# s=Spinbox(root,value=["chetan","rajesh","yamini","komal"],textvariable=x,font="times 20 italic")
# s.pack()
# b1=Button(root,text="select",command=show)
# b1.pack()
#---------------------------------------------------------------------------------------
# scale
x=IntVar()
def show(a):
    x.get()
    messagebox.showinfo("scale",f"{x.get()}")


myslider1=Scale(root,from_=0, to_= 100,tickinterval=0,orient=VERTICAL,variable=x)
myslider1.set(20)
myslider1.pack()
myslider1.bind("<ButtonRelease>",show)









root.mainloop()