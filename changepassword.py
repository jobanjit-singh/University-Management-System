from email import message
from tkinter import *
from tkinter import messagebox
import os
import cx_Oracle as xc 
conn = xc.connect("scott/tiger")
def cel():
    root.destroy()
    os.system("student.py")
def up():
    try:
        cur2 = con.cursor()
        idval = id1.get()
        fname = newvalfname.get()
        cur2.execute("update uni_record set fname='%s' where u_rollno=%d"%(fname,int(idval)))
        con.commit()
        cur2.close()
        root.destroy()
        messagebox.showinfo("Update Detail","Updation Completed")
        os.system("changepassword.py")
    except:
        messagebox.showwarning("Update Detail","Enter Valid Input")
def opdet():
    cur1 = conn.cursor()
    cur1.execute("select username from login")
    ls = cur1.fetchall()
    if id1.get() == "":
        messagebox.showinfo("Update Detail","Entry is Empty")
    if id1.get() not in ls:
        messagebox.showwarning("Change Username and Password","User Not Found")
    else:
        cur1.execute("select username,password from login where username='%s'"%(id1.get()))
        ls1 = cur1.fetchall()
    f4 = Frame(root)
    Label(f4,text="Old username:",font="time_roman 15 bold").grid(row=0,column=0,padx=10,pady=10,sticky="w")
    Label(f4,text="New username:",font="time_roman 15 bold").grid(row=1,column=0,padx=10,pady=10,sticky="w")
    # Entries
    Label(f4,text="%s"%(ls1[0]),font="time_roman 15 bold").grid(row=0,column=1,padx=10,pady=10)

    Entry(f4,textvariable=newusername,font="times_roman 15 bold").grid(row=1,column=1,padx=10,pady=10)

    Label(f4,text="Old Password:",font="time_roman 15 bold").grid(row=2,column=0,padx=10,pady=10,sticky="w")
    Label(f4,text="New Password:",font="time_roman 15 bold").grid(row=3,column=0,padx=10,pady=10,sticky="w")
    # Entries
    Label(f4,text="%s"%(ls1[1]),font="time_roman 15 bold").grid(row=2,column=1,padx=10,pady=10)

    Entry(f4,textvariable=newusername,font="times_roman 15 bold").grid(row=3,column=1,padx=10,pady=10)

    f4.pack()
    f5 = Frame(root)
    # button
    Button(f5,text="Update",command=up).grid(row=0,column=0,padx=10,pady=10)
    Button(f5,text="Cancel",borderwidth=2,command=cel).grid(row=0,column=1,padx=10,pady=10)
    f5.pack() 
root = Tk()
id1 = StringVar()
newusername = StringVar()
newpassword = StringVar()
root.title("Change Username and Password")
root.geometry("400x400+0+0")
root.minsize(400,400)
root.maxsize(400,400)
newfname = StringVar()
# Heading 
f1 = Frame(root)
Label(f1,text="Change Username and Password",font="times_roman 20 bold",fg="red").pack(padx=10,pady=10)
f1.pack()

# Entry

f2 = Frame(root)
Label(f2,text="U.Rollno:",font="times_roman 15 bold").grid(row=0,column=0,padx=10,pady=10)
Entry(f2,textvariable=id1,font="times_roman 15 bold").grid(row=0,column=1,padx=10,pady=10)
f2.pack()

# button
f3=Frame(root)
Button(f3,text="Fetch Detail",borderwidth=2,command=opdet).grid(row=0,column=0,padx=10,pady=10)
Button(f3,text="Cancel",borderwidth=2,command=cel).grid(row=0,column=1,padx=10,pady=10)
f3.pack()
root.mainloop()