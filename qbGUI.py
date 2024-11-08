import tkinter as tk

from tkinter import *

from tkinter import ttk

from tkinter import messagebox

import sqlite3


#database connecction

con = sqlite3.connect('quizBowlDB2.db')
cur = con.cursor()

#class for buttons and text box
#class contains the interactive elements

root =tk.Tk()
style = ttk.Style(root)
style.theme_use('classic') 
root.configure(bg="lightblue")
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
        self.click = StringVar(root)
        self.radiobutton = ttk.Radiobutton(root, text = "Math" ,variable = self.click, value = "math")
        self.radiobutton.place(x=180,y=220)

        self.radiobutton = ttk.Radiobutton(root, text ="English" ,variable = self.click, value = "English")
        self.radiobutton.place(x=180,y=200)

        self.radiobutton = ttk.Radiobutton(root, text ="IT" ,variable = self.click, value = "IT")
        self.radiobutton.place(x=180,y=180)

        self.radiobutton = ttk.Radiobutton(root, text = "Science" ,variable = self.click, value = "Science")
        self.radiobutton.place(x=180,y=160)            

        self.radiobutton = ttk.Radiobutton(root, text = "History", variable = self.click, value = "History")
        self.radiobutton.place(x=180,y=140)  

        self.btn1 = ttk.Button(root, text = "Press to start!", command = self.new_window)
        self.btn1.place (x=150,y=240)

    
        
    def new_window(self):
        selectedcourse = self.click.get()
        new_window = New_window(self.m, selectedcourse)

class New_window:
    def __init__(self,master,course):
        root.geometry("450x450")

        root.configure(bg="lightblue")

        self.current_question = 0
        self.score = 0
        self.course = course

        self.newwindow = tk.Toplevel(master)
        self.newwindow.title("Questions")
        self.newwindow.geometry("500x500")

        self.label1 = tk.Label(self.newwindow,text = "Please enter the correct answer below")
        self.label1.place(x = 30, y = 40)

        self.label1 = ttk.Label(self.newwindow,text = "Enter text here:")
        self.label1.place(x = 30, y = 80)

        self.answerentry = ttk.Entry(self.newwindow)
        self.answerentry.place(x = 150, y = 110)

        self.btn1 = ttk.Button(self.newwindow, text = "Submit Answer", command = self.check_answer)
        self.btn1.place(x = 30, y = 100)

        self.btn2_next = ttk.Button(self.newwindow, text = "Next question", command = self.next_question)
        self.btn2_next.place(x = 30, y = 130, )

        self.questions = self.load_questions()
        self.load_question()

    def load_questions(self):
        cur.execute(f'''SELECT question, answer FROM {self.course}''')
        return cur.fetchall()
    def load_question(self):
        if self.current_question < len(self.questions):
            questiontext = self.questions[self.current_question][0]
            self.label1.config(text=questiontext)
            self.answerentry.delete(0, tk.END)
        else:
            self.finish_quiz()

    def check_answer(self):
        useranswer = self.answerentry.get()
        correctanswer = self.questions[self.current_question][1]

        if useranswer.lower() == correctanswer.lower():
            messagebox.showinfo("Correct!")
            self.score += 1
        else:
            messagebox.showinfo("incorrect")
        self.answerentry.delete(0, tk.END)
        

    def next_question(self):
        self.current_question += 1
        self.load_question()

    def finish_quiz(self):
        messagebox.showinfo("Quiz finished", f"Your score was {self.score}/10")
        self.newwindow.destroy()
        

 

qBapp = QuizBowlApp(root)
root.mainloop()
