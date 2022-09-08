########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
#
#   File            :   shooters.py
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
import uuid
from datetime import datetime
from api.apputils import *


def load_shooters_data(my_event_list, my_logger, debuglevel):

    my_logger.info('{time}, load_shooters_data Entering '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    my_shooter_list = my_event_list["Shooters"]

    if debuglevel >= 2:
        my_logger.info('{time}, Printing my_shooter_list'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))
        pp_json(my_shooter_list)

    my_logger.info('{time}, load_shooters_data Exiting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    return my_shooter_list




def open_shooter_screen(root, myshooter_list, my_logger, debuglevel):

    my_logger.info('{time}, open_shooter_screen Entering '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    child = Toplevel(root)
    child.geometry("768x500")
    child.title="Maintain a individual Shooter"

    child.configure(bg='LightBlue')
    load_form = True

    id_value = StringVar()
    id_value.set(uuid.uuid4())

    input_frame = LabelFrame(child, text='Shooter Profile', bg="lightgray", font=('Consolas', 14))
    input_frame.grid(row=0, rowspan=5, column=0)

    l1 = Label(input_frame, text="First Name",  width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l2 = Label(input_frame, text="Last Name",   width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l3 = Label(input_frame, text="ID Number",   width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l4 = Label(input_frame, text="Cell Number", width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l5 = Label(input_frame, text="eMail",       width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))

    l1.grid(column=0, row=0, padx=1, pady=0)
    l2.grid(column=0, row=1, padx=1, pady=0)
    l3.grid(column=0, row=2, padx=1, pady=0)
    l4.grid(column=0, row=3, padx=1, pady=0)
    l5.grid(column=0, row=4, padx=1, pady=0)

    crm_firstname       = Entry(input_frame, width=30, borderwidth=2, fg="black",font=('Consolas', 14))
    crm_lastname        = Entry(input_frame, width=30, borderwidth=2, fg="black",font=('Consolas', 14))
    crm_idnumber        = Entry(input_frame, width=30, borderwidth=2, fg="black",font=('Consolas', 14))
    crm_cellnumber      = Entry(input_frame, width=30, borderwidth=2, fg="black",font=('Consolas', 14))
    crm_email           = Entry(input_frame, width=30, borderwidth=2, fg="black",font=('Consolas', 14))

    crm_firstname.grid(row=0, column=1)
    crm_lastname.grid(row=1, column=1)
    crm_idnumber.grid(row=2, column=1)
    crm_cellnumber.grid(row=3, column=1)
    crm_email.grid(row=4, column=1)

    load_form = False

    # Add Treeview showing target distances (as per main even structure).
    # Clicking on record allows to edit/save/discard values for distance

    # Add button to start timer as shooter starts shoot.
    # Allow scorer to open a Distance/ to be edited, time is saved when Hit/Miss is selected.

    # Add Button:
    # Save data to file or Cancel Updates and exit to main screen.

# end open_shooter_screen