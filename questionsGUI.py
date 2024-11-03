import tkinter as tk

from tkinter import *

from tkinter import ttk

import sqlite3



#database connecction
con = sqlite3.connect('newDB.db')
cur = con.cursor()

root =tk.Tk()

root.title("Feedback")
class QuestionGUI:
    def __init__(self,master):
        root.geometry('400x400')