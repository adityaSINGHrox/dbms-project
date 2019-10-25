from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('codemy.com')
root.geometry("400x400")

#create a database or connect it to one
conn = sqlite3.connect('employee.db')

#create cursor,command and returns
c = conn.cursor()


#topframe = None
#create a database or connect it to one
conn = sqlite3.connect('employee.db')

#create cursor,command and returns
c = conn.cursor()

#topframe = tkinter.Frame(root).pack()

myLabel1 = Label(root, text = "MENTALHEALTHCARE", bg = 'blue', font = 'Times 16 bold italic')
myLabel1.grid()


def employee():
	editor = Tk()
	editor.title('codemy.com')
	editor.geometry("400x400")

	#create a database or connect it to one
	conn = sqlite3.connect('employee.db')

	#create cursor,command and returns
	c = conn.cursor()

	def delete():
		#create a database or connect it to one
		conn = sqlite3.connect('employee.db')

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
		conn = sqlite3.connect('employee.db')

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

'''	def edit():
	    conn = sqlite3.connect('employee.db')

		# CREATE cursor
		#c = conn.cursor()
		#query the database
		c.execute("SELECT * FROM disease WHERE oid = " + delete_box.get())
		records = c.fetchall()
	
	
		# create text boxes
		EID_editor = Entry(editor, width=30)
		EID_editor.grid(row=12, column=1, padx=20, pady = (10, 0))

		Ename_editor = Entry(editor, width=30)
		Ename_editor.grid(row=13, column=1)

		phono_editor = Entry(editor, width=30)
		phono_editor.grid(row=14, column=1, padx=20, pady = (10, 0))

		address_editor = Entry(editor, width=30)
		address_editor.grid(row=15, column=1, padx=20, pady = (10, 0))

 		job_des_editor = Entry(editor, width=30)
		job_des_editor.grid(row=16, column=1, padx=20, pady = (10, 0))


		sal_editor = Entry(editor, width=30)
		sal_editor.grid(row=17, column=1, padx=20, pady = (10, 0))

		# create text box labels
		EID_label = Label(editor, text="Eid")
		EID_label.grid(row=12, column=0, pady = (10, 0))

		Ename_label = Label(editor, text="Ename")
		Ename_label.grid(row=13, column=0)

		
		phono_label = Label(editor, text="phono")
		phono_label.grid(row=14, column=0)



		address_label = Label(editor, text="address")
		address_label.grid(row=15, column=0)



		job_des_label = Label(editor, text="job_des")
		job_des_label.grid(row=16, column=0)



		sal_label = Label(editor, text="sal")
		sal_label.grid(row=17, column=0)

	#loop thru results
		for record in records:
			EID_editor.insert(0, record[0])
			Ename_editor.insert(0, record[1])
			phono_editor = insert(0, record[2])
			address_editor = insert(0, record[3])
			sal_label = insert(0, record[4])	

	#create a save button to save record
		edit_btn = Button(editor, text= "save record", command= edit)
		edit_btn.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

		c.commit()

		c.close()'''
	


	#CREATE query function
	def query():
		#create a database or connect it to one
		conn = sqlite3.connect('employee.db')

		#create cursor,command and returns
		c = conn.cursor()
		
		#query the database
		c.execute("SELECT *, oid FROM Employee")	
		records = c.fetchall()
		#print(records)

		#loop thru results
		print_records = ''
		for record in records:
			print_records += str(record) + "\n"


		query_label = Label(editor, text = print_records)
		query_label.grid(row = 11, column = 0, columnspan = 2)

		#commit changes
		conn.commit()

		#class connection 
		conn.close()
	

	EID = Entry(editor, width = 30)
	EID.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

	Ename = Entry(editor, width = 30)
	Ename.grid(row = 1, column = 1)

	phno = Entry(editor, width = 30)
	phno.grid(row = 2, column = 1)

	address = Entry(editor, width = 30)
	address.grid(row = 3, column = 1)

	job_des = Entry(editor, width = 30)
	job_des.grid(row = 4, column = 1)

	sal = Entry(editor, width = 30)
	sal.grid(row = 5, column = 1)

	delete_box = Entry(editor, width = 30)
	delete_box.grid(row = 9, column = 1, pady = 5)

	#create text box labels
	EID_label = Label(editor, text = "EID")
	EID_label.grid(row = 0,column = 0, pady = (10,0))

	Ename_label = Label(editor, text = "Ename")
	Ename_label.grid(row = 1,column = 0)

	phno_label = Label(editor, text = "phono")
	phno_label.grid(row = 2,column = 0)

	address_label = Label(editor, text = "Address")
	address_label.grid(row = 3,column = 0)

	job_des_label = Label(editor, text = "job_des")
	job_des_label.grid(row = 4,column = 0)

	sal_label = Label(editor, text = "sal")
	sal_label.grid(row = 5,column = 0)

	delete_box_label = Label(editor, text = "id number")
	delete_box_label.grid(row = 9 , column =0, pady =5)


	submit_btn = Button(editor, text = "add record to database", command = submit)
	submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

	query_btn = Button(editor, text = "show records", command = query)
	query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 137)


	delete_btn = Button(editor, text = "delete records", command = delete)
	delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 136)

	#create update
	#edit_btn = Button(root, text = "update records", command = edit)
	#edit_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 143)


	conn.commit()


	conn.close() 

	

def patient():
	#create a database or connect it to one
	conn = sqlite3.connect('employee.db')

	#create cursor,command and returns
	c = conn.cursor()

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

def appointments():
	#create a database or connect it to one
	conn = sqlite3.connect('employee.db')

	#create cursor,command and returns
	c = conn.cursor()

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

def prescription():
	#create a database or connect it to one
	conn = sqlite3.connect('employee.db')

	#create cursor,command and returns
	c = conn.cursor()

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

def disease():
	#create a database or connect it to one
	conn = sqlite3.connect('employee.db')

	#create cursor,command and returns
	c = conn.cursor()

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

employee_btn = Button(root, text = "employee", command = employee)
employee_btn.grid(row = 1, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 100)

patient_btn = Button(root, text = "patient", command = patient)
patient_btn.grid(row = 2, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 100)


appointments_btn = Button(root, text = "appointments", command = appointments)
appointments_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 100)


prescription_btn = Button(root, text = "prescription", command = prescription)
prescription_btn.grid(row = 4, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 100)


disease_btn = Button(root, text = "disease", command = disease)
disease_btn.grid(row = 5, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 100)


conn.commit()

conn.close() 

'''
c.execute("""CREATE TABLE  Employee (
			EID text PRIMARY KEY,
			Ename text,
			phno integer,
			address text,
			job_des text,
			sal integer
			)""")
'''

root.mainloop()