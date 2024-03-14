from tkinter import *

class Student:
    def__init__(self, name): # type: ignore
        self.first_name = name

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

def show_grade():
    # Show the grade using a label
    grade_label.config(text=csc_2[0].get_grade())
    pass

csc_2 = []

csc_2.append(Student("Bilal"))
csc_2[0]set.set_grade("Excellence")

window = Tk()
window.geometry("300x300")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="show grade")
show_grade_btn.pack()

window.mainloop*()