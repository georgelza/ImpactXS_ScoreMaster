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

    my_event_list = settings.my_event_list

    if debuglevel >= 1:
        my_logger.info('{time}, open_event_screen Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    child = Toplevel(root)
    child.geometry("768x500")
    child.title = "Events"
    
    child.configure(bg='LightBlue')
    load_form = True

    input_frame = LabelFrame(child, text='Event Profile', bg="lightgray", font=('Consolas', 14))
    input_frame.grid(row=0, rowspan=6, column=0)

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
        my_q_targets    = 3
        my_q_shots      = 4
        my_q_time_limit = 900
        my_qualifying = {
            "targets" :     my_q_targets,
            "shots":        my_q_shots,
            "time_limit":   my_q_time_limit,
            "target":       [
                {
                    "target_no": 0, "distance": 600
                },
                {
                    "target_no": 1, "distance": 800
                },
                {
                    "target_no": 2, "distance": 1000
                }
            ]
        }

        # Final
        my_f_targets    = 4
        my_f_shots      = 4
        my_f_time_limit = 900
        my_final = {
            "targets" :     my_f_targets,
            "shots":        my_f_shots,
            "time_limit":   my_f_time_limit,
            "target": [
                {
                    "target_no": 0, "distance": 800
                },
                {
                    "target_no": 1, "distance": 1200
                },
                {
                    "target_no": 2, "distance": 1400
                },
                {
                    "target_no": 3, "distance": 1685
                }
            ]
        }
        # Save
        settings.my_event_list      = my_event
        settings.my_qualifying_list = my_qualifying
        settings.my_final_list      = my_final
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

        if debuglevel >= 2:
            my_logger.info('{time}, open_event_screen.saveFinal Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end saveFinal

    crm_eventname   = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_Location    = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_Start_Date  = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_End_Date    = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_Distance    = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))

    btnSave = Button(input_frame, text="Save", padx=5, pady=10, command=saveEvent)
    btnSave.grid(row=5, column=0)

    btnCancel = Button(input_frame, text="Cancel", padx=5, pady=10, command=cancelEvent)
    btnCancel.grid(row=5, column=1)

    crm_eventname.grid(row=0, column=1)
    crm_Location.grid(row=1, column=1)
    crm_Start_Date.grid(row=2, column=1)
    crm_End_Date.grid(row=3, column=1)
    crm_Distance.grid(row=4, column=1)

    crm_eventname.delete(0, END)
    crm_eventname.insert(0, my_event_list["name"])
    crm_Location.delete(0, END)
    crm_Location.insert(0, my_event_list["location"])
    crm_Start_Date.delete(0, END)
    crm_Start_Date.insert(0, my_event_list["start_date"])
    crm_End_Date.delete(0, END)
    crm_End_Date.insert(0, my_event_list["end_date"])
    crm_Distance.delete(0, END)
    crm_Distance.insert(0, my_event_list["distance"])
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
        my_shooter_list     = my_event_list["shooter"]

    fh.close

    if debuglevel >= 2:
        my_logger.info('{time}, load_event_json_from_file.Printing my_event_list'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))
        settings.pp_json(my_event_list)

    if debuglevel >= 1:
        my_logger.info('{time}, load_event_json_from_file Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    return my_event_list

# end load_event_json_from_file