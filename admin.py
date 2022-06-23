#------------Admin Module---------------
import os
from tkinter import *

root = Tk()
def register1():
    root.destroy()
    os.system("Registratonform.py")
def read12():
    root.destroy()
    os.system("readinfoidlogin.py")
def dle():
    root.destroy()
    os.system("deletepage.py")
def updata():
    root.destroy()
    os.system("update.py")
def alocate1():
    root.destroy()
    os.system("alocateuni.py")
def backw():
    root.destroy()
    os.system("homescreen.py")
root.title("Admin")
root.config(bg="white")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(width,height))
f = Frame(root,bg="white")
l = Label(f,text="UNIVERSITY MANAGEMENT SYSTEM",font="times_romans 30 bold",bg="#3895d3",fg="white")
l.pack()
f.pack()
f1 = Frame(root,bg="white")

# Button 1
registerphoto = PhotoImage(file="register.png")
register = Button(f1,image=registerphoto,borderwidth=0,bg="white",command=register1)
register.grid(row=0,column=0,padx=50,pady=25)

# Button 2
readpho = PhotoImage(file="readinfo.png")
read = Button(f1,image=readpho,borderwidth=0,bg="white",command=read12)
read.grid(row=0,column=1,padx=50,pady=25)

# Button 3
upphoto = PhotoImage(file="update.png")
update1 = Button(f1,image=upphoto,borderwidth=0,bg="white",command=updata)
update1.grid(row=0,column=2,padx=50,pady=25)

f1.pack()

f2 = Frame(root,bg="white")


# Button 1
delpho = PhotoImage(file="del.png")
del1 = Button(f2,image=delpho,borderwidth=0,bg="white",command=dle)
del1.grid(row=0,column=0,padx=50,pady=25)

# Button 2
alophoto = PhotoImage(file="allocateuniroll.png")
alocate = Button(f2,image=alophoto,borderwidth=0,bg="white",command=alocate1)
alocate.grid(row=0,column=1,padx=50,pady=25)

# # Button 3
backphot = PhotoImage(file="back.png")
backbu = Button(f2,image=backphot,borderwidth=0,bg="white",command=backw)
backbu.grid(row=0,column=2,padx=50,pady=25)
f2.pack()

root.mainloop()


