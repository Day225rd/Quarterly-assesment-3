# import tkinter as tk

# from tkinter import *

# from tkinter import ttk

# root =tk.Tk()
# root.title("ULTIMATE QUIZBOWL")

# class QuizBowlApp:
#     def __init__(self,master):
#         root.geometry("400x400")

#         self.label = ttk.Label(master,text = "Welcome to the quizbowl game!")
#         self.label.place(x=100,y=50)

# qBapp = QuizBowlApp(root)

# root.mainloop()

    def show():
        label1 = Label( text = clicked1.get())

        options1 = [
            "1",
            "2",
            "3",
            "4",
            "5"
        ]

    #drop down menu for courses
        # questions = {"1","2","3","4","5"}
        # click = StringVar(root)
        # self.dropdown_menu = ttk.OptionMenu(root, click, *questions)
        # self.dropdown_menu.place(x=200,y=200)   

        self.radiobutton = ttk.Radiobutton(root, text = click, value = "")
        self.radiobutton.place(x=200,y=200)

        self.radiobutton = ttk.Radiobutton(root, text = click, value = "")
        self.radiobutton.place(x=200,y=180)

        self.radiobutton = ttk.Radiobutton(root, text = click, value = "")
        self.radiobutton.place(x=200,y=160)

        self.radiobutton = ttk.Radiobutton(root, text = click, value = "")
        self.radiobutton.place(x=200,y=140)

        self.radiobutton = ttk.Radiobutton(root, text = click, value = "")
        self.radiobutton.place(x=200,y=120)