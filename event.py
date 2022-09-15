########################################################################################################################
#
#
#   Project         :   ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
#
#   File            :   event.py
#
#   By              :   George Leonard ( georgelza@gmail.com )
#
#   Created         :   0.0.1 - 6 September 2022
#
#   Changelog       :   0.0.1 -
#
#   Notes           :   some ideas of tiling frames as a look https://www.youtube.com/watch?v=dlRXp4YSuG4
#
########################################################################################################################
__author__ = "George Leonard"
__email__ = "georgelza@gmail.com"
__version__ = "0.0.1"

from tkinter import *
from tkinter import filedialog as fd
from datetime import datetime
from tkcalendar import DateEntry

import json
import os

import settings

my_logger       = settings.my_logger
debuglevel      = settings.debuglevel

# Open/Select file dialog box
def select_file(mode):

    filetypes = (
        ('json files', '*.json'),
        ('All files', '*.*')
    )

    if debuglevel >= 1:
        my_logger.info('{time}, select_file Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # Determine where we running, as template and events are by default subdirectories of the App directory.
    directory = os.getcwd()
    if debuglevel >= 1:
        my_logger.info('{time}, select_file.Current App Directory {directory}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            directory=directory
        ))

        my_logger.info('{time}, select_file.Mode is {mode}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            mode=mode
        ))

    if mode == "New":
        # We're creating a new event, so lets present a event template.
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir=directory + '/template',
            filetypes=filetypes)
    else:
        #we're opening a previous defined event, so lets show saved events from ./events folder as default.
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir=directory + '/events',
            filetypes=filetypes)

    if filename:
        if debuglevel >= 1:
            my_logger.info('{time}, select_file.File Selected: {file}'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                file=filename
            ))
        return filename
    else:
        if debuglevel >= 1:
            my_logger.info('{time}, select_file.Aborted, No File Selected'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))
        return ""

# end select_file

