con = ora.connect("scott/tiger")
cur1 = con.cursor()
ls = cur1.execute("select fname from student1 where s_no=:id;",{":id":id1.get()})
print(ls)
ro = Tk()
ro.title("Name Update")
ro.geometry("400x250+0+0")
ro.minsize(250,400)
ro.maxsize(250,400)
f1 = Frame(ro)
# Labels
Label(f1,text="Old:",font="time_roman 15 bold").grid(row=0,column=0,padx=10,pady=10,sticky="w")
Label(f1,text="New:",font="time_roman 15 bold").grid(row=1,column=0,padx=10,pady=10,sticky="w")
# Entries
Label(f1,text="New:",font="time_roman 15 bold").grid(row=1,column=0,padx=10,pady=10)
