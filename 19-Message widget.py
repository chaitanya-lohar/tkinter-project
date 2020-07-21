from tkinter import *
root=Tk()
root.geometry("400x350")
root.title("Message Widget")
# root.resizable(0,0)
what_do_you="The widget can be used to display short text messages. The message widget is similar in its functionality to the Label widget, but it is more flexible in displaying text, e.g. the font can be changed while the Label widget can only display text in a single font. "
msg=Message(root,text=what_do_you,font="times 20 italic",bg="lightgreen")
msg.pack()
# l1=Label(root,text=what_do_you,font="times 20 italic")
# l1.pack()

root.mainloop()