#-------------Homescreen Module---------------
from tkinter import *
import os
ro = Tk()
ro.title("University Management System")
def Openlogin():
    ro.destroy()
    os.system("passwordscreen.py")
def contactus():
    ro.destroy()
    os.system("contactus.py")
def cour():
    ro.destroy()
    os.system("course.py")
def fact():
    ro.destroy()
    os.system("faculty.py")
widthsize = ro.winfo_screenwidth()
heightsize = ro.winfo_screenheight()
ro.geometry("%dx%d+0+0"%(widthsize,heightsize))
f1 = Frame(ro)
c1 = Canvas(f1,width=2000,height=430)
pho = PhotoImage(file="bg.png")
c1.create_image((685,210),image=pho)
c1.pack()
f1.pack()
f2 = Frame(ro)
l1 = Label(f2,text="Right Place for Bright Future",font="roboto 50 bold")
l1.grid(row=0,column=0,pady=10)
f2.pack()
f3 = Frame(ro)
dashicon = PhotoImage(file="dashbo.png")
b1 = Button(f3,image=dashicon,borderwidth=0,command=Openlogin)
b1.grid(row=0,column=1,padx=20)
courseicon = PhotoImage(file="course.png")
b2 = Button(f3,image=courseicon,borderwidth=0,command=cour)
b2.grid(row=0,column=2,padx=20)
faculityicon = PhotoImage(file="faculity.png")
b3 = Button(f3,image=faculityicon,borderwidth=0,command=fact)
b3.grid(row=0,column=3,padx=20)
contact = PhotoImage(file="contact.png")
b4 = Button(f3,image=contact,borderwidth=0,command=contactus)
b4.grid(row=0,column=4,padx=20)
f3.pack()
ro.mainloop()


