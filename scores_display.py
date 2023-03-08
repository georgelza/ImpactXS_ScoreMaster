########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
#
#   File            :   scores_display.py
#
#	By              :   George Leonard ( georgelza@gmail.com )
#
#   Created     	:   0.0.1 - 2 Mar 2023
#
#   Changelog       :   0.0.1 -
#
#   Notes       	:
########################################################################################################################
__author__  = "George Leonard"
__email__   = "georgelza@gmail.com"
__version__ = "0.0.1"

from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
from os.path import join, dirname

import settings

my_logger       = settings.my_logger
debuglevel      = settings.debuglevel
echojson        = settings.echojson


def display_all_shooters_scores(main_window):

    global score_viewer
    global trv_dsp_shooter_scores
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

    score_viewer        = settings.score_viewer
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
        my_logger.info('{time}, scores_display.display_all_shooters_scores.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    child = Toplevel(main_window)
    child.title = "Scores Displayer"
    child.geometry("1130x800")
    child.configure(bg=frame_bg)

    # Disable Resize
    child.resizable(False, False)

    header_frame    = Frame(child)
    tree_frame      = Frame(child)
    footer_frame    = Frame(child)

    header_frame.pack(fill="both",  expand="yes", padx=10, pady=10)
    tree_frame.pack(fill="both",    expand="yes", padx=10, pady=10)
    footer_frame.pack(fill="both",  expand="yes", padx=10, pady=10)


    # Read the Image
    image               = Image.open(join(dirname(__file__), "images/" + settings.my_event_image))
    # Resize the image using resize() method
    resize_image_event  = image.resize((150, 150))
    img1                = ImageTk.PhotoImage(resize_image_event)
    # create label and add resize image
    label1              = Label(header_frame, image=img1)
    label1.image        = img1
    label1.pack(side=tk.LEFT)

    yscrollbar = ttk.Scrollbar(tree_frame, orient='vertical')

    columns = ("Place", "Shooter", "Spotter", "Caliber", "Qualifying", "Finals", "Total")

    trv_dsp_shooter_scores = ttk.Treeview(tree_frame, yscrollcommand=yscrollbar.set, columns=columns, show="headings", height="20")
    trv_dsp_shooter_scores.grid(row=0, column=0, rowspan=20, columnspan=7, sticky=E+W)

    trv_dsp_shooter_scores.heading("Place",      text="Place",      anchor="w")
    trv_dsp_shooter_scores.heading("Shooter",    text="Shooter",    anchor="center")
    trv_dsp_shooter_scores.heading("Spotter",    text="Spotter",    anchor="center")
    trv_dsp_shooter_scores.heading("Caliber",    text="Caliber",    anchor="center")
    trv_dsp_shooter_scores.heading("Qualifying", text="Qualifying", anchor="center")
    trv_dsp_shooter_scores.heading("Finals",     text="Finals",     anchor="center")
    trv_dsp_shooter_scores.heading("Total",      text="Total",      anchor="center")

    trv_dsp_shooter_scores.column("#1", anchor="w", width=50,  stretch=True)
    trv_dsp_shooter_scores.column("#2", anchor="w", width=259, stretch=True)
    trv_dsp_shooter_scores.column("#3", anchor="w", width=250, stretch=True)
    trv_dsp_shooter_scores.column("#4", anchor="w", width=200, stretch=False)
    trv_dsp_shooter_scores.column("#5", anchor="w", width=110, stretch=False)
    trv_dsp_shooter_scores.column("#6", anchor="w", width=110, stretch=False)
    trv_dsp_shooter_scores.column("#7", anchor="w", width=110, stretch=False)

    yscrollbar.configure(command=trv_dsp_shooter_scores.yview())
    yscrollbar.grid(row=0, column=8, rowspan=10, sticky=NS)

    # Read the Image
    image               = Image.open(join(dirname(__file__), "images/" + settings.splash_footer))
    # Resize the image using resize() method
    resize_impactxs     = image.resize((930, 150))
    img2                = ImageTk.PhotoImage(resize_impactxs)
    # create label and add resize image
    label2              = Label(footer_frame, image=img2)
    label2.image        = img2
    label2.grid(row=0, column=0, padx=5, pady=5)

    settings.trv_dsp_shooter_scores = trv_dsp_shooter_scores
    settings.dsp_shooter_scores     = True              # Controls the events/dispatch refresh of the score trv update, aka block a update if the screen/trv is not displayed.

    paintScoreTrv()

    if debuglevel >= 2:
        my_logger.info('{time}, scores_display.display_all_shooters_scores.Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

   # settings.dsp_shooter_scores = False

# end display_all_shooters_scores


def paintScoreTrv():

    if debuglevel >= 2:
        my_logger.info('{time}, scores_display.paintScoreTrv.Called, {dsp_shooter_scores}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            dsp_shooter_scores=settings.dsp_shooter_scores
        ))

    if settings.dsp_shooter_scores:

        # Create new ordered array from global my_shooter_list
        ordered_my_shooter_list = sorted(settings.my_event_list["shooters"], key=settings.sort_by_key, reverse=True)

        #Retrieve the treeview into which we're going to pain
        trv_dsp_shooter_scores = settings.trv_dsp_shooter_scores

        # Cleanout my score trv structure
        for item in trv_dsp_shooter_scores.get_children():
            trv_dsp_shooter_scores.delete(item)

        # paint/repaint it
        rowIndex = 1
        for key in ordered_my_shooter_list:
            equipment = key["equipment"]  # Structure with equipment
            rifle = equipment['rifle']  # sub structure with rifle information
            scores = key["scores"]  # structure with scores

            trv_dsp_shooter_scores.insert('', index='end', iid=rowIndex, text="",
                                          values=(rowIndex,
                                                  key["first_name"].strip() + " " + key["last_name"].strip(),
                                                  key["spotter"],
                                                  rifle["caliber"],
                                                  scores['qualifying_score'],
                                                  scores['final_score'],
                                                  scores['total_score']))

            rowIndex += 1

    #end if

    if debuglevel >= 2:
        my_logger.info('{time}, scores_display.paintScoreTrv.Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))
    #end if
# end paint
