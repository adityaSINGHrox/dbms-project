from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('codemy.com')
root.geometry("400x400")

#create a database or connect it to one
conn = sqlite3.connect('mentalHealthCare.db')

#create cursor,command and returns
c = conn.cursor()



c.execute("""CREATE TABLE  Employee (
			EID text,
			Ename text,
			phno integer,
			address text,
			job_des text,
			sal integer
			)""")

'''
def delete():
	#create a database or connect it to one
	conn = sqlite3.connect('mentalHealthCare.db')

	#create cursor,command and returns
	c = conn.cursor()

	#delete a record
	c.execute("DELETE from employee WHERE oid = " + delete_box.get())

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

def submit():
		#create a database or connect it to one
	conn = sqlite3.connect('mentalHealthCare.db')

	#create cursor,command and returns
	c = conn.cursor()
	

	#Insert into values
	c.execute("INSERT INTO Employee VALUES (:EID, :Ename, :phno, :address, :job_des, :sal)",
		{
		 #create dictonary for dummy values using keys
		 'EID' : EID.get(),
		 'Ename' : Ename.get(),
		 'phno': phno.get(),
		 'address'	: address.get(),
		 'job_des': job_des.get(),
		 'sal' : sal.get()
		 }
		 )

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

	EID.delete(0, END)
	Ename.delete(0, END)
	phno.delete(0, END)
	address.delete(0, END)
	job_des.delete(0, END)
	sal.delete(0, END)

#CREATE query function
def query():
	#create a database or connect it to one
	conn = sqlite3.connect('mentalHealthCare.db')

	#create cursor,command and returns
	c = conn.cursor()
	
	#query the database
	c.execute("SELECT *, oid FROM Employee")	
	records = c.fetchall()
	#print(records)

	#loop thru results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[6]) + "\n"


	query_label = Label(root, text = print_records)
	query_label.grid(row = 11, column = 0, columnspan = 2)

	#commit changes
	conn.commit()

	#class connection 
	conn.close()


EID = Entry(root, width = 30)
EID.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

Ename = Entry(root, width = 30)
Ename.grid(row = 1, column = 1)

phno = Entry(root, width = 30)
phno.grid(row = 2, column = 1)

address = Entry(root, width = 30)
address.grid(row = 3, column = 1)

job_des = Entry(root, width = 30)
job_des.grid(row = 4, column = 1)

sal = Entry(root, width = 30)
sal.grid(row = 5, column = 1)

delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1, pady = 5)

#create text box labels
EID_label = Label(root, text = "EID")
EID_label.grid(row = 0,column = 0, pady = (10,0))

Ename_label = Label(root, text = "Ename")
Ename_label.grid(row = 1,column = 0)

phno_label = Label(root, text = "phono")
phno_label.grid(row = 2,column = 0)

address_label = Label(root, text = "Address")
address_label.grid(row = 3,column = 0)

job_des_label = Label(root, text = "job_des")
job_des_label.grid(row = 4,column = 0)

sal_label = Label(root, text = "sal")
sal_label.grid(row = 5,column = 0)

delete_box_label = Label(root, text = "id number")
delete_box_label.grid(row = 9 , column =0, pady =5)


submit_btn = Button(root, text = "add record to database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

query_btn = Button(root, text = "show records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 137)


delete_btn = Button(root, text = "delete records", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 136)

'''
conn.commit()

conn.close() 


root.mainloop()