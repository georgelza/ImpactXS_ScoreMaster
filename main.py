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
#                   :   With lots of help from Scott Johnson (softwareNugget65@gmail.com)
#                   :   & many YouTube videos ;)
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
import pymsgbox

# Initialize Global Variables
settings.init()

import event
import shooters
import scores_editor
import scores_display

global main_window

my_logger       = settings.my_logger
loglevel        = settings.loglevel
splashtime      = settings.splashtime
debuglevel      = settings.debuglevel
appname         = settings.appname
event_mode      = settings.event_mode

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

    my_logger.info('{time}, main.Exiting...'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))
    exit()

# end exitProgram

def newEvent():
    # Call loadEvent in the new mode
    settings.event_mode = "Load_Template"
    loadEvent("Load_Template")

# end newEvent

def currentEvent():
    # Call loadEvent in the load current known event mode mode
    settings.event_mode = "Load_Event"
    loadEvent("Load_Event")

# end CurrentEvent

def loadEvent(_mode):

    global main_window

    if debuglevel >= 1:
        my_logger.info('{time}, main.loadEvent.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    if _mode == "Load_Template":
        settings.filename = settings.file_dialog("Load_Template")
        settings.event_mode = "Initial_Event_Save"

    else:
        settings.filename = settings.file_dialog("Load_Event")
        settings.event_mode = ""

    if settings.filename:
        settings.load_event_json_from_file(settings.filename)

    if _mode == "New_Event":
        settings.my_event_list["uuid"]  = str(uuid.uuid4())

    event.open_event_screen(main_window)

    if debuglevel >= 1:
        my_logger.info('{time}, main.loadEvent.Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end loadEvent


def load_all_shooters():

    global main_window

    if debuglevel >= 1:
        my_logger.info('{time}, main.load_all_shooters.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    if settings.first_start_mode == False:
        shooters.load_all_shooters(main_window)

    else:
        # popup message
        pymsgbox.alert('Please load an Event first', 'Error')

        if debuglevel >= 1:
            my_logger.info('{time}, main.load_all_shooters.Bypassing, no event loaded yet!!!'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    if debuglevel >= 1:
        my_logger.info('{time}, main.load_all_shooters.Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_shooters


def shooter_score_editor():

    if debuglevel >= 1:
        my_logger.info('{time}, main.shooter_score_editor.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    if settings.first_start_mode == False:
        scores_editor.edit_all_shooters_scores(main_window)

    else:
        # popup message
        pymsgbox.alert('Please load an Event first', 'Error')

        if debuglevel >= 1:
            my_logger.info('{time}, main.shooter_score_editor.Bypassing, no event loaded yet!!!'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    if debuglevel >= 1:
        my_logger.info('{time}, main.shooter_score_editor.Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end shooter_score_editor


def shooter_score_displayer():

    if debuglevel >= 1:
        my_logger.info('{time}, main.shooter_score_displayer.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    if settings.first_start_mode == False:
        scores_display.display_all_shooters_scores(main_window)

    else:
        # popup message
        pymsgbox.alert('Please load an Event first', 'Error')

        if debuglevel >= 1:
            my_logger.info('{time}, main.shooter_score_displayer.Bypassing, no event loaded yet!!!'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    if debuglevel >= 1:
        my_logger.info('{time}, main.shooter_score_displayer.Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end shooter_score_displayer


def save_json_to_excelfile():

    # Get export file
    if debuglevel >= 1:
        my_logger.info('{time}, main.save_json_to_excelfile.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    filename = settings.file_dialog("Save_to_Excel")

    if debuglevel >= 1:
        my_logger.info('{time}, main.save_json_to_excelfile.filenamr {filename} '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            filename=filename
        ))

    settings.save_json_to_excelfile(filename)

    if debuglevel >= 1:
        my_logger.info('{time}, main.save_json_to_excelfile.Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

#end save_json_to_excelfile

def main():

    global main_window

    if debuglevel >= 1:
        my_logger.info('{time}, Main.Called '.format(
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
    fileMenu.add_command(label="Load Event", command=currentEvent)

    # Load all shooters as per the event file loaded into Treeview, if it is a new event with no shooters open
    # empty treeview, with only Add button enabled
    fileMenu.add_command(label="Shooters...", command=load_all_shooters)

    # Load the shooters and scores into treeview, when a record is clicked we allowed the operator to edit the
    # individual scores for the shooter selected
    fileMenu.add_command(label="Scores Editor", command=shooter_score_editor)

    # display all the scores, allow the operator to select the display order, ranked by qualifying or finals or total
    fileMenu.add_command(label="Scores Displayer", command=shooter_score_displayer)

    # display all the scores, allow the operator to select the display order, ranked by qualifying or finals or total
    fileMenu.add_command(label="Export to Excel", command=save_json_to_excelfile)

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
        my_logger.info('{time}, Main.Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end main


if __name__ == "__main__":

    # Set the Splash screen Interval,after Interval call main()
    splash_root.after(splashtime, main)

    # Execute tkinter program
    mainloop()