#AS 3.46 ASSESSMENT- TRI_POLYGON

# AUTHOR: Henry Bai
# PROGRAM: AS 3.46 ASSESSMENT- TRI_POLYGON
# VERSION: 1.0

# PURPOSE OF PROGRAM

# Inital program. Due to other solutions to build avaiable, v1 will not be fully developed. V.2 Flowchart will involve major changes to ensure program
# meets criteria, flexiblity, and efficiency of the assessment. 

'''
This maths program is designed for 4-6years olds that want to learn how to count the number of
triangles in a triangle puzzle.

The users name will be taken, then the user will be directed to the quiz. The user will be notified
if they corrrectly count the number of triangle in the puzzle or incorrectly count them. The user will
enter their value into a input box, which will be processed.

When all the puzzles are guessed by the user, the results table will show up.

'''

#imports the python gui module 
from tkinter import*

#Variables
strName = ""
answer = 0
count = 0

#Lists

intAnswersList = []


def strName():
    print("Hello", nameInput.get())

def quit():
    window.destroy()

def main():
    #global variables
    global window
    global canvas
    global name
    window = Tk()
    window.title("TRI_POLYGON")

    #Adds Quit Button to program
    Button(window,text="QUIT", width=5, command=quit, font="Calibri 20").pack()

    canvas = Canvas(window, width=960, height=600, bg="#FFFAD5")
    canvas.create_rectangle(960,90,0,0, fill="#385778")
    canvas.create_text(480,50, text='TRI_POLYGON MATHS PROGRAM', fill="#FFFFFF", font="Calibri 50")

    textCenter = 480,220
    canvas.create_rectangle(900,150,80,300, fill="#FFD34E") 
    canvas.create_text(textCenter, text="Welcome to the tri-polygon maths program. The goal is to correctly count the number of triangles in the desired puzzles.", fill="#385778", font="Calibri 12")
    canvas.pack()
    
    strName = Entry(window)
    strName.pack()
    nameInput = 480, 90
    nameInput = Button(window, text="Enter your Name", width=20, command=strName).pack()

    content = Entry.get()
    
    mainloop()
     
main()
