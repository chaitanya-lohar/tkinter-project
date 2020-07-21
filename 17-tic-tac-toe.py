from tkinter import *
root=Tk()
root.geometry("700x700")
count=1
def show(b):

    global count
    if(count%2==0):
        if(b["text"]==""):
            b["text"]="0"

    else:
        if (b["text"] == ""):
            b["text"] = "x"
    count+=1


    if(b1["text"]=="x" and b2["text"]=="x" and b3["text"]=="x"):
        print("x player is won")
        exit()
    elif(b1["text"]=="x" and b4["text"]=="x" and b7["text"]=="x"):
        print("x player is won")
        exit()
    elif(b3["text"]=="x" and b6["text"]=="x" and b9["text"]=="x" ):
        print("x player is won")
        exit()
    elif(b7["text"]=="x" and b8["text"]=="x" and b9["text"]=="x" ):
        print("x player is won")
        exit()
    elif(b1["text"]=="x" and b5["text"]=="x" and b9["text"]=="x" ):
        print("x player is won")
        exit()
    elif(b3["text"]=="x" and b5["text"]=="x" and b7["text"]=="x"):
        print("x player is won")
        exit()


    elif (b1["text"] == "0" and b2["text"] == "0" and b3["text"] == "0"):
        print("0 player is won")
        exit()
    elif (b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0"):
        print("0 player is won")
        exit()
    elif (b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0"):
        print("0 player is won")
        exit()
    elif (b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0"):
        print("0 player is won")
        exit()
    elif (b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0"):
        print("0 player is won")
        exit()
    elif (b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0"):
        print("0 player is won")
        exit()

    elif(count>9):

        print("0:you lost game")

root.title("tic-tac-toe game")
b1=Button(root,text="",width=5,height=2,font="Arial 15 bold",command=lambda :show(b1))
b1.grid(row=0,column=0)
b2=Button(root,text="",width=5,height=2,font="Arial 15 bold" ,command=lambda :show(b2))
b2.grid(row=0,column=1)
b3=Button(root,text="",width=5,height=2,font="Arial 15 bold" ,command=lambda :show(b3))
b3.grid(row=0,column=2)
b4=Button(root,text="",width=5,height=2,font="Arial 15 bold",command=lambda :show(b4))
b4.grid(row=1,column=0)
b5=Button(root,text="",width=5,height=2,font="Arial 15 bold",command=lambda :show(b5))
b5.grid(row=1,column=1)
b6=Button(root,text="",width=5,height=2,font="Arial 15 bold",command=lambda :show(b6))
b6.grid(row=1,column=2)
b7=Button(root,text="",width=5,height=2,font="Arial 15 bold",command=lambda :show(b7))
b7.grid(row=2,column=0)
b8=Button(root,text="",width=5,height=2,font="Arial 15 bold",command=lambda :show(b8))
b8.grid(row=2,column=1)
b9=Button(root,text="",width=5,height=2,font="Arial 15 bold",command=lambda :show(b9))
b9.grid(row=2,column=2)

root.mainloop()