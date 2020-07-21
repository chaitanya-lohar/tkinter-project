from tkinter import *
root=Tk() # Tk is a by default class, root is a object and we can change its name
root.geometry("500x500")
root.title("Welcome to my first page")
# root.resizable(0,0)
root.minsize(100,100)
root.maxsize(700,700)
#widget
photo=PhotoImage(file="pr.PNG")
l2=Label(root,image=photo)
l2.pack()
l1=Label(root,text="Good morning!",font="lucida 35 bold ")
l1.pack()
root.mainloop()
print("my name is chetan")