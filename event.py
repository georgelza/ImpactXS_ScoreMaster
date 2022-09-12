########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
#
#   File            :   event.py
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
from tkinter import filedialog as fd
from datetime import datetime

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

    if debuglevel >= 1:
        my_logger.info('{time}, open_event_screen Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    child = Toplevel(root)
    child.geometry("768x700")
    child.title = "Events"
    
    child.configure(bg='LightBlue')
    load_form = True

    # Latout
    input_frame = LabelFrame(child, text='Event Profile', bg="lightgray", font=('Consolas', 14))
    input_frame.grid(row=0, rowspan=6, column=0)

    # house the Qualifying event common information and grid
    qual_frame = LabelFrame(child, text='Qualifying Profile', bg="lightgray", font=('Consolas', 14))
    qual_frame.grid(row=0, rowspan=7, column=0)

    # house the Final event common information and grid
    final_frame = LabelFrame(child, text='Final Profile', bg="lightgray", font=('Consolas', 14))
    final_frame.grid(row=0, rowspan=10, column=0)

    # House the buttons
    crtls_frame = LabelFrame(child, bg="lightgray", font=('Consolas', 14))
    crtls_frame.grid(row=0, rowspan=13, column=0)

    # Main Event Data
    l1 = Label(input_frame, text="Event Name",  width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l2 = Label(input_frame, text="Location",    width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l3 = Label(input_frame, text="Start Date",  width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l4 = Label(input_frame, text="End Date",    width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l5 = Label(input_frame, text="Distance",    width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))

    l1.grid(column=0, row=0, padx=1, pady=0)
    l2.grid(column=0, row=1, padx=1, pady=0)
    l3.grid(column=0, row=2, padx=1, pady=0)
    l4.grid(column=0, row=3, padx=1, pady=0)
    l5.grid(column=0, row=4, padx=1, pady=0)

    # Qualifying Event

    l11 = Label(qual_frame, text="Targets",  width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l12 = Label(qual_frame, text="Shots",    width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l13 = Label(qual_frame, text="Time Limit",  width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))

    l11.grid(column=0, row=7, padx=1, pady=0)
    l12.grid(column=0, row=8, padx=1, pady=0)
    l13.grid(column=0, row=9, padx=1, pady=0)
    # Qualifying table here

    # Final Event

    l21 = Label(final_frame, text="Targets",  width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l22 = Label(final_frame, text="Shots",    width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l23 = Label(final_frame, text="Time Limit",  width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))

    l21.grid(column=0, row=10, padx=1, pady=0)
    l22.grid(column=0, row=11, padx=1, pady=0)
    l23.grid(column=0, row=12, padx=1, pady=0)
    # Final table here




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
            "targets":      crm_q_target.get(),
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
            "targets":      crm_f_target.get(),
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
    crm_eventname   = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_Location    = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_Start_Date  = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_End_Date    = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_Distance    = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))

    # Qualifying Event data
    crm_q_target        = Entry(qual_frame, width=20, borderwidth=2, fg="black", font=('Consolas',14))
    crm_q_shots         = Entry(qual_frame, width=20, borderwidth=2, fg="black", font=('Consolas',14))
    crm_q_time_limit    = Entry(qual_frame, width=20, borderwidth=2, fg="black", font=('Consolas',14))

    # Finals Event data
    crm_f_target        = Entry(final_frame, width=20, borderwidth=2, fg="black", font=('Consolas',14))
    crm_f_shots         = Entry(final_frame, width=20, borderwidth=2, fg="black", font=('Consolas',14))
    crm_f_time_limit    = Entry(final_frame, width=20, borderwidth=2, fg="black", font=('Consolas',14))

    crm_eventname.grid(row=0, column=1)
    crm_Location.grid(row=1, column=1)
    crm_Start_Date.grid(row=2, column=1)
    crm_End_Date.grid(row=3, column=1)
    crm_Distance.grid(row=4, column=1)

    crm_q_target.grid(row=6, column=1)
    crm_q_shots.grid(row=7, column=1)
    crm_q_time_limit.grid(row=8, column=1)

    crm_f_target.grid(row=10, column=1)
    crm_f_shots.grid(row=11, column=1)
    crm_f_time_limit.grid(row=12, column=1)

    btnSave = Button(crtls_frame, text="Save", padx=5, pady=10, command=saveEvent)
    btnSave.grid(row=13, column=0)

    btnCancel = Button(crtls_frame, text="Cancel", padx=5, pady=10, command=cancelEvent)
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
    crm_q_target.delete(0, END)
    crm_q_target.insert(0, my_qualify["targets"])
    crm_q_shots.delete(0, END)
    crm_q_shots.insert(0, my_qualify["shots"])
    crm_q_time_limit.delete(0, END)
    crm_q_time_limit.insert(0, my_qualify["time_limit"])
    # Now paint the Treeview

    # Finals Event
    crm_f_target.delete(0, END)
    crm_f_target.insert(0, my_finals["targets"])
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