#AS 3.46 ASSESSMENT- TRI_POLYGON

# AUTHOR: Henry Bai
# PROGRAM: AS 3.46 ASSESSMENT- TRI_POLYGON
# VERSION: 5.0

# CHANGES TO VERSION 5

'''
- Redesign of result page to prevent a change in the window size.
- ensured items such as continue button and other labels from appearing
on the result screeen.
- extra resultBox added to improve the appearance of the result screen. 

This will ensure invalid inputs are not accepted to the program.
'''

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
class guiItemClass:
    def __init__(self, parent):
        #sets the submit to false to allow looping of question
        self.submit = False

  
        #the default column sets all the relevant labels to the same column.
        self.defaultColumn = 10

        #the title text of the program is created
        self.titleText = Label(parent, text="TRI_POLYGON MATHS PROGRAM", bg="#385778", fg="#ffffff", font="Calibri 40 bold", padx = 5, pady =10)
        self.titleText.grid(row=0, column=self.defaultColumn , sticky = NSEW, pady=0)
        
        #creates the sub-heading for the program
        self.subHeading = Label(parent, text="Welcome Page",bg="#FFD34E", font="Calibri 15 italic", fg="#385778", padx = 10, pady =20)
        self.subHeading.grid(row=100, column=self.defaultColumn , rowspan=10, sticky = NSEW, pady=0)
        
        #creates the text box for the instructions which is also used for the puzzle quiz images and the result text
        self.box = Label(parent, text="Welcome to the tri-polygon maths program. \n The goal is to correctly count the number of triangles in the desired puzzles.",
          bg="#FFD34E", font="Calibri 15", fg="#385778", padx = 10, pady=100)
        self.box.grid(row=130, column=self.defaultColumn , rowspan=10, sticky = NSEW, pady=10)

        #creates the quit button on the grid
        self.quitButton = Button(parent,text="QUIT", width=5, command=quit, font="Calibri 20", bg="#BD4932", fg="#FFFFFF")
        self.quitButton.grid(row =0, column =0, sticky=N+W)

        #creates the guidence text to tell the user what to put in the entry box
        self.helpText = Label(parent, text="Please Enter your Name", font="Calibri 12", fg="#385778", padx = 10, pady =10)
        self.helpText.grid(row=150, column= self.defaultColumn, sticky = W)

        #creates the continue button, with the command adapting dependent on the stage of the program
        self.continueButton = Button(parent,text="CONTINUE", width=10, height= 2, command=self.inputFunction, font="Calibri 12", bg="#5ABD2F", fg="#FFFFFF")
        self.continueButton.grid(row=960, column= 11)

        #creates the entry box for the strName   
        self.inputName = Entry(window, font="Calibri 20", highlightbackground= "#385778", highlightthickness= 2, width=13)
        self.inputName.grid(row=150, column=self.defaultColumn, sticky = E, ipadx= 10, ipady = 2, pady=10)

        #error message to inform the user (strName)
        self.userErrorMessageStrName = Label(parent, font="Calibri 12", fg="#385778", padx = 20, pady =15)
        self.userErrorMessageStrName.grid(row=960, column= self.defaultColumn, sticky = E)

        #error message to inform the user question (answer)
        self.userErrorMessageAnswer = Label(parent, font="Calibri 12 italic", fg="#385778", bg="#FFFAD5", padx= 20, pady = 15)
        self.userErrorMessageAnswer.grid(row=960, column=self.defaultColumn, sticky = E)
        
        #correct/ incorrect message for user
        self.userFeedback = Label(parent, font="Calibri 12", fg="#385778", padx = 15, pady =10)
        self.userFeedback.grid(row=920, column= self.defaultColumn, sticky = W)
        
        #ensures the items for the GUI are placed on the grid
        self.titleText.grid()
        self.box.grid()
        self.subHeading.grid()
        self.quitButton.grid()
        self.helpText.grid()
        self.continueButton.grid()
        self.inputName.grid()
        self.userErrorMessageStrName.grid()
        self.userErrorMessageAnswer.grid()
        self.userFeedback.grid()

    #this will allow the program to sucessfully process the user's inputs later for processing
    '''
    The inputFunction acts as a way to process the users inputs answer for question and the users
    name. This will ensure the user's inputs are stored correctly. 
    '''
    #this will allow the program to sucessfully process the user's inputs later for processing
    def inputFunction(self):
        if self.submit == False:
            #stores inputName to strName for processing
            self.strName = self.inputName.get()

            #sets boundary cases which allows for easy modification of strName boundaries 
            minLenStrName = 3
            maxLenStrName = 16
            #the boundary range for the strName has been established to prevent the user from entering a obsure name
            '''
            A range of a min of 3 characters and a max of 16 characters have been set as the typical short name
            like amy has 3 characters and 16 characters for those odd few around that have long names.
            '''

            # error catching

            #checks if the user's answer contained digits etc.
            '''
            If is the case, the user is notified. A nested conditional loop
            has been included to ensure the user's input meets all the
            boundary and invalid cases to ensure the program doesn't
            break. Without error catching, the user's experience of
            the maths program will be impacted.
            '''
            if (any(char.isdigit() for char in self.strName)):
                self.userErrorMessageStrName.config(text="Invalid name input. Numbers in names are declined      ")
                self.inputName.delete(0, END)
            else:
                if len(self.strName) >= minLenStrName and len(self.strName) <= maxLenStrName:
                    self.inputName.grid_forget()
                    #sets counters to zero
                    self.intCount = 0
                    self.intCorrectCounter = 0 
                    self.question()
                else:
                    self.submit == False
                    self.userErrorMessageStrName.config(text="A name can't be longer than {} char or less than {} characters long      ".format(maxLenStrName, minLenStrName))             
                    self.inputName.delete(0, END)
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
                self.answer.grid(row=150, column=self.defaultColumn, sticky = E ,ipadx= 10, ipady = 2, pady=10)
                self.box.config(image = listImage[self.intCount], bg="#2D7FBD")
                
            #If the counter == the length of the intAnswerList, the question part of the program will terminate which will allow the resultClass to be called.
            #Also certain messages, items, labels ect are cleared from the window.
            elif self.intCount ==  len(intAnswerList):
                results = self.resultClass(window, self.strName, self.intCorrectCounter, self.subHeading, self.defaultColumn)
                self.helpText.grid_remove()
                self.box.grid_remove()
                self.userFeedback.grid_remove()
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

            #variables are passed through the class
            self.strName = strName
            self.intCorrectCounter = intCorrectCounter
            self.subHeading = subHeading
            self.defaultColumn = defaultColumn

            #the labels are set up to ensure the results are displayed properly
            self.subHeading.config(text="Result Page")               
            self.resultBox1 = Label(window, text="Well done {}. \n Thanks for playing \n TRI_POLYGON maths program. \n You got {} out of {}. ".format(self.strName, self.intCorrectCounter, len(intAnswerList)), bg="#2D7FBD",
                                         font="Calibri 15", fg="#FFFFFF", padx = 100, pady= 10)
            self.resultBox1.grid(row=130, column=self.defaultColumn, rowspan=120, sticky = N+ S + W)

            self.resultBox2 = Label(window, text="Answers to Questions", bg="#385778",
                                         font="Calibri 15", fg="#FFFFFF", padx = 49, pady= 20)
            self.resultBox2.grid(row=130, column=self.defaultColumn, rowspan=30, sticky = N + E)
            
            #sets the counter to zero
            intAnswerCount = 0
            #the row is initally set to zero
            r = 0
            #this while loop helps the answers to be pulled out of a list in seperate labels.
            while intAnswerCount < len(intAnswerList):
                self.questionNo = Label(window, text="Question No.{}".format(intAnswerCount+1),font="Calibri 12 bold", padx = 92, pady =5,fg="#FFFFFF", bg="#2D7FBD")
                self.questionNo.grid(row= 170+r, column = self.defaultColumn, sticky = N+ E, pady=1)
                
                self.questionAnswer = Label(window, text="{}".format(intAnswerList[intAnswerCount]),font="Calibri 12", fg="#000000", padx = 127, pady =5, bg="#ffffff")
                self.questionAnswer.grid(row= 172+ r, column = self.defaultColumn, sticky =N+ E, pady=1)
                intAnswerCount += 1
                #increases the row count to 4 allowing for answers to appear on seperate rows.
                r += 4    
            #When finished the loop ends and all the answers are shown to the user.
    #Question Function
    '''
    The question function ensures the continueButton is configured correctly to the answer function
    which processes the users answer to give the user feedback to determine if they got the question
    correct or not.
    '''
    def question(self):
        self.userErrorMessageStrName.grid_forget()
        self.submit = True
        self.continueButton.config(command=self.answer)
        self.inputFunction()

    #answer function
    def answer(self):
        #sets the max number value for the answer
        '''
        This is currently 100.
        This can be changes at any time to make to make the maths
        program easier or harder for the user. 
        '''
        intAnswerMax = 100  
        #error catching for answer
        try:
            #ensures the answer entry and intCount is set to a interger data type
            answer = self.answer.get()
            answer = int(answer)
            self.intCount = int(self.intCount)
            
            #The user feedback label is set up    
            '''
            The user is notfied if their answer is correct or not through a label text message. If they get
            the question correct, the intCorrectCounter add 1 to the count which is used for the resultClass
            to inform the user how many questions they got correct.
            '''
            
            #boundary range to ensure the user doesn't enter a silly number
            '''
            As the puzzle answers values are less than 100 and greater than 0, theses are the boundary ranges set
            This ensures the a appropriate number value is entered from the user and gives the user a hint.
            If the boundary range is too high, the range can be easily changed through the intAnswerMax variable
            '''
            if answer >0 and answer < intAnswerMax:
                if answer == intAnswerList[self.intCount]:
                    self.userFeedback.config(text="Q.{} answer is Correct".format(self.intCount+1))
                    self.intCorrectCounter += 1
                else:
                    self.userFeedback.config(text="Q.{} answer is Incorrect".format(self.intCount+1))
  
                #increases the count by one to ensure the correct number of questions are displayed to the user.
                self.intCount = self.intCount + 1
                self.inputFunction()
            else:
                self.userErrorMessageAnswer.config(text="A answer value can't be greater than {} or less than 0   ".format(intAnswerMax))           
                self.answer.delete(0, END)
            '''
            if the user enters a invalid input like "hwekj12", the user will be notifed and the entry will be cleared allowing the user to
            answer the question again.
            '''
        except ValueError:
            self.userErrorMessageAnswer.config(text="Invalid answer input. Whole numbers are only accepted   ".format(intAnswerMax))
            self.answer.delete(0, END)
          
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
    itemPlacement = guiItemClass(window)

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
