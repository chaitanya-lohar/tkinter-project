from tkinter import *
import webbrowser
from tkinter import messagebox
from PIL import Image,ImageTk

root=Tk()
root.geometry("800x600")
root.title("JavaTpoint")
photo=ImageTk.PhotoImage(Image.open('learning.jpg'))
l2=Label(root,image=photo)
l2.pack()
l3=Label(root,text="Click on above files for learning something amazing!",font="times 20 italic")
l3.pack()
# l1=Label(root,text="javaTpoint",font="times 20 italic",padx=10,pady=5)
# l1.pack(anchor="w")
def feature():
    url="https://www.javatpoint.com/python-features"
    webbrowser.open(url)
def history():
    url="https://www.javatpoint.com/python-history"
    webbrowser.open(url)
def application():
    webbrowser.open("https://www.javatpoint.com/python-applications")
def install():
    webbrowser.open("https://www.javatpoint.com/how-to-install-python")
def example():
    webbrowser.open("https://www.javatpoint.com/python-example")
def variables():
    webbrowser.open("https://www.javatpoint.com/python-variables")

def concepts():
    webbrowser.open("https://www.javatpoint.com/python-oops-concepts")
def objclass():
    webbrowser.open("https://www.javatpoint.com/python-objects-classes")
def constructor():
    webbrowser.open("https://www.javatpoint.com/python-constructors")
def inheritance():
    webbrowser.open("https://www.javatpoint.com/inheritance-in-python")

def setup():
    webbrowser.open("https://www.javatpoint.com/python-mysql-environment-setup")
def connection():
    webbrowser.open("https://www.javatpoint.com/python-mysql-database-connection")
def mongo():
    webbrowser.open("https://www.javatpoint.com/python-mongodb")
def lite():
    webbrowser.open("https://www.javatpoint.com/python-sqlite")

def button():
    webbrowser.open("https://www.javatpoint.com/python-tkinter-button")
def canvas():
    webbrowser.open("https://www.javatpoint.com/python-tkinter-canvas")
def checkbutton():
    webbrowser.open("https://www.javatpoint.com/python-tkinter-checkbutton")
def hom():
    messagebox.showinfo("Notes","You are already in home!")

mainmenu=Menu(root)
home=Menu(mainmenu,tearoff=0)
home.add_command(label="Home",command=hom)
Python=Menu(mainmenu,tearoff=0)
PythonTutorial=Menu(Python,tearoff=0)
PythonTutorial.add_command(label="Python Features",command=feature)
PythonTutorial.add_command(label="Python History",command=history)
PythonTutorial.add_command(label="Python Applications",command=application)
PythonTutorial.add_command(label="Python Install",command=install)
PythonTutorial.add_command(label="Python Example",command=example)
PythonTutorial.add_command(label="Python Variables",command=variables)

PythonOOPs=Menu(Python,tearoff=0)
PythonOOPs.add_command(label="OOPs Concepts",command=concepts)
PythonOOPs.add_command(label="Objects Class",command=objclass)
PythonOOPs.add_command(label="Constuctors",command=constructor)
PythonOOPs.add_command(label="Inheritance",command=inheritance)

PythonMySQL=Menu(Python,tearoff=0)
PythonMySQL.add_command(label="Environment Setup",command=setup)
PythonMySQL.add_command(label="Database Connection",command=connection)
# PythonMySQL.add_command(label="Creating New Database")
# PythonMySQL.add_command(label="Creating Tables")
# PythonMySQL.add_command(label="Insert Operation")

PythonMongoDB=Menu(Python,tearoff=0)
PythonMongoDB.add_command(label="Python MongoDB",command=mongo)

PythonSQLite=Menu(Python,tearoff=0)
PythonSQLite.add_command(label="Python SQlLite",command=lite)

Pythontkinter=Menu(Python,tearoff=0)
Pythontkinter.add_command(label="Button",command=button)
Pythontkinter.add_command(label="Canvas",command=canvas)
Pythontkinter.add_command(label="Checkbutton",command=checkbutton)
# Pythontkinter.add_command(label="Entry")
# Pythontkinter.add_command(label="Frame")
# Pythontkinter.add_command(label="Label")
def java1():
    webbrowser.open("https://www.tutorialspoint.com/java/index.htm")
def php1():
    webbrowser.open("https://www.w3schools.com/php/default.asp")
Java=Menu(mainmenu)
Java.add_command(label="Java",command=java1)
php=Menu(mainmenu)
php.add_command(label="php",command=php1)

mainmenu.add_cascade(label="Home",menu=home)
mainmenu.add_cascade(label="Python",menu=Python)
mainmenu.add_cascade(label="Java",menu=Java)
mainmenu.add_cascade(label="php",menu=php)
Python.add_cascade(label="Pythontutorial",menu=PythonTutorial)
Python.add_cascade(label="PythonOOPs",menu=PythonOOPs)
Python.add_cascade(label="PythonMySQL",menu=PythonMySQL)
Python.add_cascade(label="PythonMongoDB",menu=PythonMongoDB)
Python.add_cascade(label="PythonSQLite",menu=PythonSQLite)
Python.add_cascade(label="Pythontkinter",menu=Pythontkinter)
root.config(menu=mainmenu)





root.mainloop()