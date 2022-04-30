import os
import cx_Oracle
from tkinter import *
from tkinter import messagebox
root = Tk()
def enter1():
    con = cx_Oracle.connect("scott/tiger")
    cur = con.cursor()
    fla = -1
    if usern.get()=='' and passw.get() =='' and posi.get()=='Select':
        messagebox.showinfo("University Management System","Entry is Empty")
    if usern.get()=='' or passw.get() =='' or posi.get()=='Select':
        messagebox.showinfo("University Management System","Entry is Empty")
    if posi.get()=="Student":
        cur.execute("select * from login where position='Student'")
        ls = cur.fetchall()
        for i in ls:
            if i[0]==usern.get() and i[1]==passw.get():
                fla = 0
        if fla == 0:
            os.system("student.py")
        else:
            messagebox.showinfo("University Management System","Incorect Username and Password")
    if posi.get()=="Admin":
        cur.execute("select * from login where position='Admin'")
        ls = cur.fetchall()
        for i in ls:
            if i[0]==usern.get() and i[1]==passw.get():
                fla = 0
        if fla == 0:
            des()
            os.system("admin.py")
        else:
            messagebox.showinfo("University Management System","Incorect Username and Password")
    cur.close()
    con.close()
def des():
    root.destroy()
root.title("University Management System")
root.geometry("350x450")
root.minsize(450,350)
root.maxsize(450,350)
c0 = Canvas(root,width=100,height=100)
c0.pack()
pho = PhotoImage(file="fi.png")
c0.create_image(50,50,image=pho)
f1 = Frame(root)
l1 = Label(f1,text="Welcome to ABC University",font="algerian 20 bold",foreground="red")
l2 = Label(f1,text="Login",font="times_roman 15 bold",foreground="#0ea2e9")
l1.pack()
l2.pack()
f1.pack()
f2 = Frame(root)
usern = StringVar()
passw = StringVar()
posi = StringVar()
posi.set("Select")
l3 = Label(f2,text="Username",font="times_roman 15 bold")
l4 = Label(f2,text="Password",font="times_roman 15 bold")
l5 = Label(f2,text="Position",font="times_roman 15 bold")
e1 = Entry(f2,textvariable=usern)
e2 = Entry(f2,textvariable=passw,show="*")
e3 = OptionMenu(f2,posi,"Student","Admin")
l3.grid(row=0,column=0)
l4.grid(row=1,column=0)
l5.grid(row=2,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
f2.pack()
f3 = Frame(root)
b1 = Button(f3,text="Login",bg="#0ea2e9",fg="white",command=enter1)
b2 = Button(f3,text="Cancel",bg="#0ea2e9",fg="white",command=des)
b1.pack(side=LEFT,padx=10,pady=10)
b2.pack(side=LEFT,padx=10,pady=10)
f3.pack()
root.mainloop()