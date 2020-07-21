from tkinter import *
import tkinter.messagebox as box
root=Tk()
root.geometry("700x700")
def show():
    # box.showinfo("Welcome","this is file menu")
    ans=box.askquestion("Welcome","this is file menu")
    if(ans=="yes"):
        box.showinfo("you clicked on yes")
    else:
        # box.showinfo("you clicked on no")
        box.askretrycancel("ask","askretrycancel")
mainmenu=Menu(root)
file=Menu(mainmenu)
# file.add_command(label="New")
new=Menu(file)
new.add_command(label="new1")
new.add_command(label="new2")
new.add_command(label="new3")
new.add_command(label="new3")
new.add_command(label="new4")
file.add_cascade(label="New",menu=new)

file.add_command(label="Open",command=show)
file.add_command(label="Close",command=show)
file.add_command(label="Save",command=show)
file.add_command(label="Save as",command=show)
file.add_command(label="Print",command=show)
file.add_separator()
file.add_command(label="Exit",command=show)

mainmenu.add_cascade(label="File",menu=file)
root.config(menu=mainmenu)
# edit=Menu(mainmenu,tearoff=0)
# edit.add_command(label="Cut",command=show)
# edit.add_command(label="Copy",command=show)
# edit.add_command(label="Paste",command=show)
# edit.add_command(label="Find",command=show)
# edit.add_command(label="Replace",command=show)
# mainmenu.add_cascade(label="Edit",menu=edit)

root.mainloop()