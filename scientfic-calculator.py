from tkinter import *
# from tkinter import messagebox
from math import *
root=Tk()
root.geometry("425x500")
root.title("Calculator")
root.resizable(0,0)
root.configure(bg="black")
a=StringVar()
def show(b):
    a.set(a.get()+b)

def clearall(r):
    a.set("")
def clear1(r):
    num = a.get()
    num = list(num)
    num.pop()
    str1 = ""
    a.set(str1.join(num))
def ans():
    data=a.get()
    a.set(eval(data))


e1=Entry(root,font="Arial 25 bold",justify="right",textvariable=a)
e1.place(x=5,y=5,width=415,height=40)

b1=Button(root,text="sin",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("sin"))
b1.place(x=5,y=50,width=100,height=50)
b2=Button(root,text="cos",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("cos"))
b2.place(x=110,y=50,width=100,height=50)
b3=Button(root,text="tan",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("tan"))
b3.place(x=215,y=50,width=100,height=50)
b4=Button(root,text="In",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("In"))
b4.place(x=320,y=50,width=100,height=50)

b5=Button(root,text="log",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("log"))
b5.place(x=5,y=105,width=100,height=50)
b6=Button(root,text="√",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("√"))
b6.place(x=110,y=105,width=100,height=50)
b7=Button(root,text="π",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("π"))
b7.place(x=215,y=105,width=100,height=50)
b8=Button(root,text="e",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("e"))
b8.place(x=320,y=105,width=100,height=50)

b9=Button(root,text="1",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("1"))
b9.place(x=5,y=160,width=100,height=50)
b10=Button(root,text="2",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("2"))
b10.place(x=110,y=160,width=100,height=50)
b11=Button(root,text="3",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("3"))
b11.place(x=215,y=160,width=100,height=50)
b12=Button(root,text="4",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("4"))
b12.place(x=320,y=160,width=100,height=50)

b13=Button(root,text="5",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("5"))
b13.place(x=5,y=215,width=100,height=50)
b14=Button(root,text="6",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("6"))
b14.place(x=110,y=215,width=100,height=50)
b15=Button(root,text="7",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("7"))
b15.place(x=215,y=215,width=100,height=50)
b16=Button(root,text="8",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("8"))
b16.place(x=320,y=215,width=100,height=50)
b18=Button(root,text="9",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("9"))
b18.place(x=5,y=270,width=100,height=50)
b19=Button(root,text="0",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("0"))
b19.place(x=110,y=270,width=100,height=50)
b20=Button(root,text="(",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show("("))
b20.place(x=215,y=270,width=100,height=50)
b21=Button(root,text=")",font="Arial 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="black",command=lambda :show(")"))
b21.place(x=320,y=270,width=100,height=50)



b17=Button(root,text="CLEAR",font="Algerian 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="darkred")
b17.place(x=5,y=325,width=415,height=50)
b17.bind("<Button-3>",clearall)
b17.bind("<Button-1>",clear1)
b22=Button(root,text="Solution",font="Algerian 20 bold",bg="gray",fg="white",activebackground="darkgray",activeforeground="darkred")
b22.place(x=5,y=380,width=415,height=50)
b22.config(command=ans)

root.mainloop()