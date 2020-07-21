# https://www.google.com/maps/dir/Udaipur,+Rajasthan/Jaipur,+Rajasthan/@25.7462362,73.6220776,8z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x3967e56550a14411:0xdbd8c28455b868b0!2m2!1d73.712479!2d24.585445!1m5!1m1!1s0x396c4adf4c57e281:0xce1c63a0cf22e09!2m2!1d75.7872709!2d26.9124336
# https://www.google.com/maps/place/Udaipur,+Rajasthan/@24.6084261,73.6370172,12z/data=!3m1!4b1!4m5!3m4!1s0x3967e56550a14411:0xdbd8c28455b868b0!8m2!3d24.585445!4d73.712479
# https://www.google.com/maps/search/restaurants/@24.5867668,73.7122531,16z/data=!3m1!4b1!4m8!2m7!3m6!1srestaurants!2sUdaipur,+Rajasthan!3s0x3967e56550a14411:0xdbd8c28455b868b0!4m2!1d73.712479!2d24.585445
# from tkinter import *
# root=Tk()
# root.geometry("700x700")
import webbrowser
# l1=Label(root,text="enter source location:")
# l1.grid(row=0,column=0)
# e1=Entry(root)
# e1.grid(row=0,column=1)
# l2=Label(root,text="enter destination location:")
# l2.grid(row=1,column=0)
# e2=Entry(root)
# e2.grid(row=1,column=1)
# def show():
#     url = "https://www.google.com/maps/dir/"
#     url = url + e1.get() + "/" + e2.get()
#     webbrowser.open(url)
# b1=Button(root,text="direction:",command=show)
# b1.grid(row=2,columnspan=2)

p=input("enter nearby location:")
# url="https://www.google.com/maps/place/"
# url="https://www.google.com/maps/search/"
url="https://www.google.com/search?q="
url=url+p
webbrowser.open(url)



# root.mainloop()