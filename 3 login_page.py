# three methods to apply tools on form
# 1. pack()
# 2. grid()
# 3. place()


from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("Login Page")
def fun():
    root.configure(bg="lightblue")
    messagebox.showinfo("hello,this is example of button")

# def fun1():
#     root.configure(bg="lightgreen")

def fun2():
    root.configure(bg="lightyellow")
l1=Label(root,text="Enter your name:",font="Arial 14")
l1.grid(row=0,column=0 ,padx=50,pady=10)
e1=Entry(root)
e1.grid(row=0,column=1)
l2=Label(root,text="Enter password:",font="Arial 14")
l2.grid(row=1,column=0)
e2=Entry(root,show="*")
e2.grid(row=1,column=1,pady=20)
b1=Button(root,text="submit",width=10,height=2)
# b2=Button(root,text="submit",width=10,height=2,command=fun1)
# b3=Button(root,text="submit",width=10,height=2,command=fun2)
# b3.grid(row=2,column=2)
# b1.grid(row=2,column=0)
# b2.grid(row=2,column=1)
b1.config(command=fun)
b1.place(x=100,y=100)
# b2.place(x=100,y=200)
# b3.place(x=100,y=300)


root.mainloop()
