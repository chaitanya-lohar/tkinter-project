from tkinter import *
from tkinter import filedialog as file
from tkinter import colorchooser
import os
root=Tk()
root.geometry("700x700")

def show1():
     var=file.askopenfile()
     print(list(var))
     os.startfile(var)
    # file.askdirectory()
    # file.askopenfilenames()
    # file.asksaveasfile()
    # colorchooser.askcolor()

b1=Button(root,text="file open",command=show1,padx=20,pady=10)
b1.pack(anchor="w")

root.mainloop()