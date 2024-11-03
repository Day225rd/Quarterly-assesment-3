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

        self.label1 = ttk.Label(master,text = "Welcome")
        self.label1.place(x = 170, y = 40)

        self.label = ttk.Label(master,text = "Welcome to the quizbowl game!")
        self.label.place(x=100,y=50)



root.mainloop()

