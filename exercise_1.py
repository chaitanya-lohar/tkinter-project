
from tkinter import *
from tkinter import messagebox

from PIL import Image,ImageTk

root=Tk()
root.geometry("300x400")
root.resizable(1,1)
root.title("Home page")
photo=ImageTk.PhotoImage(Image.open("SBI-Logo.jpg"))
l1=Label(root,image=photo)
l1.pack()
l2=Label(root,text='''xmlrpc.client.ServerProxy now supports an optional
                    headers keyword argument for a sequence of HTTP headers to be sent with each request. 
                    Among other things,
                     this makes it possible to upgrade from default
                      basic authentication to faster session authentication.
''',bg="blue",fg="yellow",font="BlackJackRegular",bd=8,relief="ridge" ,width=10,height=3)
l2.pack(anchor="center")
        # anchor="n",padx=50,pady=50,side="bottom",fill=X
def fun():
    messagebox.showinfo("hello","good morning!")


l3=Button(root,text="Click",activeforeground="red",activebackground="yellow" ,pady=10,padx=5)
l3.pack(side="left")
l4=Button(root,text="submit",command=fun,activeforeground="white",activebackground="black",pady=10,padx=5)
l4.pack(side="left")
root.mainloop()
