from tkinter import *
import math
root=Tk()
root.geometry("425x425")
root.configure(bg="black")
a=StringVar()


def show(c):
    global a
    a.set(a.get()+c)

def solve():
    a.set(eval(a.get()))     #eval can solve any expression





e1=Entry(root,font="Arial 30 bold",justify=RIGHT,textvariable=a)
e1.place(x=0,y=0,height=50,width=425)

b=[Button()]*16
data1=["7","8","9","+","4","5","6","-","1","2","3","*",".","0","/","="]
k=0
x=5
y=55
for i in range(4):
    for j in range(4):
        b[k] = Button(root, text=data1[k], font="Arial 25 bold", bg="grey", fg="white", activebackground="yellow",activeforeground="red")
        b[k].place(x=x,y=y,width=100,height=50)
        k=k+1
        x=x+105
    x=5
    y=y+55
#
# b1=Button(root,text="7",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b1.place(x=5,y=55,width=100,height=50)
# b1.config(command=lambda : show("7"))
#
# b2=Button(root,text="8",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b2.place(x=110,y=55,width=100,height=50)
# b2.config(command=lambda : show("8"))
#
# b3=Button(root,text="9",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b3.place(x=215,y=55,width=100,height=50)
# b3.config(command=lambda : show("9"))
#
# b4=Button(root,text="+",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b4.place(x=320,y=55,width=100,height=50)
# b4.config(command=lambda : show("+"))
#
#
# b5=Button(root,text="4",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b5.place(x=5,y=110,width=100,height=50)
# b5.config(command=lambda : show("4"))
#
# b6=Button(root,text="5",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b6.place(x=110,y=110,width=100,height=50)
# b6.config(command=lambda : show("5"))
#
# b7=Button(root,text="6",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b7.place(x=215,y=110,width=100,height=50)
# b7.config(command=lambda : show("6"))
#
# b8=Button(root,text="-",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b8.place(x=320,y=110,width=100,height=50)
# b8.config(command=lambda : show("-"))
#
#
# b9=Button(root,text="1",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b9.place(x=5,y=165,width=100,height=50)
# b9.config(command=lambda : show("1"))
#
# b10=Button(root,text="2",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b10.place(x=110,y=165,width=100,height=50)
# b10.config(command=lambda : show("2"))
#
# b11=Button(root,text="3",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b11.place(x=215,y=165,width=100,height=50)
# b11.config(command=lambda : show("3"))
#
# b12=Button(root,text="*",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b12.place(x=320,y=165,width=100,height=50)
# b12.config(command=lambda : show("*"))
#
#
# b13=Button(root,text=".",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b13.place(x=5,y=220,width=100,height=50)
# b13.config(command=lambda : show("."))
#
# b14=Button(root,text="0",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b14.place(x=110,y=220,width=100,height=50)
# b14.config(command=lambda : show("0"))
#
# b15=Button(root,text="/",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b15.place(x=215,y=220,width=100,height=50)
# b15.config(command=lambda : show("/"))
#
# b16=Button(root,text="=",font="Arial 25 bold",bg="grey",fg="white",activebackground="yellow",activeforeground="red")
# b16.place(x=320,y=220,width=100,height=50)
# b16.config(command=solve)
#
#

root.mainloop()