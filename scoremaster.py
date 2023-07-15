########################################################################################################################
#
#
#  	Project     	: 	ScoreMaster
#
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
from pathlib import Path

import uuid

import settings
import pymsgbox

# Initialize Global Variables
settings.init()

from os.path import join
import sys

import events

import event
import shooters
import scores_editor
import scores_display

global main_window

my_logger       = settings.my_logger
loglevel        = settings.loglevel
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
#splash_root.geometry("1000x600")
splash_root.geometry(settings.root_width_txt_xy)

# Set Title
splash_root.title(appname)

# Disable Resize
splash_root.resizable(False, False)

# Read the Image
try:
    image = settings.splash_1mile
    imagespath =  Path(settings.app_path).joinpath('images')
    image = Image.open(join(imagespath, image))
except:
    my_logger.error('FILE NOT FOUND: '+ image)
    sys.exit(1)

# Resize the image using resize() method
resize_image1   = image.resize((350, 350))
img1            = ImageTk.PhotoImage(resize_image1)
# create label and add resize image
label1          = Label(image=img1)
label1.image    = img1
label1.place(x=0, y=0)

# Read the Image
try:
    image = settings.splash_2mile
    imagespath =  Path(settings.app_path).joinpath('images')
    image = Image.open(join(imagespath, image))
except:
    my_logger.error('FILE NOT FOUND: '+ image)
    sys.exit(1)

# Resize the image using resize() method
resize_image2   = image.resize((350, 350))
img2            = ImageTk.PhotoImage(resize_image2)
# create label and add resize image
label2          = Label(image=img2)
label2.image    = img2
label2.place(x=650, y=0)

# Read the Image
try:
    imagespath =  Path(settings.app_path).joinpath('images')
    image = Image.open(join(imagespath, settings.splash_footer))
except:
    my_logger.error('FILE NOT FOUND: '+ settings.splash_footer)
    sys.exit(1)

#image               = Image.open(join(dirname(__file__), "images/" + settings.splash_footer))
# Resize the image using resize() method
resize_splash_footer     = image.resize((settings.splash_footer_x, settings.splash_footer_y))
splash_footer            = ImageTk.PhotoImage(resize_splash_footer)
# create label and add resize image
labelsplash_footer       = Label(image=splash_footer)
labelsplash_footer.image = splash_footer
x_offset = settings.splash_footer_x/2
x_pos = (1000/2) - x_offset
labelsplash_footer.place(x=x_pos, y=450)


# Little bit of event notification/calling, when ever we click save of the score editor screen we want to execute the
# events registered, might need to move this to the function calls below, in addition to a deregister function, so that we don't call the function/screen/trv refresh wheb

events.register_events("edit_all_shooters_scores", scores_display.paintScoreTrv)
events.register_events("edit_all_shooters_scores", scores_editor.paintScoreTrv)

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

    if settings.filename:
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


    if settings.first_start_mode == False:
        filename = settings.file_dialog("Save_to_Excel")

        if filename != "":
            settings.save_json_to_excelfile(filename)

        else:
            pymsgbox.alert('Please provide output file name', 'Error')

        #end if
    else:
        # popup message
        pymsgbox.alert('Please load an Event first', 'Error')

        if debuglevel >= 1:
            my_logger.info('{time}, main.shooter_score_displayer.Bypassing, no event loaded yet!!!'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

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
    root.geometry(settings.splash_width_txt_xy)

    # Disable Resize
    root.resizable(False, False)

    # Read the Image - main splash
    try:
        imagespath =  Path(settings.app_path).joinpath('images')
        splash_img = join(imagespath, settings.splash_img)
        image = Image.open(splash_img)
    except:
        my_logger.error('FILE NOT FOUND: '+ settings.splash_img)
        sys.exit(1)

    # Resize the image using resize() method
    resize_splash_img = image.resize((settings.splash_img_x, settings.splash_img_y))
    splash_img = ImageTk.PhotoImage(resize_splash_img)
    # create label and add resize image
    labelsplash_img = Label(image=splash_img)
    labelsplash_img.image = splash_img

    x_offset = settings.splash_img_x/2
    x_pos = (settings.splash_width_x/2) - x_offset
    y_offset = settings.splash_img_y/2
    y_pos = (settings.splash_width_y/2) - y_offset

    labelsplash_img.place(x=x_pos, y=y_pos)


    # Set Title
    try:
        imagespath =  Path(settings.app_path).joinpath('images')
        icon_img = join(imagespath, settings.icon_img)
        image = Image.open(icon_img)
    except:
        my_logger.error('FILE NOT FOUND: '+ settings.icon_img)
        sys.exit(1)

    root.title(appname)
    root.iconbitmap(image)

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
    splash_root.after(settings.splashtime, main)

    # Execute tkinter program
    mainloop()