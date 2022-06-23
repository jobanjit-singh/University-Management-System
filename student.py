#----------------------Student Module--------------
import os
from tkinter import *
from tkinter import messagebox
root = Tk()
def userpro():
    root.destroy()
    os.system("readinfoidloginstudent.py")
def resu():
        root.destroy()
        os.system("result.py")
def backu():
    root.destroy()
    os.system("homescreen.py")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title("Student")
root.geometry("%dx%d+0+0"%(width,height))
root.config(bg="white")
f = Frame(root,bg="white")
l1 = Label(f,text="STUDENT PORTAL",font="times_roman 50 bold",bg="#29c5f6",fg="white")
l1.pack()
f.pack()
f1 = Frame(root,bg="white")
phot = PhotoImage(file="userprofile.png")
b1 = Button(f1,image=phot,borderwidth=0,command=userpro)
b1.grid(row=0,column=0,padx=10,pady=10)
photo2 = PhotoImage(file="result.png")
b2 = Button(f1,image=photo2,borderwidth=0,command=resu)
b2.grid(row=0,column=1,padx=10,pady=10)
f1.pack()
f2=Frame(root,bg="white")
backbut = PhotoImage(file="back1.png")
b2 = Button(f2,image=backbut,borderwidth=0,command=backu)
b2.grid(row=0,column=1,padx=10,pady=10)
f2.pack()
root.mainloop()