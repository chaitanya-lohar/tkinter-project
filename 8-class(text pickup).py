from assistent import *
from tkinter import *
root=Tk()
root.geometry('700x700')
def show1():
    s=e1.get()
    print(s)
    speak(s)
f1=Frame(root,bg="lightblue",borderwidth=5,relief=GROOVE)
f1.pack(side=LEFT)
e1=Entry(f1)
e1.pack()
b1=Button(f1,text="submit",bg="black",fg="white",command=show1)
b1.pack()
root.mainloop()