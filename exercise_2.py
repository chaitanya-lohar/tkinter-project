# Student form exam form
from assistent import *
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x700")
root.resizable(0,0)
def fun():

    speak("your from has been submited")

root.title("Student Form for Examination")
l1=Label(root,text="Your Name")
l1.grid(row=0,column=0, padx=10,pady=20)
t1=Entry(root)
t1.grid(row=0,column=1)
t1.bind("<FocusIn>",lambda a:speak("Please enter your name"))
l2=Label(root,text="Father name")
l2.grid(row=1,column=0, padx=10,pady=20)
t2=Entry(root)
t2.grid(row=1,column=1)
t2.bind("<FocusIn>",lambda a:speak("enter your father name"))
l3=Label(root,text="Mobile Number")
l3.grid(row=2,column=0, padx=10,pady=20)
t3=Entry(root)
t3.grid(row=2,column=1)
t3.bind("<FocusIn>",lambda a:speak("Enter your mobile number"))
l4=Label(root,text="Previous Class Percentage")
l4.grid(row=3,column=0, padx=10,pady=10)
t4=Entry(root)
t4.grid(row=3,column=1)
t4.bind("<FocusIn>",lambda a:speak("enter your pervious year percentage"))
b1=Button(root,text="Submit",command=fun)
b1.bind("<Button-1>",lambda a:root.configure(bg="lightblue"))
b1.grid(row=4,columnspan=2)


root.mainloop()