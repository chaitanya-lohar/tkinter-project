from tkinter import *
from covid import Covid
root=Tk()
root.geometry("700x700")
y=StringVar()
def show():
    f1 = Frame(root, bg="cyan")
    covid = Covid()
    cases = covid.get_status_by_country_name((y.get()).upper())
    Button(f1, text="Back", font="times 15 italic",command=home).place(x=10, y=10)
    n=100
    Label(f1, text=f"Current Covid-19 Status Of {(y.get()).upper()}",font="times 20 bold",bg="cyan").place(x=100,y=50)
    for record in cases:
        print(record,":",cases[record])

        Label(f1,text=f"{record}     :      {cases[record]}",font="times 15 italic",bg="cyan").place(x=200,y=n)
        n+=50
    f1.place(x=0,y=0,height=700,width=700)
    y.set("")

def home():
    f1=Frame(root,bg="lightblue").place(x=0,y=0,height=700,width=700)
    Label(f1,text="Status Of Covid-19 Cases",font="Algerian 20 bold",bg="lightblue").place(x=150,y=80)
    Label(f1,text="Enter Your Country Name:",font="times 15 italic",bg="lightblue").place(x=100,y=200)
    Entry(f1,textvariable=y).place(x=350,y=200)
    Button(f1,text="Check Status",font="times 15 italic",command=show).place(x=250,y=250)
home()
root.mainloop()