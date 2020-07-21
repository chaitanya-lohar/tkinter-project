from tkinter import *
root=Tk()
root.geometry("700x700")
def func1():
    print(f"Your name is:{e1.get()}\n Your roll number is:{e2.get()}")
    # with open("records.txt","a") as obj:
    obj=open("records.txt","a")
    obj.write(f"\n{e1.get()} {e2.get()}")
    obj.close()

l1=Label(root,text="enter name")
l1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
l2=Label(root,text="Enter roll number:")
l2.grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)
b1=Button(root,text="Submit")
b1.grid(row=2,columnspan=2)
b1.config(command=func1)
root.mainloop()