import tkinter as tk

from tkinter import *

from tkinter import ttk

import sqlite3


#database connecction

con = sqlite3.connect('quizBowlDB2.db')
cur = con.cursor()

#class for buttons and text box
#class contains the interactive elements

root =tk.Tk()
root.title("ULTIMATE QUIZBOWL")


class QuizBowlApp:
    def __init__(self,master):
        root.geometry("450x450")

        self.m = master



        self.label = ttk.Label(master,text = "Welcome to the quizbowl game!")
        self.label.place(x=100,y=50)

        self.label = ttk.Label(master, text = "Please select a topic, then press start when you are ready.")
        self.label.place(x=100,y=120)

        
        #radio button for courses
        click = StringVar(root)
        self.radiobutton = ttk.Radiobutton(root, text = "Math" ,variable = click, value = "Rainbow six")
        self.radiobutton.place(x=180,y=220)

        self.radiobutton = ttk.Radiobutton(root, text ="English" ,variable = click, value = "Terraria")
        self.radiobutton.place(x=180,y=200)

        self.radiobutton = ttk.Radiobutton(root, text ="IT" ,variable = click, value = "OW2")
        self.radiobutton.place(x=180,y=180)

        self.radiobutton = ttk.Radiobutton(root, text = "Geology" ,variable = click, value = "Darksouls 3")
        self.radiobutton.place(x=180,y=160)            

        self.radiobutton = ttk.Radiobutton(root, text = "Random", variable = click, value = "Elden Ring")
        self.radiobutton.place(x=180,y=140)  

        self.btn1 = ttk.Button(root, text = "Press to start!", command = self.opennew_window)
        self.btn1.place (x=180,y=240)

    def obtaincourse(self):
            cur = self.conn.cursor()
            cur.execute('''SELECT DISTINCT course FROM Course''')
            courses = [row[0] for row in cur.fetchall()]
            return courses
        
    def opennew_window(self):
        new_window(self.m)

class new_window:
    def __init__(self,master):
        root.geometry("450x450")


        self.newwindow = tk.Toplevel(master)
        self.newwindow.title("Questions")

        self.label1 = tk.Label(self.newwindow,text = "Please enter the correct answer below")
        self.label1.place(x = 30, y = 40)

        self.label1 = ttk.Label(self.newwindow,text = "Enter text here:")
        self.label1.place(x = 30, y = 80)

        self.txtfield1 = ttk.Entry(self.newwindow)
        self.txtfield1.place(x = 130, y = 80)

        self.btn1 = ttk.Button(self.newwindow, text = "Submit Answer")
        self.btn1.place(x = 30, y = 100)


        cur.execute('''SELECT DISTINCT question FROM Math''')
        questionmath = cur.fetchone()
        self.label1 = tk.Label(self.newwindow, text = questionmath)
        self.label1.place(x = 30, y = 60)

qBapp = QuizBowlApp(root)
root.mainloop()
