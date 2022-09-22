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
from datetime import datetime

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
    child.title = "Shooters"
    child.geometry("1000x700")
    child.configure(bg=frame_bg)

    tree_frame = Frame(child)

    # Determine where we're running, as template and events are by default subdirectories of the App directory.
    directory = os.getcwd()

    if debuglevel >= 1:
        my_logger.info('{time}, scores.load_all_shooters_scores.Current App Directory {directory}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            directory=directory
        ))

    trv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings", height="16")
    trv.grid(row=1, column=0, rowspan=16, columnspan=9)

    trv.heading(1, text="Action",       anchor="w")
    trv.heading(2, text="ID",           anchor="center")
    trv.heading(3, text="First Name",   anchor="center")
    trv.heading(4, text="Last Name",    anchor="center")
    trv.heading(5, text="ID Number",    anchor="center")
    trv.heading(6, text="Cell Phone",   anchor="center")
    trv.heading(7, text="eMail",        anchor="center")
    trv.heading(8, text="Team",         anchor="center")
    trv.heading(9, text="Spotter",      anchor="center")

    trv.column("#1", anchor="w", width=100, stretch=True)
    trv.column("#2", anchor="w", width=270, stretch=True)
    trv.column("#3", anchor="w", width=140, stretch=False)
    trv.column("#4", anchor="w", width=140, stretch=False)
    trv.column("#5", anchor="w", width=140, stretch=False)
    trv.column("#6", anchor="w", width=140, stretch=False)
    trv.column("#7", anchor="w", width=140, stretch=False)
    trv.column("#8", anchor="w", width=140, stretch=False)
    trv.column("#9", anchor="w", width=140, stretch=False)

    tree_frame.grid(row=0, column=0)


    def load_trv_with_json():

        for item in trv.get_children():
            trv.delete(item)

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters_scores.load_trv_with_json Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        rowIndex = 1

        for key in settings.my_shooter_list:
            guid_value  = key["id"]
            first_name  = key["first_name"]
            last_name   = key["last_name"]
            id_number   = key["id_number"]
            cell_phone  = key["cell_phone"]
            email       = key["email"]
            team        = key["team"]
            spotter     = key["spotter"]

            trv.insert('', index='end', iid=rowIndex, text="",
                       values=('edit', guid_value, first_name, last_name, id_number, cell_phone, email, team, spotter))
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
