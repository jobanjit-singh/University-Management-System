#---------------------Update Data Module----------------
import os
from tkinter import *
from tkinter import messagebox
import cx_Oracle as cs
con = cs.connect("scott/tiger")
cursor1 = con.cursor()
def cel():
    root.destroy()
    os.system("admin.py")
def up():
    if changes.get()=="First Name":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set fname='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Last Name":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set lname='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Father Name":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set father_name='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Mother Name":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set mother_name='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Mobile No":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set mobile_no='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Email Id":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set email_id='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Address":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set address='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Matric Aggregate":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set matric_agg='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Senior Secondary Marks":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set sen_sec='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Course":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set course='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
    elif changes.get()=="Department":
        try:
            cur2 = con.cursor()
            idval = id1.get()
            fname = newvalfname.get()
            cur2.execute("update uni_record set department='%s' where u_rollno=%d"%(fname,int(idval)))
            con.commit()
            cur2.close()
            root.destroy()
            messagebox.showinfo("Update Detail","Updation Completed")
            os.system("update.py")
        except:
            messagebox.showwarning("Update Detail","Enter Valid Input")
def opdet():
    if id1.get() == "" and changes.get()=="Select":
        messagebox.showinfo("Update Detail","Entry is Empty")
    if id1.get() == "" or changes.get()=="Select":
        messagebox.showinfo("Update Detail","Entry is Empty")
    elif changes.get()=='First Name':
        idval = int(id1.get())
        cursor1.execute("select fname from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Last Name':
        idval = int(id1.get())
        cursor1.execute("select lname from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Father Name':
        idval = int(id1.get())
        cursor1.execute("select father_name from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Mother Name':
        idval = int(id1.get())
        cursor1.execute("select mother_name from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Mobile No':
        idval = int(id1.get())
        cursor1.execute("select mobile_no from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Email Id':
        idval = int(id1.get())
        cursor1.execute("select email_id from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Address':
        idval = int(id1.get())
        cursor1.execute("select address from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Matric Aggregate':
        idval = int(id1.get())
        cursor1.execute("select matric_agg from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Senior Secondary Marks':
        idval = int(id1.get())
        cursor1.execute("select sen_sec from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Course':
        idval = int(id1.get())
        cursor1.execute("select course from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    elif changes.get()=='Department':
        idval = int(id1.get())
        cursor1.execute("select department from uni_record where u_rollno=:id",{":id":idval})
        ls = cursor1.fetchall()
        cursor1.close()
    f4 = Frame(root)
    # Labels
    Label(f4,text="Old:",font="time_roman 15 bold").grid(row=0,column=0,padx=10,pady=10,sticky="w")
    Label(f4,text="New:",font="time_roman 15 bold").grid(row=1,column=0,padx=10,pady=10,sticky="w")
    # Entries
    Label(f4,text="%s"%(ls[0]),font="time_roman 15 bold").grid(row=0,column=1,padx=10,pady=10)

    Entry(f4,textvariable=newvalfname,font="times_roman 15 bold").grid(row=1,column=1,padx=10,pady=10)

    f4.pack()
    f5 = Frame(root)
    # button
    Button(f5,text="Update",command=up).grid(row=0,column=0,padx=10,pady=10)
    Button(f5,text="Cancel",borderwidth=2,command=cel).grid(row=0,column=1,padx=10,pady=10)
    f5.pack()
root = Tk()
id1 = StringVar()
newvalfname = StringVar()
root.title("Change Detail")
root.geometry("400x400+0+0")
root.minsize(400,400)
root.maxsize(400,400)
newfname = StringVar()
# Heading 
f1 = Frame(root)
Label(f1,text="Change Detail",font="times_roman 20 bold",fg="red").pack(padx=10,pady=10)
f1.pack()

# Entry

f2 = Frame(root)
Label(f2,text="Rollno:",font="times_roman 15 bold").grid(row=0,column=0,padx=10,pady=10)
Label(f2,text="Update:",font="times_roman 15 bold").grid(row=1,column=0,padx=10,pady=10)
changes = StringVar()
changes.set("Select")
Entry(f2,textvariable=id1,font="times_roman 15 bold").grid(row=0,column=1,padx=10,pady=10)
OptionMenu(f2,changes,"First Name","Last Name","Father Name","Mother Name","Mobile No","Email Id","Address","Matric Aggregate","Senior Secondary Marks","Course","Department").grid(row=1,column=1,padx=10,pady=10,sticky="w")
f2.pack()

# button
f3=Frame(root)
Button(f3,text="Fetch Detail",borderwidth=2,command=opdet).grid(row=0,column=0,padx=10,pady=10)
Button(f3,text="Cancel",borderwidth=2,command=cel).grid(row=0,column=1,padx=10,pady=10)
f3.pack()
root.mainloop()