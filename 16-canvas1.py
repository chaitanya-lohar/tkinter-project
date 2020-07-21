from tkinter import*
root=Tk()
# x=IntVar()
# y=IntVar()
# def func1():
#     h = x.get()
#     w = y.get()
#     root.geometry(f"{h}x{w}")
# e1=Entry(root,textvariable=x)
# e1.pack()
# e2=Entry(root,textvariable=y)
# e2.pack()
#
# b1=Button(root,command=func1)
# b1.pack()

c1=Canvas(root,width=150,height=150,bg="red")
c1.pack()
# c1.create_line(10,10,10,100,fill="white")
# c1.create_line(10,10,100,10,fill="white")
# c1.create_line(100,10,100,100,fill="white")
# c1.create_line(10,100,100,100,fill="white")
# c1.create_line(10,10,100,100,fill="white")
# c1.create_line(10,100,100,10,fill="white")
c1.create_rectangle(10,10,100,100,fill="green")

c1.create_text(20,50,text="name")
c1.create_oval(0,0,150,100,fill="white")
root.mainloop()