from tkinter import * 
import sqlite3
import os

root = Tk()
os.system('clear')
root.title('codemy.com')
root.geometry("400x400")

# create a database or connect to one
conn = sqlite3.connect('database.db')

# create cursor
c = conn.cursor()


# create table
'''
c.execute("""CREATE TABLE disease (
			DI_ID integer,
			DI_name text
			)""")

'''
# create function to edit record
def edit():
	editor = Tk()
	editor.title('update a record')
	editor.geometry("400x400")

	# create a database or connect to one
	conn = sqlite3.connect('database.db')

	# CREATE cursor
	c = conn.cursor()

	record_id = delete_box.get()
	#query the database
	c.execute("SELECT * FROM disease WHERE oid = " + record_id)
	records = c.fetchall()
	
	
	# create text boxes
	DI_ID_editor = Entry(editor, width=30)
	DI_ID_editor.grid(row=0, column=1, padx=20, pady = (10, 0))

	DI_name_editor = Entry(editor, width=30)
	DI_name_editor.grid(row=1, column=1)

	# create text box labels
	DI_ID_label = Label(editor, text="disease id")
	DI_ID_label.grid(row=0, column=0, pady = (10, 0))

	DI_name_label = Label(editor, text="disease name")
	DI_name_label.grid(row=1, column=0)

	#loop thru results
	for record in records:
		DI_ID_editor.insert(0, record[0])
		DI_name_editor.insert(0, record[1])


	#create a save button to save record
	edit_btn = Button(editor, text= "save record", command= edit)
	edit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=145)



# create function to delete a record
def delete():
	# create a database or connect to one
	conn = sqlite3.connect('database.db')
	# create cursor
	c = conn.cursor()

	# delete a record
	c.execute("DELETE from disease WHERE oid = " + delete_box.get())

	# commit changes
	conn.commit()
	# close connections
	conn.close()




#create submit function for database
def submit():
	# create a database or connect to one
	conn = sqlite3.connect('database.db')
	# create cursor
	c = conn.cursor()

	# insert into table
	c.execute("INSERT INTO disease VALUES (:DI_ID, :DI_name)",
			{
			'DI_ID': DI_ID.get(),
			'DI_name': DI_name.get()
			})



	
	# commit changes
	conn.commit()
	# close connections
	conn.close()

	
	# clear text boxes
	DI_ID.delete(0, END)
	DI_name.delete(0, END)

	# create query function
def query():
	# create a database or connect to one
	conn = sqlite3.connect('database.db')

	# CREATE cursor
	c = conn.cursor()

	#query the database
	c.execute("SELECT *, oid FROM disease")
	records = c.fetchall()
	print(records)

	# loop through results
	print_records = ''
	for record in records:
		print_records += str(record) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row= 8, column= 0, columnspan= 2)

	# commit changes
	conn.commit()
	# close connections
	conn.close()

# create text boxes
DI_ID = Entry(root, width=30)
DI_ID.grid(row=0, column=1, padx=20, pady = (10, 0))

DI_name = Entry(root, width=30)
DI_name.grid(row=1, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=5, column=1)

# create text box labels
DI_ID_label = Label(root, text="disease id")
DI_ID_label.grid(row=0, column=0, pady = (10, 0))

DI_name_label = Label(root, text="disease name")
DI_name_label.grid(row=1, column=0)

delete_box_label = Label(root, text="ID Number")
delete_box_label.grid(row=5, column=0)

# create submit button
submit_btn = Button(root, text="add record to database", command= submit)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create a query button
query_btn = Button(root, text= "show records", command= query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create a delete button
delete_btn = Button(root, text= "delete record", command= delete)
delete_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

#create an update button
edit_btn = Button(root, text= "edit record", command= edit)
edit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=143)



# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()



