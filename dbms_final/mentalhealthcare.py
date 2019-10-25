from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('codemy.com')
root.geometry("400x400")

#topframe = None
#create a database or connect it to one
conn = sqlite3.connect('mhc.db')

#create cursor,command and returns
c = conn.cursor()

#topframe = tkinter.Frame(root).pack()

myLabel1 = Label(root, text = "MENTALHEALTHCARE", bg = 'blue', font = 'Times 16 bold italic')
myLabel1.grid()


#heading = tkinter.Label(topframe, text="MENTALHEALTHCARE",bg='cadet blue',fg='',font='Times 16 bold italic')
def employee():
	#create a database or connect it to one
	conn = sqlite3.connect('mhc.db')

	#create cursor,command and returns
	c = conn.cursor()

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

def patient():
	#create a database or connect it to one
	conn = sqlite3.connect('mhc.db')

	#create cursor,command and returns
	c = conn.cursor()

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

def appointments():
	#create a database or connect it to one
	conn = sqlite3.connect('mhc.db')

	#create cursor,command and returns
	c = conn.cursor()

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

def prescription():
	#create a database or connect it to one
	conn = sqlite3.connect('mhc.db')

	#create cursor,command and returns
	c = conn.cursor()

	#commit changes
	conn.commit()

	#class connection 
	conn.close()

def disease():
	#create a database or connect it to one
	conn = sqlite3.connect('mhc.db')

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


root.mainloop()