import tkinter as tk

from tkinter import *

from tkinter import ttk

import sqlite3



#database connecction
con = sqlite3.connect('newDB.db')
cur = con.cursor()

root =tk.Tk()
root.title("ULTIMATE QUIZBOWL")
#class for buttons and text box
#class contains the interactive elements
class QuizBowlApp:
    def __init__(self,master):
        root.geometry('600x600')

        self.label = ttk.Label(master,text = "Welcome to the quizbowl game!")
        self.label.place(x=50, y=500)



root.mainloop()
