#--------Contact Us Module-----------
import os
from tkinter import *
def back1():
    root.destroy()
    os.system("homescreen.py")
root = Tk()

root.title("Contact Us")
root.geometry("500x250+0+0")
root.minsize(500,250)
root.maxsize(500,250)
f1 = Frame(root)
Label(f1,text="ABC University",font="times_roman 20 bold",fg="red").pack()
f2 = Frame(root,bg="#808080")
Label(f2,text="Contact Us:",font="times_roman 10 bold",bg="#808080",fg="white").grid(row=0,column=0,sticky="w")
Label(f2,text="Mobile No:7964521812",font="times_roman 10 bold",bg="#808080",fg="white").grid(row=1,column=1,sticky="w")
Label(f2,text="Email Id:abc_university01234@gmail.com",font="times_roman 10 bold",bg="#808080",fg="white").grid(row=2,column=1,sticky="w")
f3 = Frame(root)
Label(f2,text="Developed By:",font="times_roman 10 bold",bg="#808080",fg="white").grid(row=3,column=0,sticky="w")
Label(f2,text="Himanshu Madhura (2000109)",font="times_roman 10 bold",bg="#808080",fg="white").grid(row=4,column=1,sticky="w")
Label(f2,text="Jobanjit Singh (2000118)",font="times_roman 10 bold",bg="#808080",fg="white").grid(row=5,column=1,sticky="w")
Label(f2,text="Karampreet Singh (2000122)",font="times_roman 10 bold",bg="#808080",fg="white").grid(row=6,column=1,sticky="w")
Label(f2,text="Karandeep Singh (2000123)",font="times_roman 10 bold",bg="#808080",fg="white").grid(row=7,column=1,sticky="w")
f3 = Frame(root)
Button(f3,text="Back",command=back1).pack(pady=5)
f1.pack()
f2.pack()
f3.pack()
root.mainloop()

