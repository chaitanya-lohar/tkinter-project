from tkinter import *
root=Tk()
root.geometry("800x800")
# s=StringVar()
x=StringVar()
x1=IntVar()
x2=IntVar()
x3=IntVar()
x4=IntVar()
def show1():
    s1=""
    if(x1.get()==1):
        s1=s1+"Python "
    if (x2.get() == 1):
        s1 = s1 + "java "
    if (x3.get() == 1):
        s1 = s1 + "php "
    if (x4.get() == 1):
        s1 = s1 + "C++"
    x.set(s1)
c1=Checkbutton(root,text="Python",font="times 20 italic",padx=10,variable=x1,command=show1)
c1.pack()
c2=Checkbutton(root,text="Java",font="times 20 italic",padx=10,variable=x2,command=show1)
c2.pack()
c3=Checkbutton(root,text="PHP",font="times 20 italic",padx=10,variable=x3,command=show1)
c3.pack()
c4=Checkbutton(root,text="C++",font="times 20 italic",padx=10,variable=x4,command=show1)
c4.pack()
# b1=Button(root,text="select")
# b1.pack()
# b1.config(command=show1)
e1=Entry(root,textvariable=x)
e1.pack()


root.mainloop()