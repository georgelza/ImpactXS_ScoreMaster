########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
#
#   File            :   scores.py
#
#	By              :   George Leonard ( georgelza@gmail.com )
#
#   Created     	:   0.0.1 - 6 September 2022
#
#   Changelog       :   0.0.1 -
#
#   Notes       	:
########################################################################################################################
__author__ = "George Leonard"
__email__ = "georgelza@gmail.com"
__version__ = "0.0.1"

from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk

import uuid
import json
import os

import settings

my_logger       = settings.my_logger
debuglevel      = settings.debuglevel


# Refresh data in memory from file (include updating global settings variable),
# shooters include their personal data,
# equipment and scores
def load_shooter_scores_json_from_file(myfile):

    if debuglevel >= 1:
        my_logger.info('{time}, scores.load_shooter_scores_json_from_file Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    with open(myfile, "r") as file_handler:
        settings.my_event_list = json.load(file_handler)
        settings.my_shooter_list = settings.my_event_list["shooters"]

    file_handler.close

    settings.pp_json(settings.my_shooter_list)

    if debuglevel >= 1:
        my_logger.info('{time}, scores.load_shooter_scores_json_from_file.file has been read and closed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_shooter_scores_json_from_file



# We will add the scores via the File/scores menu.
# For now ust build Scott's Treeview and user editor, then replace with my data.
def load_all_shooters_scores(main_window):

    global trv
    global label_text_bg
    global label_text_fg
    global entry_text_bg
    global entry_text_fg
    global txtfont
    global txtfont_size
    global lblfont
    global lblfont_size
    global lblframefont
    global lblframefont_size

    frame_bg            = settings.frame_bg
    label_text_bg       = settings.label_text_bg
    label_text_fg       = settings.label_text_fg
    entry_text_bg       = settings.entry_text_bg
    entry_text_fg       = settings.entry_text_fg
    txtfont             = settings.txtfont
    txtfont_size        = settings.txtfont_size
    lblfont             = settings.lblfont
    lblfont_size        = settings.lblfont_size
    lblframefont        = settings.lblframefont
    lblframefont_size   = settings.lblframefont_size

    if debuglevel >= 1:
        my_logger.info('{time}, scores.load_all_shooters_scores Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    child = Toplevel(main_window)
    child.title = "Scores"
    child.geometry("1000x800")
    child.configure(bg=frame_bg)

    header_frame    = Frame(child)
    tree_frame      = Frame(child)
    footer_frame    = Frame(child)

    header_frame.pack(fill="both",  expand="yes", padx=10, pady=10)
    tree_frame.pack(fill="both",    expand="yes", padx=10, pady=10)
    footer_frame.pack(fill="both",  expand="yes", padx=10, pady=10)

    # Determine where we're running, as template and events are by default subdirectories of the App directory.
    directory = os.getcwd()

    if debuglevel >= 1:
        my_logger.info('{time}, scores.load_all_shooters_scores.Current App Directory {directory}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            directory=directory
        ))

    image_file = "images/" + settings.my_event_image
    # Read the Image
    image               = Image.open(image_file)
    # Resize the image using resize() method
    resize_image_event  = image.resize((150, 150))
    img1                = ImageTk.PhotoImage(resize_image_event)
    # create label and add resize image
    label1              = Label(header_frame, image=img1)
    label1.image        = img1
    label1.pack(side=tk.LEFT)

    trv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6), show="headings", height="20")
    trv.grid(row=0, column=0, rowspan=20, columnspan=6, sticky=E+W)

    trv.heading(1, text="Place",        anchor="w")
    trv.heading(2, text="Shooter",      anchor="center")
    trv.heading(3, text="Spotter",      anchor="center")
    trv.heading(4, text="Caliber",      anchor="center")
    trv.heading(5, text="Qualifying",   anchor="center")
    trv.heading(6, text="Finals",       anchor="center")

    trv.column("#1", anchor="w", width=50, stretch=True)
    trv.column("#2", anchor="w", width=250, stretch=True)
    trv.column("#3", anchor="w", width=250, stretch=True)
    trv.column("#4", anchor="w", width=200, stretch=False)
    trv.column("#5", anchor="w", width=113, stretch=False)
    trv.column("#6", anchor="w", width=113, stretch=False)

    # Read the Image
    image = Image.open("images/impactxs.png")
    # Resize the image using resize() method
    resize_impactxs = image.resize((930, 150))
    img2 = ImageTk.PhotoImage(resize_impactxs)
    # create label and add resize image
    label2 = Label(footer_frame, image=img2)
    label2.image = img2
    label2.grid(row=0, column=0, padx=5, pady=5)

    def load_trv_with_json():

        for item in trv.get_children():
            trv.delete(item)

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters_scores.load_trv_with_json Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        rowIndex = 1

        for key in settings.my_shooter_list:

            equipment           = key["equipment"]                          # Structure with equipment
            rifle               = equipment['rifle']                        # sub structure with rifle information
            scores              = key["scores"]                             # structure with scores

            trv.insert('', index='end', iid=rowIndex, text="",
                       values=(rowIndex,
                               key["first_name"].strip() + " " + key["last_name"].strip(),
                               key["spotter"],
                               rifle["caliber"],
                               scores['qualifying_score'],
                               scores['final_score']))

            rowIndex = rowIndex + 1

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters_scores.load_trv_with_json Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end load_trv_with_json

    load_trv_with_json()

    if debuglevel >= 2:
        my_logger.info('{time}, scores.load_all_shooters_scores Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_shooters_scores
