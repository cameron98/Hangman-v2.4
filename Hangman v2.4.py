"""
Hangman v2.3

New update streamlining of code using classes


Purpose to create a GUI hangman game for STEM day/school
Begin with window to type in word, hidden with *.
Must display list of letters, hangman screen and _ for letters.

Created by Cameron
cameron.finnie@yahoo.co.uk
"""
import tkinter as tk
import turtle
from sys import exit

#Class to create the alphabet buttons to guess with
class Buttons:
    
    #Takes input for location values of button and assigns them to variable
    def __init__(self, letter, column, row):
        self.letter = letter
        self.column = column
        self.row = row

    #Function to create and display each button using arguments given
    def create(self):
        self.tkbutton = tk.Button(window, text=self.letter, bg = colour, font=FONT,
                         command=lambda : check(self.letter))
        self.tkbutton.place(relx=self.column, rely=self.row)

#command for EXIT button, close tkinter window and end program
def EXIT():
    window.destroy()
    exit()

#function to check if guess is in word
def check(guess):
    global wordList, correct, attempt, missing
    occurences = word.count(guess) #Find number of occurences
    if occurences > 0:
        while occurences > 0: #loops replacement for number of occurences
            location = word.index(guess)
            word[location] = "!"
            wordList[location] = guess
            occurences -= 1
            correct += 1
        wordDisplay.config(text=wordList)
        if correct == total: #Changes text when complete
            wordList = ("Correct! The word was '" + final.upper() + "'")
            wordDisplay.config(text=wordList)
    else: #changes text when failed
        attempt += 1
        draw(attempt)
    guesses = []
    missing.append(guess)
    guesses.append(guess)
    guess = eval(guess)
    guess.tkbutton.place_forget()
    
    #attatch new function to this to trigger drawing

#steps to draw hangman on tkinter canvas    
def draw(step): 
    if step ==1:
        t.penup()
        t.goto(-300, -200)
        t.pendown()
        t.forward(600)
        t.penup()
        t.goto(-100,-200)
    elif step ==2:
        t.left(90)
        t.pendown()
        t.forward(400)
    elif step ==3:
        t.right(90)
        t.forward(250)
    elif step ==4:
        t.penup()
        t.goto(-100, 160)
        t.left(45)
        t.pendown()
        t.forward(56.56854249)
    elif step ==5:
        t.penup()
        t.goto(150,200)
        t.setheading(270)
        t.pendown()
        t.forward(40)
    elif step ==6:
        t.speed(0)
        t.seth(180)
        t.circle(17)
    elif step == 7:
        t.speed(5)
        t.penup()
        t.goto(150,125)
        t.pendown()
        t.seth(270)
        t.forward(80)
    elif step ==8:
        t.penup()
        t.goto(120, 100)
        t.seth(0)
        t.pendown()
        t.forward(60)
    elif step ==9:
        t.penup()
        t.goto(150,45)
        t.right(45)
        t.pendown()
        t.forward(45)
    elif step ==10:
        t.penup()
        t.goto(150, 45)
        t.right(90)
        t.pendown()
        t.forward(45)
        wordDisplay.config(text="OUT OF LIVES! The word was '" + final.upper() + "'")
        


#Function for start button, inputs word into game and begins 
def START():
    global word, wordDisplay, wordList, total, correct, attempt, final, missing
    t.reset()
    for letter in missing:
        eval(letter).create()
    missing = []
    word = INPUT.get()
    final = word
    final.upper()
    word = word.upper()
    word = list(word)
    wordList = []
    for n in range(len(word)):
        wordList.append("_")
    ', '.join(wordList)
    wordDisplay.config(text=wordList)
    total = len(word)
    correct = 0
    t.penup()
    t.goto(-300,-200)
    attempt = 0
    RESTART.config(text="RESTART")
    INPUT.delete(0, 'end')

colour = "#538bad"
FONT = ("Arial", 20)
row1 = 0.3
row2 = 0.4
row3 = 0.5
row4 = 0.6
row5 = 0.7
row6 = 0.8
column1 = 0.05
column2 = 0.1
column3 = 0.15
column4 = 0.2
column5 = 0.25
missing = []

#code to find monitor resolutions
res = tk.Tk()
Sheight = res.winfo_screenheight()
Swidth = res.winfo_screenwidth()
res.destroy()
res.mainloop()

#Create main window
window = tk.Tk()
#Adds window title
window.title("Hangman")
#Sets window to fullscreen
window.attributes('-fullscreen', 'True')
#To add a background colour 
window.configure(background=colour)

#Title widget creation and placement
title = tk.Label(window, text="HANGMAN", bg=colour, font=("Arial", 50))
title.place(relx=0.38, rely=0.05)

#Alphabet button creation and placement as part of Buttons class
A = Buttons('A', column1, row1)
A.create()
B = Buttons('B', column2, row1)
B.create()
C = Buttons('C', column3, row1)
C.create()
D = Buttons('D', column4, row1)
D.create()
E = Buttons('E', column5, row1)
E.create()
F = Buttons('F', column1, row2)
F.create()
G = Buttons('G', column2, row2)
G.create()
H = Buttons('H', column3, row2)
H.create()
I = Buttons('I', column4, row2)
I.create()
J = Buttons('J', column5, row2)
J.create()
K = Buttons('K', column1, row3)
K.create()
L = Buttons('L', column2, row3)
L.create()
M = Buttons('M', column3, row3)
M.create()
N = Buttons('N', column4, row3)
N.create()
O = Buttons('O', column5, row3)
O.create()
P = Buttons('P', column1, row4)
P.create()
Q = Buttons('Q', column2, row4)
Q.create()
R = Buttons('R', column3, row4)
R.create()
S = Buttons('S', column4, row4)
S.create()
T = Buttons('T', column5, row4)
T.create()
U = Buttons('U', column1, row5)
U.create()
V = Buttons('V', column2, row5)
V.create()
W = Buttons('W', column3, row5)
W.create()
X = Buttons('X', column4, row5)
X.create()
Y = Buttons('Y', column5, row5)
Y.create()
Z = Buttons('Z', column3, row6)
Z.create()


#Turtle canvas creation and placement
canvas = tk.Canvas(window, height=Sheight*0.6, width=Swidth*0.6)
canvas.place(relx=0.35, rely=row1)

#Turtle setup
t = turtle.RawTurtle(canvas)
screen = t.getscreen()
screen.bgcolor=("white")

#Word to guess display setup and placement
wordDisplay = tk.Label(window, text="", font=("Arial",30), bg=colour)
wordDisplay.place(relx=0.1, rely=0.2)

#EXIT button creation and placement
EXIT = tk.Button(window, text="EXIT", bg=colour, command=EXIT)
EXIT.place(relx=0.14, rely=0.95)

#Restart button setup and placement
RESTART = tk.Button(bg=colour, text="START", command=START)
RESTART.place(relx=0.75, rely=0.95)

INPUT = tk.Entry(window, show="*")
INPUT.place(relx=0.6, rely=0.955)

window.mainloop()
