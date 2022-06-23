#-----------------------Result Module----------------
import os
from tkinter import *
from tkinter import messagebox
import cx_Oracle
def bac():
    root.destroy()
    os.system("student.py")
root = Tk()
conn = cx_Oracle.connect("scott/tiger")
cur1 = conn.cursor()
cur1.execute("select fname,course,department,grade from uni_record,result where uni_record.u_rollno=result.uni_rollno")
ls = cur1.fetchall()
cur1.close()
root.title("Result Tabular Form")
widh = root.winfo_screenwidth()
hifh = root.winfo_screenheight()
rows_len = len(ls)
columns_len = len(ls[0])
root.geometry("%dx%d+0+0"%(widh,hifh))
f1 = Frame(root)
Label(f1,text="Result Tabular Form",font="times_roman 20 bold",fg="red").pack(padx=20,pady=20)
f1.pack()
f2 = Frame(root,bg="white")
Label(f2,text="Name",font="times_roman 15 bold",bg="white",width=20).grid(row=0,column=0)
Label(f2,text="Course",font="times_roman 15 bold",bg="white",width=20).grid(row=0,column=1)
Label(f2,text="Department",font="times_roman 15 bold",bg="white",width=20).grid(row=0,column=2)
Label(f2,text="Result(in CGPA)",font="times_roman 15 bold",bg="white",width=20).grid(row=0,column=3)
f2.pack()
f3 = Frame(root)
for i in range(rows_len):
    for j in range(columns_len):
        try:
            e = Entry(f3,width=20,font="times_roman 15 bold")
            e.grid(row=i,column=j)
            e.insert(END,ls[i][j])
            e.config(state="disable")
        except:
            messagebox.showinfo("Result Page","Not Declared")
f3.pack()
f4 = Frame(root)
Button(f4,text="Back",command=bac).pack(pady=30,padx=30)
f4.pack()
root.mainloop()

