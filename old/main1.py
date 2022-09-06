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
########################################################################################################################
__author__      = "George Leonard"
__email__       = "georgelza@gmail.com"
__version__     = "0.0.1"

import tkinter
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

global myevent_list
global myshooter_list
global currentRowIndex
splash_time = 5000
App_Name = "ImpactXS - ScoreMaster"

# Our lists.... Possible collapse into one list.
myevent_list    = []
myshooter_list  = []


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

# Our Functions
def exitProgram():
    exit()

def show_frame(frame):
    frame.tkraise()

def main():
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

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(root)

    for frame in (frame1, frame2, frame3):
        frame.grid(row=0, column=0, sticky="nsew")

    # ======================== Frame 1 ========================
    frame1_title = tk.Label(frame1, text="Page 1", bg="red")
    frame1_title.pack(fill="both", expand=True)

    frame1_btn = tk.Button(frame1, text="Enter", command=lambda:show_frame(frame2))
    frame1_btn.pack(fill="x", ipady=15)

    # ======================== Frame 2 ========================
    frame2_title = tk.Label(frame2, text="Page 2", bg="blue")
    frame2_title.pack(fill="both", expand=True)

    frame2_btn = tk.Button(frame2, text="Enter", command=lambda:show_frame(frame3))
    frame2_btn.pack(fill="x", ipady=15)

    # ======================== Frame 3 ========================
    frame3_title = tk.Label(frame3, text="Page 3", bg="green")
    frame3_title.pack(fill="both", expand=True)

    frame3_btn = tk.Button(frame3, text="Enter", command=lambda:show_frame(frame1))
    frame3_btn.pack(fill="x", ipady=15)

    show_frame(frame1)

# Set the Interval
splash_root.after(splash_time, main)

# Execute tkinter program
mainloop()