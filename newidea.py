import tkinter as tk

from tkinter import *

from tkinter import ttk

import sqlite3



#database connecction
con = sqlite3.connect('newDB.db')
cur = con.cursor()

root =tk.Tk()
root.title("Feedback")
#class for buttons and text box
class FeedbackApp:
    def __init__(self,master):
        root.geometry('400x400')

        #welcome statement
        self.label1 = ttk.Label(master,text = "Welcome")
        self.label1.place(x = 170, y = 40)
        
        self.label1 = ttk.Label(master,text = "Please complete the following fields below")
        self.label1.place(x = 80, y = 70)

        #submit feedback button
        self.btn1 = ttk.Button(master, text = "Submit Feedback", command = self.fbsubmit)
        self.btn1.config(command = self.buttontext)
        self.btn1.place(x = 150, y = 220)

        #feedback label and text field
        self.label1 = ttk.Label(master,text = "Feedback:")
        self.label1.place(x = 30, y = 190)
        self.txtfield1 = tk.Text(master)
        self.txtfield1.place(x = 140, y = 190, width = 130, height = 80)

        #name label and text field
        self.label2 = ttk.Label(master,text = "Name:")
        self.label2.place(x = 30, y = 130)
        self.txtfield2 = ttk.Entry(master)
        self.txtfield2.place(x = 140, y = 130)
        
        #Email label and text field
        self.label3 = ttk.Label(master,text = "Email:")
        self.label3.place(x = 30, y = 160)
        self.txtfield3 = ttk.Entry(master)
        self.txtfield3.place(x = 140, y = 160)

        #Phone number label and text field
        self.label4 = ttk.Label(master,text = "Phone Number:")
        self.label4.place(x = 30, y = 100)
        self.txtfield4 = ttk.Entry(master)
        self.txtfield4.place(x = 140, y = 100)

        #Submit button
        self.submitButton = ttk.Button(master, text = "Submit", command = self.fbsubmit)
        self.submitButton.config(command = self.buttontext() )
        self.submitButton.place(x=140,y=300)

        #past entries button
        self.historyButton = ttk.Button(master, text = "Check past entries", command = self.fbhistorypassword)
        self.historyButton.config(command = self.buttontext() )
        self.historyButton.place(x=140,y=330)

    #password for data history
    def fbhistorypassword(self):
        while True:
            password = input("Please enter the password ->")
            if password == "1":
                return (self.history())
            else:
                print("Incorrect password")
    
    #the history of data submissions
    def history(self):
        cur.execute('''SELECT * FROM feedback''')
        print(cur.fetchall())
        

        #grabbing the text input
    def txtprint(self):
        textentry = self.txtfield1.get("1.0", "end-1c"), self.txtfield2.get(), self.txtfield3.get(), self.txtfield4.get()
        print(textentry)

    def buttontext(self):
        print()

    
    #function for adding text fields to database
    def fbsubmit(self):
        number = self.txtfield4.get()
        name = self.txtfield2.get()
        email = self.txtfield3.get()
        feedback = self.txtfield1.get("1.0", "end-1c")
        values = [number, name, email, feedback]
        cur.execute('''INSERT INTO Feedback
                    (number ,name ,email ,feedback) 
                    VALUES (?, ?, ?, ?)''', values)
    

        con.commit()

        print("Feedback submitted")

fbapp = FeedbackApp(root)
root.mainloop()
con.close()


#/////////////////////////////
# button1 = ttk.Button(root)
# button1.config(text="Click here")
# button1.grid()

