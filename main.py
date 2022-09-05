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
from PIL import Image, ImageTk

global myevent_list
global myshooter_list
global currentRowIndex

# Our lists.... Possible collapse into one list.
myevent_list    = []
myshooter_list  = []

### Build the SplashScreen

# Create object
splash_root = Tk()

# Adjust size
splash_root.geometry("1000x500")

# Set Title
splash_root.title("ImpactXS - Score Master")

# Read the Image
image = Image.open("images/1mile.png")
# Resize the image using resize() method
resize_image1 = image.resize((350, 350))
img1 = ImageTk.PhotoImage(resize_image1)
# create label and add resize image
label1 = Label(image=img1)
label1.image = img1
label1.place(x=0, y=0)

# Read the Image
image = Image.open("images/2mile.png")
# Resize the image using resize() method
resize_image2 = image.resize((350, 350))
img2 = ImageTk.PhotoImage(resize_image2)
# create label and add resize image
label2 = Label(image=img2)
label2.image = img2
label2.place(x=650, y=0)

# Read the Image
image = Image.open("images/impactxs.png")
# Resize the image using resize() method
resize_impactxs = image.resize((1000, 150))
impactxs = ImageTk.PhotoImage(resize_impactxs)
# create label and add resize image
labelimpactxs = Label(image=impactxs)
labelimpactxs.image = impactxs
labelimpactxs.place(x=0, y=350)

# Our Functions
def exitProgram():
    exit()

def main():
    # destroy splash window
    splash_root.destroy()

    # Execute tkinter
    root = Tk()

    # Adjust size
    root.geometry("400x400")

    # Set Title
    root.title("ImpactXS - Score Master")

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


# Set the Interval
splash_root.after(3000, main)

# Execute tkinter program
mainloop()