from tkinter import *
names = [] #need an empty names list, that we will add names to it, so we can keep track of players and use them later for score board

class Quizstarter:  
    def __init__(self, parent):#constructor, The _init_() function us called automatically every time the class is being used to create a new object.
        
        background_color="OldLace"# to set it as background color for all the label widgets
        
        #Frame set up
        self.quiz_frame=Frame(parent, bg=background_color, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders._
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parents widget.
        
        #Label widget for the heading
        self.heading_label=Label(self.quiz_frame, text="NZ Road Rules", font=("Tw Cen MT","18", "bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20)