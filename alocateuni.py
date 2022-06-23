#-------------------Allocate Rollno Module-------------
import os
from tkinter import *
from tkinter import messagebox
import cx_Oracle as cx
conn = cx.connect("scott/tiger")
cur1 = conn.cursor()
cur1.execute("select fname,lname,father_name,mother_name,mobile_no,email_id,address,matric_agg,sen_sec,course,department from student1 order by fname")
ls = cur1.fetchall()
cur1.close()
if ls ==[]:
    messagebox.showinfo("Allocate University Rollno","Already Allocated")
    os.system("admin.py")     
else:
    for i in ls:
        cur2 = conn.cursor()
        cur2.execute("select u_rollno from uni_record")
        ls2 = cur2.fetchall()
        lenght = len(ls2)
        if lenght == 0:
            last = [1999]  
        else:
            last = list(ls2[lenght-1])
        cur2.close()
        firstname = i[0]
        lastname = i[1]
        fathername = i[2]
        mothername = i[3]
        mobileno = i[4]
        emailid = i[5]
        address = i[6]
        matric = i[7]
        senior = i[8]
        course1 = i[9]
        department = i[10]
        print(firstname)
        cur3 = conn.cursor()
        cur3.execute("insert into uni_record (u_rollno,fname,lname,father_name,mother_name,mobile_no,email_id,address,matric_agg,sen_sec,course,department) values (:u_rollno,:fname,:lname,:father_name,:mother_name,:mobile_no,:email_id,:address,:matric_agg,:sen_sec,:course,:department)",{":u_rollno":last[0]+1,":fname":firstname,":lname":lastname,":father_name":fathername,":mother_name":mothername,":mobile_no":int(mobileno),":email_id":emailid,":address":address,":matric_agg":int(matric),":sen_sec":int(senior),":course":course1,":department":department})
        cur3.execute("truncate table student1")
        cur3.execute("insert into login (username,password,position) values ('%s','abc%s','Student')"%(str(last[0]+1),str(last[0]+1)))
        cur3.execute("insert into result (uni_rollno) values ('%d')"%(last[0]+1))
        messagebox.showinfo("Allocate University Rollno","Allocated Successfully")
        cur3.close()
        conn.commit()


