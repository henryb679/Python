#AS 3.46 ASSESSMENT- TRI_POLYGON

# AUTHOR: Henry Bai
# PROGRAM: AS 3.46 ASSESSMENT- TRI_POLYGON
# VERSION: 2.0

# PURPOSE OF PROGRAM
'''
This maths program is designed for 4-6years olds that want to learn how to count the number of
triangles in a triangle puzzle. This program is also suitable for all ages. 

The users name will be taken, then the user will be directed to the quiz. The user will be notified
if they corrrectly count the number of triangle in the puzzle or incorrectly count them. The user will
enter their value into a input box, which will be processed.

When all the puzzles are guessed by the user, the results table will show up.

'''

#imports the python gui module 
from tkinter import *

#The quit function allows the user to exit the maths program via the quit button created in the guiItem
def quit():
    window.destroy()

#the guiItem puts all the default items on the grid like quit button adn titleText which will be displayed throughout the program.
'''
This allows code not to be duplicated increasing the efficiency of the program. Also visual effects like fonts, padding etc are
added to the labels to improve the appearance of the program
'''
class guiItem:
    def __init__(self, parent):
        #sets the submit to false to allow looping of question
        self.submit = False

        #the default column sets all the relevant labels to the same column.
        self.defaultColumn = 10

        #the title text of the program is created
        self.titleText = Label(parent, text="TRI_POLYGON MATHS PROGRAM", bg="#385778", fg="#ffffff", font="Calibri 40", padx = 5, pady =10)
        self.titleText.grid(row=0, column=self.defaultColumn , sticky = NSEW, pady=0)
        
        #creates the sub-heading for the program
        self.subHeading = Label(parent, text="Welcome Page",bg="#FFD34E", font="Calibri 15", fg="#385778", padx = 10, pady =20)
        self.subHeading.grid(row=100, column=self.defaultColumn , rowspan=10, sticky = NSEW, pady=10)
        
        #creates the text box for the instructions which is also used for the puzzle quiz images and the result text
        self.box = Label(parent, text="Welcome to the tri-polygon maths program. \n The goal is to correctly count the number of triangles in the desired puzzles.",
          bg="#FFD34E", font="Calibri 15", fg="#385778", padx = 10, pady=100)
        self.box.grid(row=130, column=self.defaultColumn , rowspan=10, sticky = NSEW, pady=10)

        #creates the quit button on the grid
        self.quitButton = Button(parent,text="QUIT", width=5, command=quit, font="Calibri 20", bg="#BD4932", fg="#FFFFFF")
        self.quitButton.grid(row =0, column =0, sticky=N+W)

        #creates the guidence text to tell the user what to put in the entry box
        self.helpText = Label(parent, text="Please Enter your Name", font="Calibri 12", fg="#385778", padx = 10, pady =10)
        self.helpText.grid(row=150, column= 10, sticky = W)

        #creates the continue button, with the command adapting dependent on the stage of the program
        self.continueButton = Button(parent,text="CONTINUE", width=10, height= 2, command=self.inputFunction, font="Calibri 12", bg="#5ABD2F", fg="#FFFFFF")
        self.continueButton.grid(row=960, column= 620)

        #creates the entry box for the strName   
        self.inputName = Entry(window, font="Calibri 20", highlightbackground= "#385778", highlightthickness= 2)
        self.inputName.grid(row=150, column=10, sticky = E, ipadx= 40, ipady = 2, pady=20)

        #ensures the items for the GUI are placed on the grid
        self.titleText.grid()
        self.box.grid()
        self.subHeading.grid()
        self.quitButton.grid()
        self.helpText.grid()
        self.continueButton.grid()
        self.inputName.grid()

    #this will allow the program to sucessfully process the user's inputs later for processing
    '''
    The inputFunction acts as a way to process the users inputs answer for question and the users
    name. This will ensure the user's inputs are stored correctly. 
    '''
    #this will allow the program to sucessfully process the user's inputs later for processing
    def inputFunction(self):
        if self.submit == False:
            self.strName = self.inputName.get()
            #clears the entry box
            print(self.strName)
            self.inputName.delete(0, END)
            self.inputName.grid_forget()
            #sets counters to zero
            self.intCount = 0
            self.intCorrectCounter = 0 
            self.question()

            '''
            if conditions are true, the questions are generated according the the length and the values in the intAnswerList plus the
            puzzle images.

            Also the question labels and functions are all set to allow for new puzzles to be added with minnal work for the user
            '''
        elif self.submit == True:
            if self.intCount < len(intAnswerList):
                self.helpText.config(text="Your Answer")
                self.subHeading.config(text="Question {} of {}:   How many triangles are in this picture?".format(self.intCount+1, (len(intAnswerList)))) 
                self.answer = Entry(window, font="Calibri 20", highlightbackground= "#385778", highlightthickness= 2, width=1)
                self.answer.grid(row=150, column=10, sticky = E ,ipadx= 10, ipady = 2, pady=10)
                self.box.config(image = listImage[self.intCount],bg="#2D7FBD")
                answer = self.answer.get()

            #If the counter == the length of the intAnswerList, the question part of the program will terminate which will allow the resultClass to be called.

            elif self.intCount ==  len(intAnswerList):
                results = self.resultClass(window, self.strName, self.intCorrectCounter, self.subHeading, self.defaultColumn)
                self.helpText.grid_remove()
                self.continueButton.grid_remove()
    '''
    The resultClass displays how many answers the user got correct out of the length of the intAnswerList, the users name and the answers to the puzzle.

    The relevant items are called through the class parmeters through self which reduces code duplication allowing for quick and easy changes to the
    appearance of the program through classes of the labels in the program.

    Due to time constants, the users answers have not been included to allow the user to see their results and compare against the answers. This will be
    added to future programs to improve the appearance of the result page. 

    '''
    class resultClass:
        def __init__(self, window, strName, intCorrectCounter, subHeading, defaultColumn):
            #the size of the grid changes to fit the answers label
            window.geometry('960x780+0+10')

            #variables are passed through the class
            self.strName = strName
            self.intCorrectCounter = intCorrectCounter
            self.subHeading = subHeading
            self.defaultColumn = defaultColumn

            #the labels are set up to ensure the results are displayed properly
            self.subHeading.config(text="Result Page")               
            self.resultBox1 = Label(window, text="Well done {}. \n Thanks for playing TRI_POLYGON maths program. \n You got {} out of {}. \n Answers Below".format(self.strName, self.intCorrectCounter, len(intAnswerList)), bg="#2D7FBD",
                                         font="Calibri 15", fg="#FFFFFF", padx = 2, pady= 2)
            self.resultBox1.grid(row=130, column=self.defaultColumn, rowspan=10, sticky = NSEW)

            #sets the counter to zero
            intAnswerCount = 0
            #the row is initally set to zero
            r = 0
            #this while loop helps the answers to be pulled out of a list in seperate labels.
            while intAnswerCount < len(intAnswerList):

                self.questionNo = Label(window, text="Question No.{}".format(intAnswerCount+1),font="Calibri 12 bold", padx = 2, pady =2,fg="#FFFFFF", bg="#2D7FBD")
                self.questionNo.grid(row= 140+r, column = self.defaultColumn, sticky = NSEW, pady=1)

                self.questionAnswer = Label(window, text="{}".format(intAnswerList[intAnswerCount]),font="Calibri 12", fg="#000000", padx = 2, pady =2, bg="#ffffff")
                self.questionAnswer.grid(row= 142+ r, column = self.defaultColumn, sticky = NSEW, pady=1)

                intAnswerCount += 1

                r += 4    
            #When finished the loop ends and all the answers are shown to the user.

    #Question Function
    '''
    The question function ensures the continueButton is configured correctly to the answer function
    which processes the users answer to give the user feedback to determine if they got the question
    correct or not.
    '''
    def question(self):
        print(self.intCount)
        self.submit = True
        self.continueButton.config(command=self.answer)
        self.inputFunction()

    #answer function
    def answer(self):
        #ensures the entry's are set to a interger data type
        answer = self.answer.get()
        answer = int(answer)
        print(answer)
        self.intCount = int(self.intCount)
        #The user feedback label is set up    
        userFeedback = Label(window, font="Calibri 12", fg="#385778", padx = 15, pady =10)
        userFeedback.grid(row=960, column= 10, sticky = W)
        '''
        The user is notfied if their answer is correct or not through a label text message. If they get
        the question correct, the intCorrectCounter add 1 to the count which is used for the resultClass
        to inform the user how many questions they got correct.
        '''
    
        if answer == intAnswerList[self.intCount]:
            userFeedback.config(text="Correct")
            userFeedback.grid()
            self.intCorrectCounter += 1
            print(self.intCorrectCounter )
            print("Correct")
            print(answer)
        else:
            userFeedback.config(text="Incorrect")
            userFeedback.grid()
            print("Incorrect")
            print(answer)

        #increases the count by one to ensure the correct number of questions are displayed to the user.
        self.intCount = self.intCount + 1
        self.inputFunction()

