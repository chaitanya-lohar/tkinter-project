from tkinter import *
from tkinter import messagebox

from voicecommand_project import *
import time
root=Tk()
root.geometry("700x700")
root.resizable(0,0)
def fun1():
    b1.bind("<FocusIn>",speak("Your form has been submited"))

    messagebox.showinfo("Your form has been submited")
    b1.bind("<FocusIn>")

def check1():
    if(e2.get()==None or e3.get()==None or e5.get()==None or e6.get()==None or e7.get() or e8.get()==None or e9.get()==None):
        speak("Entry is not completed, Please fill properly.")
    else:
        a1=e2.get()
        speak(f"your name is{a1}")
        time.sleep(1)

        a2 = e3.get()
        speak(f"your course is{a2}")
        time.sleep(1)
        a3 = e5.get()
        speak(f"{a3} semester")
        time.sleep(1)
        a4 = e6.get()
        speak(f"form number is:{a4}")
        time.sleep(1)
        a5 = e7.get()
        speak(f"your contact number is:{a5}")
        time.sleep(1)
        a6 = e8.get()
        speak(f"your email ID is:{a6}")
        time.sleep(1)
        a7 = e9.get()
        speak("sorry ,due to privacy issue , i can't speak password")
        time.sleep(1)

a=StringVar()
b=StringVar()
c=StringVar()
d=IntVar()
e=IntVar()
f=StringVar()
g=StringVar()
def voice1():
    a.set(takecommand())
    time.sleep(1)
    b.set(takecommand())
    time.sleep(1)
    c.set(takecommand())
    time.sleep(1)
    d.set(takecommand())
    time.sleep(1)
    e.set(takecommand())
    time.sleep(1)
    f.set(takecommand())
    time.sleep(1)
    g.set(takecommand())
    time.sleep(1)






l12=Label(root,text="Registration Form",font="Arial 10 bold")
l12.grid(row=0,columnspan=2)
l1=Label(root,text="Name",padx=20,pady=5)
l1.grid(row=1,column=0)
e2=Entry(root,textvariable=a)
e2.grid(row=1,column=1)
e2.bind("<FocusIn>",lambda a:speak("Enter your name"))
l2=Label(root,text="Course",padx=20,pady=5)
l2.grid(row=2,column=0)
e3=Entry(root,textvariable=b)
e3.grid(row=2,column=1)
e3.bind("<FocusIn>",lambda a:speak("Enter your Course"))

l4=Label(root,text="Semester",padx=20,pady=5)
l4.grid(row=4,column=0)
e5=Entry(root,textvariable=c)
e5.grid(row=4,column=1)
e5.bind("<FocusIn>",lambda a:speak("Enter Semester Name"))

l5=Label(root,text="Form Number",padx=20,pady=5)
l5.grid(row=5,column=0)
e6=Entry(root,textvariable=d)
e6.grid(row=5,column=1)
e6.bind("<FocusIn>",lambda a:speak("Enter form number"))

l6=Label(root,text="Contact Number",padx=20,pady=5)
l6.grid(row=6,column=0)
e7=Entry(root,textvariable=e)
e7.grid(row=6,column=1)
e7.bind("<FocusIn>",lambda a:speak("Enter Contact number"))
l7=Label(root,text="Email ID",padx=20,pady=5)
l7.grid(row=7,column=0)
e8=Entry(root,textvariable=f)
e8.grid(row=7,column=1)
e8.bind("<FocusIn>",lambda a:speak("Enter your Email ID"))
l8=Label(root,text="Password",padx=20,pady=10)
l8.grid(row=8,column=0)
e9=Entry(root,show="*",textvariable=g)
e9.grid(row=8,column=1)
e9.bind("<FocusIn>",lambda a:speak("Enter your password"))
b1=Button(root,text="Submit",font="Arial 13 bold",bg="gray",fg="black",pady=10)
b1.config(command=fun1)
b1.grid(row=9,column=1)
b2=Button(root,text="Check",font="Arial 13 bold",bg="red",fg="black",pady=20)
b2.config(command=check1)
b2.grid(row=9,column=2)
b3=Button(root,text="Entry By Voice command",font="Arial 13 bold",bg="black",fg="white",pady=15)
b3.config(command=voice1)
b3.grid(row=10,columnspan=2)
mainloop()
