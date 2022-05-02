from tkinter import *
from tkinter import messagebox
import cx_Oracle as cs
def read1():
    idval = id.get()
    if idval=='':
        messagebox.showinfo("ID ENTRY","Entry is Empty")
    else:
        conn = cs.connect("scott/tiger")
        cur = conn.cursor()
        cur.execute("select s_no from student1 where s_no=:idval",{":idval":int(idval)})
        ls = cur.fetchall()
        idint = int(idval)
        if ls==[]:
            messagebox.showinfo("ID ENTRY","No User Found")
        else:
            for i in ls:
                if i[0]==idint:
                    root.destroy()
                    showinfo()
        cur.close()
        conn.close()
def showinfo():
    r = Tk()
    width = r.winfo_screenwidth()
    height = r.winfo_screenheight()
    r.geometry("%dx%d+0+0"%(width,height))
    r.title("Student Detail")
    r.config(bg="white")
    f =Frame(r,bg="white")
    Label(f,text="Student Detail",font="times_roman 40 bold",fg = "red",bg="white").pack(padx=10,pady=10)
    f.pack()
    connn = cs.connect("scott/tiger")
    cur1 = connn.cursor()
    idval1=int(id.get())
    cur1.execute("select * from Student1 where s_no=:idval1",{":idval1":idval1})
    list1 = cur1.fetchall()
    rollno = list1[0][0]
    name = list1[0][1] +" "+list1[0][2]
    fathername = list1[0][3]
    mothername = list1[0][4]
    mobile = list1[0][5]
    emailid = list1[0][6]
    address = list1[0][7]
    matric_agg = list1[0][8]
    sen_secc = list1[0][9]
    courses = list1[0][10]
    department = list1[0][11]
    f1 = Frame(r,bg="#808080")
    Label(f1,text="Rollno: %s"%(rollno),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Name: %s"%(name),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Father Name: %s"%(fathername),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Mother Name: %s"%(mothername),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Mobile No: %s"%(mobile),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Email Id: %s"%(emailid),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Address: %s"%(address),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Matric Aggregate: %s"%(matric_agg),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Senior Secondary: %s"%(sen_secc),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Course: %s"%(courses),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    Label(f1,text="Department: %s"%(department),font="times_roman 15 bold",bg="#808080",fg="white").pack(padx=5,pady=10)
    f1.pack()
    r.mainloop()
    cur1.close()
    connn.close()
root = Tk()
root.geometry("350x150+0+0")
root.minsize(350,150)
root.maxsize(350,150)
root.title("ID ENTRY")
f= Frame(root)
Label(f,text="Entry",font="times_roman 15 bold",fg="red").pack()
f.pack()
f1 = Frame(root)
Label(f1,text="Rollno: ",font="times_roman 15 bold").grid(row=0,column=0,pady=10)
id = StringVar()
Entry(f1,textvariable=id,font="times_roman 15 bold").grid(row=0,column=1,pady=10)
f1.pack()
f2 = Frame(root)
Button(f2,text="Read",font="times_roman 10 bold",command=read1).pack(pady=10)
f2.pack()
root.mainloop()