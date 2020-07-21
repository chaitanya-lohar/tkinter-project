from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Home page")
root.geometry("500x500")
root.resizable(0,0)
photo=ImageTk.PhotoImage(Image.open("SBI-Logo.jpg"))
l2=Label(root,image=photo)
l2.pack()
l1=Label(root,text='''xmlrpc.client.ServerProxy now supports an optional
                    headers keyword argument for a sequence of HTTP headers to be sent with each request. 
                    Among other things,
                     this makes it possible to upgrade from default
                      basic authentication to faster session authentication.''',font="BlackJackRegular")
root.mainloop()