def open_event_screen(root):

    my_event        = settings.my_event_list
    my_qualify      = settings.my_event_list["qualifying"]
    my_finals       = settings.my_event_list["final"]
    my_shooters     = settings.my_event_list["shooters"]

    # color'ing
    frame_bg            = settings.frame_bg
    frame_fg            = settings.frame_fg
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
        my_logger.info('{time}, open_event_screen Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    child = Toplevel(root)
    child.title = "Events Maintenance"
    child.geometry("825x465")
    child.configure(bg=frame_bg)

    load_form = True

    input_frame = Frame(child)
    qual_frame  = Frame(child)
    final_frame = Frame(child)
    crtls_frame = Frame(child)

    # Event Frame Layout
    input_lbframe = LabelFrame(input_frame, text='Event Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
    input_lbframe.grid()
    input_frame.grid(row=0, rowspan=6, column=0, columnspan=12, sticky="W", pady=(1,5))

    # Qualifications Event Layout
    qual_lbframe = LabelFrame(qual_frame, text='Qualifying Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
    qual_lbframe.grid()
    qual_frame.grid(row=6, rowspan=5, column=0, columnspan=3, sticky="W", padx=(0,5))

    # Final Event Layout
    final_lbframe = LabelFrame(final_frame, text='Final Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
    final_lbframe.grid()
    final_frame.grid(row=6, rowspan=5, column=3, columnspan=3, sticky="W")

    # Controlling Buttons
    crtls_lbframe = LabelFrame(crtls_frame, bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
    crtls_lbframe.grid()
    crtls_frame.grid(row=12, rowspan=4, column=0, sticky="W", pady=(5,0))

    # Event Frame Layout
    lb_crm_eventname    = Label(input_lbframe, text="Event Name",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_Location     = Label(input_lbframe, text="Location",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_Start_Date   = Label(input_lbframe, text="Start Date",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_End_Date     = Label(input_lbframe, text="End Date",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_Distance     = Label(input_lbframe, text="Distance",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))

    lb_crm_eventname.grid   (column=0, row=0, padx=1, pady=0)
    lb_crm_Location.grid    (column=0, row=1, padx=1, pady=0)
    lb_crm_Start_Date.grid  (column=0, row=2, padx=1, pady=0)
    lb_crm_End_Date.grid    (column=0, row=3, padx=1, pady=0)
    lb_crm_Distance.grid    (column=0, row=4, padx=1, pady=0)


    crm_eventname   = Entry(input_lbframe, width=40, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
    crm_Location    = Entry(input_lbframe, width=40, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
    crm_Start_Date  = DateEntry(input_lbframe, width=39, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size), date_pattern='dd/mm/yy', selectmode='day')
    crm_End_Date    = DateEntry(input_lbframe, width=39, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size), date_pattern='dd/mm/yy', selectmode='day')
    crm_Distance    = Entry(input_lbframe, width=40, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))

    crm_eventname.grid  (column=1, row=0)
    crm_Location.grid   (column=1, row=1)
    crm_Start_Date.grid (column=1, row=2)
    crm_End_Date.grid   (column=1, row=3)
    crm_Distance.grid   (column=1, row=4)

    # Qualifications Event Layout
    lb_crm_q_targets    = Label(qual_lbframe, text="Targets",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_q_shots      = Label(qual_lbframe, text="Shots",       width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_q_time_limit = Label(qual_lbframe, text="Time Limit",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))

    lb_crm_q_targets.grid(column=0, row=0, padx=1, pady=0)
    lb_crm_q_shots.grid(column=0, row=1, padx=1, pady=0)
    lb_crm_q_time_limit.grid(column=0, row=2, padx=1, pady=0)

    crm_q_targets       = Entry(qual_lbframe, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
    crm_q_shots         = Entry(qual_lbframe, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
    crm_q_time_limit    = Entry(qual_lbframe, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))

    crm_q_targets.grid(row=0, column=2)
    crm_q_shots.grid(row=1, column=2)
    crm_q_time_limit.grid(row=2, column=2)

    # Finals Event Layout
    lb_crm_f_targets    = Label(final_lbframe, text="Targets",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_f_shots      = Label(final_lbframe, text="Shots",      width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_f_time_limit = Label(final_lbframe, text="Time Limit", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))

    lb_crm_f_targets.grid(column=0, row=0, padx=1, pady=0)
    lb_crm_f_shots.grid(column=0, row=1, padx=1, pady=0)
    lb_crm_f_time_limit.grid(column=0, row=2, padx=1, pady=0)

    crm_f_targets       = Entry(final_lbframe, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
    crm_f_shots         = Entry(final_lbframe, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
    crm_f_time_limit    = Entry(final_lbframe, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))

    crm_f_targets.grid(column=2, row=0, padx=1, pady=0)
    crm_f_shots.grid(column=2, row=1, padx=1, pady=0)
    crm_f_time_limit.grid(column=2, row=2, padx=1, pady=0)

    # Qualifications treeview here

    # Finals treeview here

    def cancelEvent():

        if debuglevel >= 2:
            my_logger.info('{time}, open_event_screen.cancelEvent Called '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        child.destroy()

        if debuglevel >= 2:
            my_logger.info('{time}, open_event_screen.cancelEvent Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end cancelEvent

    # Add Buttons:
    # Save data to file or Cancel Updates and exit to main screen
    def saveEvent():

        if debuglevel >= 2:
            my_logger.info('{time}, open_event_screen.saveEvent Called '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        # Save data to my_event_list
        my_event = {
            "name":         crm_eventname.get(),
            "location":     crm_Location.get(),
            "start_date":   crm_Start_Date.get(),
            "end_date":     crm_End_Date.get(),
            "distance":     crm_Distance.get()
        }

        # Qualifying
        my_qualifying = {
            "targets":      crm_q_targets.get(),
            "shots":        crm_q_shots.get(),
            "time_limit":   crm_q_time_limit.get(),
            "target":       [
                {
                    "target_no": 0, "distance": 800
                },
                {
                    "target_no": 1, "distance": 1000
                },
                {
                    "target_no": 2, "distance": 1300
                },
                {
                    "target_no": 3, "distance": 1600
                }
            ]
        }

        # Final
        my_final = {
            "targets":      crm_f_targets.get(),
            "shots":        crm_f_shots.get(),
            "time_limit":   crm_q_time_limit.get(),
            "target": [
                {
                    "target_no": 0, "distance": 1800
                },
                {
                    "target_no": 1, "distance": 2500
                },
                {
                    "target_no": 2, "distance": 3000
                },
                {
                    "target_no": 3, "distance": 3500
                }
            ]
        }

        # Save
        settings.my_event_list      = my_event
        settings.my_qualifying_list = my_qualifying
        settings.my_final_list      = my_final
        settings.my_shooter_list    = my_shooters
        settings.save_json_to_file(settings.filename)

        # cleanup
        child.destroy()

        if debuglevel >= 2:
            my_logger.info('{time}, open_event_screen.saveEvent Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end saveEvent

    def saveQualifying():
        if debuglevel >= 2:
            my_logger.info('{time}, open_event_screen.saveQualifying Called '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        settings.save_json_to_file(settings.filename)


        if debuglevel >= 2:
            my_logger.info('{time}, open_event_screen.saveQualifying Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end saveQualifying

    def saveFinal():
        if debuglevel >= 2:
            my_logger.info('{time}, open_event_screen.saveFinal Called '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        settings.save_json_to_file(settings.filename)

        if debuglevel >= 2:
            my_logger.info('{time}, open_event_screen.saveFinal Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end saveFinal

    # Main Event Common Data

    btnSave = Button(crtls_lbframe, text="Save", padx=5, pady=10, command=saveEvent)
    btnSave.grid(row=13, column=0)

    btnCancel = Button(crtls_lbframe, text="Cancel", padx=5, pady=10, command=cancelEvent)
    btnCancel.grid(row=13, column=1)

    # Insert/Paint the screen with the data as we have it currently
    # Main Event
    crm_eventname.delete(0, END)
    crm_eventname.insert(0, my_event["name"])
    crm_Location.delete(0, END)
    crm_Location.insert(0, my_event["location"])
    crm_Start_Date.delete(0, END)
    crm_Start_Date.insert(0, my_event["start_date"])
    crm_End_Date.delete(0, END)
    crm_End_Date.insert(0, my_event["end_date"])
    crm_Distance.delete(0, END)
    crm_Distance.insert(0, my_event["distance"])

    # Qualifying Event
    crm_q_targets.delete(0, END)
    crm_q_targets.insert(0, my_qualify["targets"])
    crm_q_shots.delete(0, END)
    crm_q_shots.insert(0, my_qualify["shots"])
    crm_q_time_limit.delete(0, END)
    crm_q_time_limit.insert(0, my_qualify["time_limit"])
    # Now paint the Treeview

    # Finals Event
    crm_f_targets.delete(0, END)
    crm_f_targets.insert(0, my_finals["targets"])
    crm_f_shots.delete(0, END)
    crm_f_shots.insert(0, my_finals["shots"])
    crm_f_time_limit.delete(0, END)
    crm_f_time_limit.insert(0, my_finals["time_limit"])
    # Now paint the Treeview

    load_form = False

    # Add Treeview (and buttons Add/Edit/Delete) to define Qualifying and Final distances.

    if debuglevel >= 1:
        my_logger.info('{time}, open_event_screen Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end open_event_screen


def load_event_json_from_file(file):

    if debuglevel >= 1:
        my_logger.info('{time}, load_event_json_from_file Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

        my_logger.info('{time}, load_event_json_from_file.Loading file: {file}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=file
        ))

    with open(file, "r") as fh:
        my_event_list       = json.load(fh)
        my_qualifying_list  = my_event_list["qualifying"]
        my_final_list       = my_event_list["final"]
        my_shooter_list     = my_event_list["shooters"]

    fh.close

    if debuglevel >= 2:
        my_logger.info('{time}, load_event_json_from_file.Printing my_event_list'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))
        print("------ my_event_list ------")
        settings.pp_json(my_event_list)

        print("------ my_qualifying_list ------")
        settings.pp_json(my_qualifying_list)

        print("------ my_final_list ------")
        settings.pp_json(my_final_list)

        print("------ my_shooter_list ------")
        settings.pp_json(my_shooter_list)

        print("--------------------------------")

    if debuglevel >= 1:
        my_logger.info('{time}, load_event_json_from_file Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    return my_event_list

# end load_event_json_from_file