########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
#
#   File            :   Event.py
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

import json
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Scrollbar
from datetime import datetime
from api.apputils import *


def load_event_data(file, my_logger, debuglevel):


    my_logger.info('{time}, load_event_data Entering '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    my_logger.info('{time}, Opening file: {file}'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
        file=file
    ))

    with open(file, "r") as fh:
        my_event_list = json.load(fh)
    fh.close

    if debuglevel >= 2:
        my_logger.info('{time}, Printing my_event_list'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))
        pp_json(my_event_list)

    my_logger.info('{time}, load_event_data Exiting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    return my_event_list

# end load_event_data



def open_event_screen(root, myevent_list, my_logger, debuglevel):

    my_logger.info('{time}, open_event_screen Entering '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    child = Toplevel(root)
    child.geometry("768x500")
    child.title = "Events"

    id_value = StringVar()
    id_value.set(myevent_list["uuid"])
    
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

    def cancelAction():
        child.destroy()

    #end cancelAction

    # Add Buttons:
    # Save data to file or Cancel Updates and exit to main screen
    def saveAction():
        my_logger.info('{time}, open_event_screen.saveAction Entering '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # end saveAction

    crm_eventname   = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_Location    = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_Start_Date  = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_End_Date    = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))
    crm_Distance    = Entry(input_frame, width=40, borderwidth=2, fg="black", font=('Consolas',14))

    btnSave = Button(input_frame, text="Save", padx=5, pady=10, command=saveAction)
    btnSave.grid(row=5, column=0)

    btnCancel = Button(input_frame, text="Cancel", padx=5, pady=10, command=cancelAction)
    btnCancel.grid(row=5, column=1)

    crm_eventname.grid(row=0, column=1)
    crm_Location.grid(row=1, column=1)
    crm_Start_Date.grid(row=2, column=1)
    crm_End_Date.grid(row=3, column=1)
    crm_Distance.grid(row=4, column=1)

    crm_eventname.delete(0, END)
    crm_eventname.insert(0, myevent_list["Name"])
    crm_Location.delete(0, END)
    crm_Location.insert(0, myevent_list["Location"])
    crm_Start_Date.delete(0, END)
    crm_Start_Date.insert(0, myevent_list["Start_Date"])
    crm_End_Date.delete(0, END)
    crm_End_Date.insert(0, myevent_list["End_Date"])
    crm_Distance.delete(0, END)
    crm_Distance.insert(0, myevent_list["Distance"])
    load_form = False

    # Add Treeview (and buttons Add/Edit/Delete) to define Qualifying and Final distances.


# end open_event_screen