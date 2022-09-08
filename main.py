########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
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
#                   :   JSONLint :          https://jsonlint.com
#
########################################################################################################################
__author__      = "George Leonard"
__email__       = "georgelza@gmail.com"
__version__     = "0.0.1"

from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime

import uuid
import settings

# Initialize Global Variables
settings.init()

import event
import shooters

global main_window

my_logger       = settings.my_logger
appname         = settings.appname
splashtime      = settings.splashtime
debuglevel      = settings.debuglevel

############## LETS Start ##############
my_logger.info('{time}, --------------------------------------------------'.format(
    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
))


### Build the SplashScreen

# Create object
splash_root = Tk()

# Adjust size
splash_root.geometry("1000x600")

# Set Title
splash_root.title(appname)

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
resize_impactxs = image.resize((1000, 125))
impactxs = ImageTk.PhotoImage(resize_impactxs)
# create label and add resize image
labelimpactxs = Label(image=impactxs)
labelimpactxs.image = impactxs
labelimpactxs.place(x=0, y=450)

# Finish Building Splash screen


# Our Functions
def exitProgram():

    my_logger.info('{time}, Exiting...'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))
    exit()

# end exitProgram

def newEvent():

    global main_window

    if debuglevel >= 1:
        my_logger.info('{time}, newEvent Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # Popup file open window, allowing user to select 1Mile or 2 Mile event.json template file
    settings.filename = event.select_file("New")
    if settings.filename:
        settings.my_event_list = event.load_event_data(settings.filename)
        settings.my_event_list["uuid"] = str(uuid.uuid4())
        event.open_event_screen(main_window, settings.my_event_list)

    if debuglevel >= 1:
        my_logger.info('{time}, newEvent Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end newEvent

def loadEvent():

    global main_window

    if debuglevel >= 1:
        my_logger.info('{time}, loadEvent Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    settings.filename = event.select_file("Load")
    if settings.filename:
        settings.my_event_list = event.load_event_data(settings.filename)
        event.open_event_screen(main_window)

    if debuglevel >= 1:
        my_logger.info('{time}, loadEvent Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end loadEvent

def load_all_shooters():

    global main_window

    if debuglevel >= 1:
        my_logger.info('{time}, load_all_shooters Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    shooters.load_shooters(main_window)

    if debuglevel >= 1:
        my_logger.info('{time}, load_all_shooters Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_shooters


def load_scores():

    global myevent_list

    if debuglevel >= 1:
        my_logger.info('{time}, load_scores Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    shooters.load_scores(main_window)

    if debuglevel >= 1:
        my_logger.info('{time}, load_scores Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_shooters

def main():

    global main_window

    if debuglevel >= 1:
        my_logger.info('{time}, Main Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # destroy splash window
    splash_root.destroy()

    # As we're destroying the above TK object we happy to create a new one, otherwise we'de use TopLevel()
    # Execute tkinter
    root = Tk()
    root.state("zoomed")

    # Adjust size
    root.geometry("600x400")

    # Set Title
    root.title(appname)
    root.iconbitmap("images/impactxs_ico.jpg")

    # Lets Build the Menu Structure
    menu = Menu(root)
    root.config(menu=menu)
    fileMenu = Menu(menu, tearoff=0)

    # Open file dialog, allowing user to select 1 Mile or 2 Mile Template
    fileMenu.add_command(label="New Event", command=newEvent)

    # Open file dialog allowing user to select event file
    fileMenu.add_command(label="Load Event", command=loadEvent)

    # Load all shooters as per the event file loaded into Treeview, if it is a new event with no shooters open
    # empty treeview, with only Add button enabled
    fileMenu.add_command(label="Shooters...", command=load_all_shooters)

    # #1 Load the shooters and scores into treeview
    # #2 if auto update is selected, disable edit mode, allow user to select Qualify or Final as the order, initiate
    # auto refresh, for now every 10 seconds, change to refresh when shooter score is updated,
    fileMenu.add_command(label="Scores...", command=load_scores)

    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exitProgram)
    menu.add_cascade(label="File", menu=fileMenu)

    helpMenu = Menu(menu, tearoff=0)
    helpMenu.add_command(label="Welcome")
    helpMenu.add_command(label="About...")
    menu.add_cascade(label="Help", menu=helpMenu)

    main_window = root
    fileMenu.bind("")

    if debuglevel >= 1:
        my_logger.info('{time}, Main Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end main


# Set the Splash screen Interval,after Interval call main()
splash_root.after(splashtime, main)

# Execute tkinter program
mainloop()