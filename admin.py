import os
from tkinter import *

root = Tk()
def register1():
    root.destroy()
    os.system("Registratonform.py")
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
register.grid(row=0,column=0,padx=100,pady=40)

# Button 2
readpho = PhotoImage(file="readinfo.png")
read = Button(f1,image=readpho,borderwidth=0,bg="white")
read.grid(row=0,column=1,padx=100,pady=40)
f1.pack()

f2 = Frame(root,bg="white")

# Button 1
upphoto = PhotoImage(file="update.png")
update1 = Button(f2,image=upphoto,borderwidth=0,bg="white")
update1.grid(row=0,column=0,padx=100,pady=40)

# Button 2
delpho = PhotoImage(file="del.png")
del1 = Button(f2,image=delpho,borderwidth=0,bg="white")
del1.grid(row=0,column=1,padx=100,pady=40)
f2.pack()
root.mainloop()