#main program
'''
the main function sets up the grid of the window which will allow all the relevant widgets to appear.
Then the guitItem class will show 
'''
def main():
    
    #sets relevant variables to global vaiables
    global window, listImage, intAnswerList
    
    #calls the window to tkinter  
    window = Tk()
    #sets the grid size, title, background colour of window
    window.geometry('960x600+0+10')
    window.configure(background='#FFFAD5')
    window.title("TRI_POLYGON")

    #the answers of puzzle pictures 
    intAnswerList = [7, 5, 40, 15, 27]
    '''
    Program flexbility, when a new value and listImage is added or modified, the program
    will be able to adapt by determining the number of questions to ask to the user.
    The result page will also adapt.
    '''
    
    #calls the class
    itemPlacement = guiItem(window)

    #Image list
    '''
    The image list stores all the puzzle pictures to a list which will be called up through the
    intCount, which will show the correct puzzle for each question. 
    '''
    listImage = []
    listImage.append(PhotoImage(file = "images\q-1.gif"))
    listImage.append(PhotoImage(file = "images\q-2.gif"))
    listImage.append(PhotoImage(file = "images\q-3.gif"))
    listImage.append(PhotoImage(file = "images\q-4.gif"))
    listImage.append(PhotoImage(file = "images\q-5.gif"))
     
    window.mainloop()

#calls the main function
main()

