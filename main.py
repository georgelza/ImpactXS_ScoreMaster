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

from api.apputils import *
import logging
from tkinter import *
from PIL import Image, ImageTk
import Shooters
import Event
import uuid

global my_logger
global DEBUGLEVEL
global myevent_list
global myshooter_list
global currentRowIndex

# Our lists.... Possible collapse into one list.
myevent_list    = []
myshooter_list  = []


# Read/Define Environment variables
config_params   = getAppEnvVariables()
DEBUGLEVEL      = config_params["debuglevel"]
LOGLEVEL        = config_params["loglevel"]
SPLASH_TIME     = config_params["splash_time"]
App_Name        = "ImpactXS - ScoreMaster"


# Logging Handler
logging.root.handlers = []
FORMAT = '%(levelname)s :%(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT)

# create logger
my_logger = logging.getLogger(__name__)

# Set Logging level
if LOGLEVEL == 'INFO':
    my_logger.setLevel(logging.INFO)
    my_logger.info('{time}, INFO LEVEL Activated'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

elif LOGLEVEL == 'DEBUG':
    my_logger.setLevel(logging.DEBUG)
    my_logger.debug('{time}, DEBUG LEVEL Activated'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

elif LOGLEVEL == 'CRITICAL':
    my_logger.setLevel(logging.CRITICAL)
    my_logger.critical('{time}, CRITICAL LEVEL Activated'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

# end DEBUGLEVEL


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
splash_root.title(App_Name)

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
    my_logger.info('{time}, exitProgram Called '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))
    exit()

# end exitProgram


def main():
    global my_logger
    global main_window

    my_logger.info('{time}, Main Starting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    # destroy splash window
    splash_root.destroy()

    # Execute tkinter
    root = Tk()
    root.state("zoomed")

    # Adjust size
    root.geometry("1200x800")

    # Set Title
    root.title(App_Name)

    # Lets Build the Menu Structure
    menu = Menu(root)
    root.config(menu=menu)
    fileMenu = Menu(menu, tearoff=0)

    # Open file dialog, allowing user to select 1 Mile or 2 Mile Template
    fileMenu.add_command(label="New Event", command=newEvent)

    # Open file dialog allowing user to select event file
    fileMenu.add_command(label="Load Event", command=loadEvent)

    # Load shooters as per the event file loaded => Treeview, if new event with no shooters open empty treeview,
    # with only Add button enabled
    fileMenu.add_command(label="Shooters", command=loadShooters)

    # Load Shooters names and scores onto an auto updating screen, every time a user updates/saves a score refresh the
    # scores screen
    fileMenu.add_command(label="Scores")

    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exitProgram)
    menu.add_cascade(label="File", menu=fileMenu)

    helpMenu = Menu(menu, tearoff=0)
    helpMenu.add_command(label="Welcome")
    helpMenu.add_command(label="About...")
    menu.add_cascade(label="Help", menu=helpMenu)

    fileMenu.bind("")
    main_window = root

# end main


def newEvent():
    global my_logger
    global DEBUGLEVEL
    global myevent_list
    global main_window

    my_logger.info('{time}, newEvent Starting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    # Popup file open window, allowing user to select 1Mile or 2 Mile event.json template file

    # On events screen, once opened and first time <SAVE> or <SAVE AS>, filename/format <start_date>_<distance>_event.json

    myevent_list = Event.load_event_data("events/new_1m_event.json", my_logger, DEBUGLEVEL)
    myevent_list["uuid"] = str(uuid.uuid4())
    Event.open_event_screen(main_window, myevent_list, my_logger, DEBUGLEVEL)

# end newEvent


def loadEvent():
    global my_logger
    global DEBUGLEVEL
    global myevent_list
    global main_window

    my_logger.info('{time}, loadEvent Starting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    myevent_list = Event.load_event_data("events/20220901_1m_event.json", my_logger, DEBUGLEVEL)
    Event.open_event_screen(main_window, myevent_list, my_logger, DEBUGLEVEL)

# end loadEvent


def loadShooters():
    global my_logger
    global DEBUGLEVEL
    global myevent_list
    global myshooter_list
    global main_window

    my_logger.info('{time}, loadShooters Starting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    myshooter_list = Shooters.load_shooters_data(myevent_list, my_logger, DEBUGLEVEL)
    Shooters.open_shooter_screen(main_window, myshooter_list, my_logger, DEBUGLEVEL)

# end loadShooters

# Set the Splash screen Interval
splash_root.after(SPLASH_TIME, main)

# Execute tkinter program
mainloop()