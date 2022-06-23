#-------------------Faculty Module--------------
import os
from tkinter import *
import cx_Oracle
def bac():
    root.destroy()
    os.system("homescreen.py")
root = Tk()
conn = cx_Oracle.connect("scott/tiger")
cur1 = conn.cursor()
cur1.execute("select * from faculty")
ls = cur1.fetchall()
cur1.close()
root.title("Courses")
widh = root.winfo_screenwidth()
hifh = root.winfo_screenheight()
rows_len = len(ls)
columns_len = len(ls[0])
root.geometry("%dx%d+0+0"%(widh,hifh))
f1 = Frame(root)
Label(f1,text="HOD Faculty Members",font="times_roman 20 bold",fg="red").pack(padx=10,pady=10)
f1.pack()
f2 = Frame(root,bg="white")
Label(f2,text="Name",font="times_roman 15 bold",bg="white",width=20).grid(row=0,column=0)
Label(f2,text="Mobile No",font="times_roman 15 bold",bg="white",width=30).grid(row=0,column=1)
Label(f2,text="Department",font="times_roman 15 bold",bg="white",width=30).grid(row=0,column=2)
Label(f2,text="Email Id",font="times_roman 15 bold",bg="white",width=20).grid(row=0,column=3)
f2.pack()
f3 = Frame(root)
for i in range(rows_len):
    for j in range(columns_len):
        e = Entry(f3,width=30,font="times_roman 15 bold")
        e.grid(row=i,column=j)
        e.insert(END,ls[i][j])
        e.config(state="disable")
f3.pack()
f4 = Frame(root)
Button(f4,text="Back",command=bac).pack(pady=30,padx=30)
f4.pack()
root.mainloop()


