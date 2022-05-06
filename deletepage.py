from tkinter import *
import cx_Oracle as co
from tkinter import messagebox
root = Tk()
root.geometry("400x200+0+0")
root.config(bg="white")
root.minsize(400,200)
root.maxsize(400,200)
root.title("Delete Data")
def dele():
    conn = co.connect("scott/tiger")
    curone = conn.cursor()
    idval = id1.get()
    if idval =='':
        messagebox.showinfo("Delete Record","Entry is Empty")
    elif idval!='':
        curone.execute("select s_no from student1 where s_no=:id2",{":id2":int(idval)})
        ls = curone.fetchall()
        print(ls)
        if ls == []:
               messagebox.showinfo("Delete Record","Please enter valid rollno") 
        else:
            for i in ls:
            # if i==idrol:
                curone.execute("Delete from student1 where s_no=:id2",{":id2":int(idval)})
                conn.commit()
                messagebox.showinfo("Delete Record","Record Deletion Successful")
    curone.close()
    conn.close()
#Frame 1
f1 = Frame(root,bg="white")
Label(f1,text="Delete Data",font="times_roman 20 bold",bg="white",fg="red").pack(padx=10,pady=10)
# Frame 2
f2 = Frame(root,bg="white")
Label(f2,text="Roll No",font="times_roman 15 bold",bg="white").grid(row=0,column=0)
# Entry
id1 = StringVar()
Entry(f2,textvariable=id1,borderwidth=2,font="times_roman 15 bold").grid(row=0,column=1)
# Frame 3 
f3 = Frame(root,bg="white")
Button(f3,text="Delete Record",borderwidth=2,command=dele).pack(padx=10,pady=10)
f1.pack()
f2.pack()
f3.pack()
root.mainloop()