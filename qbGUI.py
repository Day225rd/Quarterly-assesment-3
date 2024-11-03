import tkinter as tk

from tkinter import *

from tkinter import ttk

import sqlite3


#database connecction
con = sqlite3.connect('quizBowldb.db')
cur = con.cursor()

#class for buttons and text box
#class contains the interactive elements

root =tk.Tk()
root.title("ULTIMATE QUIZBOWL")

class QuizBowlApp:
    def __init__(self,master):
        root.geometry("450x450")

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

        self.btn1 = ttk.Button(root, text = "Press to start!")
        self.btn1.place (x=180,y=240)

    def selection(self):
        cur = self.conn.cur()
        cur.execute('''SELECT DISTINCT course FROM question''')
        courses = [row[0] for row in cur.fetchall()]
        return courses
    
    # def start(self):
        

# class QuizBowlquestionWindow:
#     def __init__(self,master):


qBapp = QuizBowlApp(root)
root.mainloop()

