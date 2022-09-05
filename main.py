########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#   For             :   For Bredan Fike
#   eMail           :
#
#
#   File            :   main.py
#
#	By              :   George Leonard ( georgelza@gmail.com )
#
#   Created     	:   0.0.1 - 5 September 2022
#
#   Changelog       :   0.0.1 - 8 Jul 2022
#
#
#   Notes       	:
#                   :   Menu bar :          https://www.pythontutorial.net/tkinter/tkinter-menu/
#                   :   Scott's Examples :  https://www.youtube.com/watch?v=cuIjKMPRn0k
########################################################################################################################
__author__      = "George Leonard"
__email__       = "georgelza@gmail.com"
__version__     = "0.0.1"

import tkinter
from tkinter import *
from tkinter import ttk
import uuid
import json
import datetime
from PIL import Image, ImageTk

global myevent_list
global myshooter_list
global currentRowIndex

# Our lists.... Possible collapse into one list.
myevent_list    = []
myshooter_list  = []

root = Tk()
root.title('ImpactXS - ScoreMaster')

# Our Functions
def exitProgram():
    exit()




# Lets Build the Menu Structure
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu, tearoff=0)
fileMenu.add_command(label="New Event")
fileMenu.add_command(label="Load Event")
fileMenu.add_command(label="Shooters")
fileMenu.add_command(label="Scores")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitProgram)
menu.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menu, tearoff=0)
helpMenu.add_command(label="Welcome")
helpMenu.add_command(label="About...")
menu.add_cascade(label="Help", menu=helpMenu)

canvas = tkinter.Canvas(root, width=300, height=200)
canvas.grid(columnspan=5)


# Lets add some Logos onto our splash screen
logo1m      = Image.open('images/1mile.png')
logo1m      = ImageTk.PhotoImage(logo1m)
logo_label  = tkinter.Label(image = logo1m)
logo_label.image = logo1m
logo_label.grid(column=0, row = 0)

logo2m      = Image.open('images/2mile.png')
logo2m      = ImageTk.PhotoImage(logo2m)
logo_label  = tkinter.Label(image = logo2m)
logo_label.image = logo2m
logo_label.grid(column=1, row = 0)

logoimpact  = Image.open('images/impactxs.png')
logoimpact  = ImageTk.PhotoImage(logoimpact)
logo_label  = tkinter.Label(image = logoimpact)
logo_label.image = logoimpact
logo_label.grid(columnspan=3, column=0, row = 1)


root.mainloop()