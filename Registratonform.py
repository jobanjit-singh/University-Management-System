#-------------------Registration Form Module-----------------
from tkinter import *
import os
import cx_Oracle as co
from tkinter import messagebox
def cancel1():
    ro.destroy()
    os.system("admin.py")
def sub():
    fnameval = fname.get()
    lnameval = lname.get()
    mothernameval = mothername.get()
    fathernameval = fathername.get()
    mobileval = Mobile.get()
    emailval = email.get()
    addressval = Add.get()
    matval = matricagg.get()
    sensecval = sen_secc.get()
    coursedetval = coursedet.get()
    departval = depart.get()
    if fnameval==''and lnameval=='' and mothernameval=='' and fathernameval=='' and mobileval=='' and emailval=='' and addressval=='' and matval=='' and sensecval=='' and coursedetval=='Select' and departval=='Select':
        messagebox.showinfo("Registration Form","Entry is Empty")
    elif fnameval==''or lnameval=='' or mothernameval=='' or fathernameval=='' or mobileval=='' or emailval=='' or addressval=='' or matval=='' or sensecval=='' or coursedetval=='Select' or departval=='Select':
        messagebox.showinfo("Registration Form","Entry is Empty")
    else:
        try:
            con = co.connect("scott/tiger")
            cur = con.cursor()
            cur.execute("insert into student1(fname,lname,father_name,mother_name,mobile_no,email_id,address,matric_agg,sen_sec,course,department) values (:fnameval,:lnameval,:fathernameval,:mothernameval,:mobileval,:emailval,:addressval,:matval,:sensecval,:coursedetval,:departval)",{":fnameval":fnameval,":lnameval":lnameval,":fathernameval":fathernameval,":mothernameval":mothernameval,":mobileval":int(mobileval),":emailval":emailval,":addressval":addressval,":matval":int(matval),":sensecval":int(sensecval),":coursedetval":coursedetval,":departval":departval})
            con.commit()
            cur.close()
            con.close()
            ro.destroy()
            messagebox.showinfo("Registration Form","Form Submmitted Successfully")
            os.system("Registratonform.py")
        except:
            ro.destroy()
            messagebox.showwarning("Registration Form","Enter Valid Data")
            os.system("Registratonform.py")
ro = Tk()
ro.config(bg="white")
width1 = ro.winfo_screenwidth()
height1 = ro.winfo_screenheight()
ro.geometry("%dx%d+0+0"%(width1,height1))
ro.title("Registration Form")
#Frame 1
f1 = Frame(ro)
L1 = Label(f1,text="Registration Form",font="times_romans 40 bold",fg="red",bg="white")
L1.config(anchor=CENTER)
L1.pack()
f1.pack()
#Frame 2
f2 = Frame(ro,bg="#808080")
fname = StringVar()
lname = StringVar()
fathername = StringVar()
mothername = StringVar()
Mobile = StringVar()
email = StringVar()
Add = StringVar()
l1 = Label(f2,text="First Name:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=0,column=0,padx=10,pady=10,sticky="w")
l2 = Label(f2,text="Last Name:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=1,column=0,padx=10,pady=10,sticky="w")
l3 = Label(f2,text="Father's Name:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=2,column=0,padx=10,pady=10,sticky="w")
l4 = Label(f2,text="Mother's Name:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=3,column=0,padx=10,pady=10,sticky="w")
l5 = Label(f2,text="Mobile No.:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=4,column=0,padx=10,pady=10,sticky="w")
l6 = Label(f2,text="Email ID:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=5,column=0,padx=10,pady=10,sticky="w")
l4 = Label(f2,text="Address:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=6,column=0,padx=10,pady=10,sticky="w")
efname = Entry(f2,textvariable=fname,font="times_roman 15 bold").grid(row=0,column=1,padx=10,pady=10,sticky="w")
elname = Entry(f2,textvariable=lname,font="times_roman 15 bold").grid(row=1,column=1,padx=10,pady=10,sticky="w")
efathername = Entry(f2,textvariable=fathername,font="times_roman 15 bold").grid(row=2,column=1,padx=10,pady=10,sticky="w")
emothername = Entry(f2,textvariable=mothername,font="times_roman 15 bold").grid(row=3,column=1,padx=10,pady=10,sticky="w")
emobileno = Entry(f2,textvariable=Mobile,font="times_roman 15 bold").grid(row=4,column=1,padx=10,pady=10,sticky="w")
emailid = Entry(f2,textvariable=email,font="times_roman 15 bold").grid(row=5,column=1,padx=10,pady=10,sticky="w")
eaddress = Entry(f2,textvariable=Add,font="times_roman 15 bold").grid(row=6,column=1,padx=10,pady=10,sticky="w")
matricagg = StringVar()
sen_secc = StringVar()
coursedet = StringVar()
coursedet.set('Select')
depart = StringVar()
depart.set("Select")
l1 = Label(f2,text="Matric Aggregate's:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=7,column=0,padx=10,pady=10,sticky="w")
l2 = Label(f2,text="Sen_Sec:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=8,column=0,padx=10,pady=10,sticky="w")
l3 = Label(f2,text="Course:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=9,column=0,padx=10,pady=10,sticky="w")
l4 = Label(f2,text="Department:",fg="white",bg="#808080",font="times_roman 15 bold").grid(row=10,column=0,padx=10,pady=10,sticky="w")
emat = Entry(f2,textvariable=matricagg,font="times_roman 15 bold").grid(row=7,column=1,padx=10,pady=10,sticky="w")
sendata = Entry(f2,textvariable=sen_secc,font="times_roman 15 bold").grid(row=8,column=1,padx=10,pady=10,sticky="w")
courses = OptionMenu(f2,coursedet,'B.Tech','Management','Computer Application','Pharmacy').grid(row=9,column=1,padx=10,pady=10,sticky="w")
dep = OptionMenu(f2,depart,'CSE','CE','ECE','ME','BBA','B.COM(HONS)','MBA','B.A','BCA','MCA','B.PHARMACY','D.PHARMACY','B.Sc').grid(row=10,column=1,padx=10,pady=10,sticky="w")
f2.pack()

# Frame 3

f3=Frame(ro,bg="white")
b1 = Button(f3,text="Submit",bg="#808080",command=sub,fg="white",borderwidth=3).grid(row=0,column=0,padx=10,pady=10)
b2 = Button(f3,text="Cancel",bg="#808080",fg="white",borderwidth=3,command=cancel1).grid(row=0,column=1,padx=10,pady=10)
f3.pack()
ro.mainloop()