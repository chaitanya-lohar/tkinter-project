from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("400x400")
x=IntVar()
def show1():
    if(x.get()==1):
        # messagebox.showinfo("courses","you clicked on python")
        messagebox.askquestion("courses",f"do you want to purchase this {'Python'} course?")
    else:
        pass

l1=Label(root,text="which language do you want to learn?",font="times 20 italic",padx=20,pady=5)
l1.pack()
r1=Radiobutton(root,text="Python",font="times 20 italic",variable=x,value=1,padx=20)
r1.pack(anchor="w")
r1=Radiobutton(root,text="Perl",font="times 20 italic",variable=x,value=2,padx=20)
r1.pack(anchor="w")
r1=Radiobutton(root,text="C++",font="times 20 italic",variable=x,value=3,padx=20)
r1.pack(anchor="w")
r1=Radiobutton(root,text="Java",font="times 20 italic",variable=x,value=4,padx=20)
r1.pack(anchor="w")
b1=Button(root,text="select",command=show1)
b1.pack()

root.mainloop()