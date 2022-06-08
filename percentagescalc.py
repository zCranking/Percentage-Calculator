from tkinter import *
from tkinter import messagebox
import math as Math
import random

root = Tk()
root.geometry("700x700")
root.config(background="#004777")
root.title("Python Caculator")

grade3percent = Label(root, bg="#004777", foreground="#FF7700", font=("Comic Sans MS", "34", "bold"))
grade5percent = Label(root, bg="#004777", foreground="#FF7700", font=("Comic Sans MS", "34", "bold"))
grade10percent = Label(root, bg="#004777", foreground="#FF7700", font=("Comic Sans MS", "34", "bold"))

class grade3():
    def __init__(self, language, math):
        self.lan = language
        self.math = math
    def lan(self):
        return str(self.lan)
    
    def math(self):
        return str(self.math)
    
    def percentage(self):
        lanMarks = self.lan
        mathMarks = self.math    
        total = lanMarks + mathMarks
        total100 = total * 100
        grade3final = Math.floor(total100 / 200)
        grade3percent['text'] = str(grade3final) + "%"

class grade5():
    def __init__(self, language, math, history):
        self.lan = language
        self.math = math
        self.history = history
        
    def lan(self):
        return str(self.lan)
    
    def math(self):
        return str(self.math)
    
    def history(self):
        return str(self.history)
    
    def percentage(self):
        lanMarks = self.lan
        mathMarks = self.math    
        historyMarks = self.history
        total = lanMarks + mathMarks + historyMarks
        total100 = total * 100
        grade5final = Math.floor(total100 / 300)
        grade5percent['text'] = str(grade5final) + "%"

class grade10():
    def __init__(self, language, math, history, flanguage):
        self.lan = language
        self.math = math
        self.history = history
        self.flanguage = flanguage
        
    def lan(self):
        return str(self.lan)
    
    def math(self):
        return str(self.math)
    
    def history(self):
        return str(self.history)
    
    def flanguage(self):
        return str(self.flanguage)
    
    def percentage(self):
        lanMarks = self.lan
        mathMarks = self.math    
        historyMarks = self.history
        flanguageMarks = self.flanguage
        total = lanMarks + mathMarks + historyMarks + flanguageMarks
        total100 = total * 100
        grade10final = Math.floor(total100 / 400)
        grade10percent['text'] = str(grade10final) + "%"

lan = random.randint(40, 100)
math = random.randint(40, 100)
history = random.randint(40, 100)
flan = random.randint(40, 100)

grade3 = grade3(lan, math)
grade3button = Button(root, text="Grade 3 Percentage!", bg="#CC0000", foreground="#FF7700", font=("Comic Sans MS", "12", "normal"), command=grade3.percentage)
grade3button.place(relx=0.2, rely=0.8, anchor=CENTER)
grade3percent.place(relx=0.2 , rely=0.6, anchor=CENTER)

grade5 = grade5(lan, math, history)
grade5button = Button(root, text="Grade 5 Percentage!", bg="#CC0000", foreground="#FF7700", font=("Comic Sans MS", "12", "normal"), command = grade5.percentage)
grade5button.place(relx=0.5, rely=0.8, anchor=CENTER)
grade5percent.place(relx=0.5, rely=0.6, anchor=CENTER)

grade10 = grade10(lan, math, history, flan)
grade10button = Button(root, text="Grade 10 Percentage!", bg="#CC0000", foreground="#FF7700", font=("Comic Sans MS", "12", "normal"), command = grade10.percentage)
grade10button.place(relx=0.8, rely=0.8, anchor=CENTER)
grade10percent.place(relx=0.8, rely=0.6, anchor=CENTER)
root.mainloop()