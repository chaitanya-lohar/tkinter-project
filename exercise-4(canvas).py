from tkinter import *
root=Tk()
# def show():
#
#     root.geometry(f"{e1.get()}x{e2.get()}")

# e1=Entry(root)
# e1.grid(row=0,column=0)
# e2=Entry(root)
# e2.grid(row=1,column=0)
# b1=Button(root,text="submit",command=show)
# b1.grid(row=3,column=0)
root.geometry("700x700")
c1=Canvas(root,bg="lightblue",width=700,height=700)
c1.pack()
# c1.create_line(100,10,100,100,fill="white")
# c1.create_line(200,10,200,100,fill="white")
# c1.create_line(200,10,10,10,fill="white")
c1.create_oval(100,0,0,100,fill="white")
root.mainloop()