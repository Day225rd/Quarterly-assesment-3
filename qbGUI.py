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
        root.geometry("400x400")

        self.label = ttk.Label(master,text = "Welcome to the quizbowl game!")
        self.label.place(x=100,y=50)

        
        #radio button for courses
        click = StringVar(root)
        self.radiobutton = ttk.Radiobutton(root, text = "Rainbow six" ,variable = click, value = "Rainbow six")
        self.radiobutton.place(x=180,y=220)

        self.radiobutton = ttk.Radiobutton(root, text ="Terraria" ,variable = click, value = "Terraria")
        self.radiobutton.place(x=180,y=200)

        self.radiobutton = ttk.Radiobutton(root, text ="OW2" ,variable = click, value = "OW2")
        self.radiobutton.place(x=180,y=180)

        self.radiobutton = ttk.Radiobutton(root, text = "Darksouls 3" ,variable = click, value = "Darksouls 3")
        self.radiobutton.place(x=180,y=160)            

        self.radiobutton = ttk.Radiobutton(root, text = "Elden Ring", variable = click, value = "Elden Ring")
        self.radiobutton.place(x=180,y=140)  

qBapp = QuizBowlApp(root)
root.mainloop()

