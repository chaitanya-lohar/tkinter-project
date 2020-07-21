from tkinter import *
root=Tk()
root.geometry("700x700")
x=IntVar()
def show1(a):
    y=myslider.get()
    x.set((y*76.5))
    # b1["bg"]="black"
    # b1["fg"]="white"
    # b1["width"]=10
    # b1["height"]=5
    # b1["text"]="chetan"
    #
l1=Label(root,text="how many amount we required?")
l1.pack()

myslider=Scale(root,from_=0,to=100,tickinterval=25,orient=HORIZONTAL)
myslider.set(30)
myslider.bind("<ButtonRelease>",show1)
myslider.pack()
e1=Label(root,textvariable=x)
e1.pack()
# b1=Button(root,text="submit",command=show1)
# b1.pack()
root.mainloop()