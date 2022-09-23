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

from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

import uuid
import json
import os

import settings

my_logger       = settings.my_logger
debuglevel      = settings.debuglevel


# Refresh data in memory from file (include updating global settings variable),
# shooters include their personal data,
# equipment and scores
def load_shooter_json_from_file(myfile):

    if debuglevel >= 1:
        my_logger.info('{time}, shooters.load_shooter_json_from_file Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    with open(myfile, "r") as file_handler:
        settings.my_event_list = json.load(file_handler)
        settings.my_shooter_list = settings.my_event_list["shooters"]

    file_handler.close

    settings.pp_json(settings.my_shooter_list)

    if debuglevel >= 1:
        my_logger.info('{time}, shooters.load_shooter_json_from_file.file has been read and closed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_shooter_json_from_file

def find_rec_in_my_shooter_list(guid_value):

    if debuglevel >= 2:
        my_logger.info('{time}, shooters.find_rec_in_my_shooter_list Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    row = 0
    found = False

    for rec in settings.my_shooter_list:
        if rec["id"] == guid_value:
            found = True
            break

    if (found == True):
        return (rec)

    return (-1)

#end find_rec_in_my_shooter_list


# We will add the scores via the File/scores menu.
# For now ust build Scott's Treeview and user editor, then replace with my data.
def load_all_shooters(main_window):

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
        my_logger.info('{time}, shooters.load_all_shooters Called '.format(
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
        my_logger.info('{time}, shooters.load_all_shooters.Current App Directory {directory}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            directory=directory
        ))

    def make_new_record():

        if debuglevel >= 2:
            my_logger.info('{time}, shooters.load_all_shooters.make_new_record Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        emptyRecord = dict()
        open_popup('add', emptyRecord, tree_frame)

    #end make_new_record

    btnNewRecord = Button(tree_frame, text="Add New", bg="#34d2eb", padx=2, pady=3, command=lambda: make_new_record())
    btnNewRecord.grid(row=0, column=0, sticky="w")

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

    def remove_all_data_from_trv():

        if debuglevel >= 2:
            my_logger.info('{time}, shooters.load_all_shooters.remove_all_data_from_trv Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        for item in trv.get_children():
            trv.delete(item)

        if debuglevel >= 2:
            my_logger.info('{time}, shooters.load_all_shooters.remove_all_data_from_trv Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # Reload trv with all shooters data

    def load_trv_with_json():

        if debuglevel >= 2:
            my_logger.info('{time}, shooters.load_all_shooters.load_trv_with_json Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        remove_all_data_from_trv()

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
            my_logger.info('{time}, shooters.load_all_shooters.load_trv_with_json Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end load_trv_with_json

    def MouseButtonUpCallBack(event):
        global trv

        if debuglevel >= 2:
            my_logger.info('{time}, shooters.load_all_shooters.MouseButtonUpCallBack Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        currentRowIndex = trv.selection()[0]

        my_logger.info('{time}, shooters.load_all_shooters.MouseButtonUpCallBack Called Cur Row Index: {currentRowIndex}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            currentRowIndex=currentRowIndex
        ))

        lastTuple = (trv.item(currentRowIndex, 'values'))
        # Get from my_shooter_list dictionary the entire record matching the lastTuple[1], this is the id column
        my_jsonrec = find_rec_in_my_shooter_list(lastTuple[1])
        open_popup('edit', my_jsonrec, tree_frame)

        if debuglevel >= 2:
            my_logger.info('{time}, shooters.load_all_shooters.MouseButtonUpCallBack Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end MouseButtonUpCallBack

    # Lets design/pain the popup, this is what is opened when the user clicks on a shooter in the treeview.
    def open_popup(_mode, json_record, primary):

        if _mode == 'add':
            scores = {}
        else:
            # json_record is the entire record of the current shooter,
            scores = json_record["scores"]

        if debuglevel >= 2:
            my_logger.info('{time}, shooters.load_all_shooters.open_popup Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

            my_logger.info('{time}, shooters.load_all_shooters.open_popup Current Shooter'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))
            settings.pp_json(json_record)

        child = Toplevel(primary)
        child.title('Shooter Maintenance')
        child.geometry("1100x825")
        child.configure(bg=frame_bg)
        child.grab_set()  # allow it to receive events

        load_form = True

        shooter_frame   = Frame(child)
        rifle_frame     = Frame(child)
        scope_frame     = Frame(child)
        cartridge_frame = Frame(child)
        cntrls_frame    = Frame(child)

        # Frame Layout
        shooter_lbframe = LabelFrame(shooter_frame, text='Shooter Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        shooter_lbframe.grid()
        shooter_frame.grid(row=0, rowspan=10, column=0, columnspan=4, sticky="W", pady=(1, 5))

        # Frame Layout : Shooter
        rifle_lbframe = LabelFrame(rifle_frame, text='Rifle Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        rifle_lbframe.grid()
        rifle_frame.grid(row=11, rowspan=11, column=0, columnspan=4, sticky="W", padx=(1, 5))

        # Frame Layout : Rifle
        scope_lbframe = LabelFrame(scope_frame, text='Scope Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        scope_lbframe.grid()
        scope_frame.grid(row=0, rowspan=5, column=6, columnspan=3, sticky="W", padx=(1, 5))

        # Frame Layout : Cartridge
        cartridge_lbframe = LabelFrame(cartridge_frame, text='Cartridge Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        cartridge_lbframe.grid()
        cartridge_frame.grid(row=11, rowspan=10, column=6, columnspan=4, sticky="W", padx=(1, 5))

        # Frame Layout : Buttons
        cntrls_lbframe = LabelFrame(cntrls_frame, bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size), relief=RIDGE)
        cntrls_lbframe.grid()
        cntrls_frame.grid(row=22, rowspan=4, column=0, columnspan=8, sticky="W", pady=(5, 0))

        # Shooter
        lb_shooter1 = Label(shooter_lbframe, text="ID",            width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter2 = Label(shooter_lbframe, text="First Name",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter3 = Label(shooter_lbframe, text="Last Name",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter4 = Label(shooter_lbframe, text="ID Number",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter5 = Label(shooter_lbframe, text="Cell Phone",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter6 = Label(shooter_lbframe, text="eMail",         width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter7 = Label(shooter_lbframe, text="Team",          width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter8 = Label(shooter_lbframe, text="Spotter",       width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

        lb_shooter1.grid(row=1, column=0, padx=5, pady=0)
        lb_shooter2.grid(row=2, column=0, padx=5, pady=0)
        lb_shooter3.grid(row=3, column=0, padx=5, pady=0)
        lb_shooter4.grid(row=4, column=0, padx=5, pady=0)
        lb_shooter5.grid(row=5, column=0, padx=5, pady=0)
        lb_shooter6.grid(row=6, column=0, padx=5, pady=0)
        lb_shooter7.grid(row=7, column=0, padx=5, pady=0)
        lb_shooter8.grid(row=8, column=0, padx=5, pady=0)

        id_value = StringVar()
        id_value.set(uuid.uuid4())

        # Shooter
        crm_shooter_id = Label(shooter_lbframe, anchor="w", height=1, relief="ridge", textvariable=id_value, font=(txtfont, txtfont_size))
        crm_shooter_id.grid(row=1, column=1, padx=20)

        crm_shooter_fn = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_fn.grid(row=2, column=1)

        crm_shooter_ln = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_ln.grid(row=3, column=1)

        crm_shooter_id_number = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_id_number.grid(row=4, column=1)

        crm_shooter_cellphone = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_cellphone.grid(row=5, column=1)

        crm_shooter_email = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_email.grid(row=6, column=1)

        crm_shooter_team = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_team.grid(row=7, column=1)

        crm_shooter_spotter = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_spotter.grid(row=8, column=1)


        # Rifle
        lb_rifle1 = Label(rifle_lbframe, text="Make",         width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_rifle2 = Label(rifle_lbframe, text="Model",        width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_rifle3 = Label(rifle_lbframe, text="Caliber",      width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_rifle4 = Label(rifle_lbframe, text="Chassis",      width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_rifle5 = Label(rifle_lbframe, text="Trigger",      width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_rifle6 = Label(rifle_lbframe, text="Break",        width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_rifle7 = Label(rifle_lbframe, text="Supressor",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_rifle8 = Label(rifle_lbframe, text="Weight (lb)",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_rifle9 = Label(rifle_lbframe, text="Bipod",        width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_rifle10 = Label(rifle_lbframe, text="Software",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

        lb_rifle1.grid(row=1, column=0, padx=5, pady=0)
        lb_rifle2.grid(row=2, column=0, padx=5, pady=0)
        lb_rifle3.grid(row=3, column=0, padx=5, pady=0)
        lb_rifle4.grid(row=4, column=0, padx=5, pady=0)
        lb_rifle5.grid(row=5, column=0, padx=5, pady=0)
        lb_rifle6.grid(row=6, column=0, padx=5, pady=0)
        lb_rifle7.grid(row=7, column=0, padx=5, pady=0)
        lb_rifle8.grid(row=8, column=0, padx=5, pady=0)
        lb_rifle9.grid(row=9, column=0, padx=5, pady=0)
        lb_rifle10.grid(row=10, column=0, padx=5, pady=0)

        crm_rifle_make = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_make.grid(row=1, column=1)

        crm_rifle_model = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_model.grid(row=2, column=1)

        crm_rifle_cal = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_cal.grid(row=3, column=1)

        crm_rifle_chassis = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_chassis.grid(row=4, column=1)

        crm_rifle_trigger = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_trigger.grid(row=5, column=1)

        crm_rifle_break = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_break.grid(row=6, column=1)

        crm_rifle_supressor = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_supressor.grid(row=7, column=1)

        crm_rifle_weight = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_weight.grid(row=8, column=1)

        crm_rifle_bipod = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_bipod.grid(row=9, column=1)

        crm_rifle_software = Entry(rifle_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_rifle_software.grid(row=10, column=1)


        # Scope
        lb_scope1 = Label(scope_lbframe, text="Make",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope2 = Label(scope_lbframe, text="Model",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope3 = Label(scope_lbframe, text="Rings",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope4 = Label(scope_lbframe, text="MOA Rise", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

        lb_scope1.grid(row=1, column=0, padx=5, pady=0)
        lb_scope2.grid(row=2, column=0, padx=5, pady=0)
        lb_scope3.grid(row=3, column=0, padx=5, pady=0)
        lb_scope4.grid(row=4, column=0, padx=5, pady=0)

        crm_scope_make = Entry(scope_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_scope_make.grid(row=1, column=1, padx=5, pady=0)

        crm_scope_model = Entry(scope_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_scope_model.grid(row=2, column=1, padx=5, pady=0)

        crm_scope_rings = Entry(scope_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_scope_rings.grid(row=3, column=1, padx=5, pady=0)

        crm_scope_moa_rise = Entry(scope_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_scope_moa_rise.grid(row=4, column=1, padx=5, pady=0)


        # Cartridge
        lb_scope1 = Label(cartridge_lbframe, text="Brass",        width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope2 = Label(cartridge_lbframe, text="Bullet Make",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope3 = Label(cartridge_lbframe, text="Bullet Model", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope4 = Label(cartridge_lbframe, text="Bullet Weight",width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope5 = Label(cartridge_lbframe, text="Primer Make",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope6 = Label(cartridge_lbframe, text="Primer Model", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope7 = Label(cartridge_lbframe, text="Powder Make",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_scope8 = Label(cartridge_lbframe, text="Powder Model", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

        lb_scope1.grid(row=1, column=0, padx=5, pady=0)
        lb_scope2.grid(row=2, column=0, padx=5, pady=0)
        lb_scope3.grid(row=3, column=0, padx=5, pady=0)
        lb_scope4.grid(row=4, column=0, padx=5, pady=0)
        lb_scope5.grid(row=5, column=0, padx=5, pady=0)
        lb_scope6.grid(row=6, column=0, padx=5, pady=0)
        lb_scope7.grid(row=7, column=0, padx=5, pady=0)
        lb_scope8.grid(row=8, column=0, padx=5, pady=0)

        crm_cartridge_brass_make = Entry(cartridge_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_cartridge_brass_make.grid(row=1, column=1, padx=5, pady=0)

        crm_cartridge_bullet_make = Entry(cartridge_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_cartridge_bullet_make.grid(row=2, column=1, padx=5, pady=0)

        crm_cartridge_bullet_model = Entry(cartridge_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_cartridge_bullet_model.grid(row=3, column=1, padx=5, pady=0)

        crm_cartridge_bullet_weight = Entry(cartridge_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_cartridge_bullet_weight.grid(row=4, column=1, padx=5, pady=0)

        crm_cartridge_primer_make = Entry(cartridge_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_cartridge_primer_make.grid(row=5, column=1, padx=5, pady=0)

        crm_cartridge_primer_model = Entry(cartridge_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_cartridge_primer_model.grid(row=6, column=1, padx=5, pady=0)

        crm_cartridge_powder_make = Entry(cartridge_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_cartridge_powder_make.grid(row=7, column=1, padx=5, pady=0)

        crm_cartridge_powder_model = Entry(cartridge_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_cartridge_powder_model.grid(row=8, column=1, padx=5, pady=0)

        # button
        btnAdd = Button(cntrls_lbframe, text="Save", padx=5, pady=10, command=lambda: determineAction())
        btnAdd.grid(row=0, column=0)

        btnDelete = Button(cntrls_lbframe, text="Delete", padx=5, pady=10, command=lambda: delete_record())
        btnDelete.grid(row=0, column=2)

        btnCancel = Button(cntrls_lbframe, text="Cancel", padx=5, pady=10, command=lambda: child_cancel())
        btnCancel.grid(row=0, column=3)

        load_form = False

        def delete_record():

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.delete_record Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            guid_value  = id_value.get()
            first_name  = crm_shooter_fn.get()
            last_name   = crm_shooter_ln.get()
            id_number   = crm_shooter_id_number.get()
            cell_phone  = crm_shooter_cellphone.get()
            email       = crm_shooter_email.get()
            team        = crm_shooter_team.get()
            spotter     = crm_shooter_spotter.get()

            equipment   = ""
            scores      = ""

            # Confirm Deletion
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this Shooter?"):

                my_logger.info('{time}, shooters.load_all_shooters.delete_record Confirmed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

                process_request('_DELETE_', guid_value, first_name, last_name, id_number, cell_phone, email, team, spotter, equipment, scores)
                reload_main_form()
                child.grab_release()
                child.destroy()
                child.update()

            else:
                my_logger.info('{time}, shooters.load_all_shooters.delete_record Cancelled'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.delete_record Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end delete_record

        def child_cancel():

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.child_cancel Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            child.grab_release()
            child.destroy()
            child.update()

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.child_cancel Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end child_cancel

        def reload_main_form():

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.reload_main_form Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            load_trv_with_json()

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.reload_main_form Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
        def change_background_color(new_color):

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.change_background_color Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            # Shooter
            crm_shooter_fn.config(bg=new_color)
            crm_shooter_ln.config(bg=new_color)
            crm_shooter_id_number.config(bg=new_color)
            crm_shooter_cellphone.config(bg=new_color)
            crm_shooter_email.config(bg=new_color)
            crm_shooter_team.config(bg=new_color)
            crm_shooter_spotter.config(bg=new_color)

            # Equipment
            # Rifle
            crm_rifle_make.config(bg=new_color)
            crm_rifle_model.config(bg=new_color)
            crm_rifle_cal.config(bg=new_color)
            crm_rifle_chassis.config(bg=new_color)
            crm_rifle_trigger.config(bg=new_color)
            crm_rifle_break.config(bg=new_color)
            crm_rifle_supressor.config(bg=new_color)
            crm_rifle_weight.config(bg=new_color)
            crm_rifle_bipod.config(bg=new_color)
            crm_rifle_software.config(bg=new_color)

            # Scope
            crm_scope_make.config(bg=new_color)
            crm_scope_model.config(bg=new_color)
            crm_scope_rings.config(bg=new_color)
            crm_scope_moa_rise.config(bg=new_color)

            # Cartridge
            crm_cartridge_brass_make.config(bg=new_color)
            crm_cartridge_bullet_make.config(bg=new_color)
            crm_cartridge_bullet_model.config(bg=new_color)
            crm_cartridge_bullet_weight.config(bg=new_color)
            crm_cartridge_primer_make.config(bg=new_color)
            crm_cartridge_primer_model.config(bg=new_color)
            crm_cartridge_powder_make.config(bg=new_color)
            crm_cartridge_powder_model.config(bg=new_color)

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.change_background_color Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end change_background_color

        def add_entry():

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.add_entry Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            # shooter
            guid_value  = id_value.get()
            first_name  = crm_shooter_fn.get()
            last_name   = crm_shooter_ln.get()
            id_number   = crm_shooter_id_number.get()
            cell_phone  = crm_shooter_cellphone.get()
            email       = crm_shooter_email.get()
            team        = crm_shooter_team.get()
            spotter     = crm_shooter_spotter.get()

            # equipment
            # rifle
            rifle = {
                "make":             crm_rifle_make.get(),
                "model":            crm_rifle_model.get(),
                "caliber":          crm_rifle_cal.get(),
                "chassis":          crm_rifle_chassis.get(),
                "trigger":          crm_rifle_trigger.get(),
                "break":            crm_rifle_break.get(),
                "supressor":        crm_rifle_supressor.get(),
                "weight":           crm_rifle_weight.get(),
                "bipod":            crm_rifle_bipod.get(),
                "software":         crm_rifle_software.get(),
            }

            # scope
            scope = {
                "make":             crm_scope_make.get(),
                "model":            crm_scope_model.get(),
                "rings":            crm_scope_rings.get(),
                "moa_rise":         crm_scope_moa_rise.get()
            }

            # cartridge
            cartridge = {
                "brass_make":       crm_cartridge_brass_make.get(),
                "bullet_make":      crm_cartridge_bullet_make.get(),
                "bullet_model":     crm_cartridge_bullet_model.get(),
                "bullet_weight":    crm_cartridge_bullet_weight.get(),
                "primer_make":      crm_cartridge_primer_make.get(),
                "primer_model":     crm_cartridge_primer_model.get(),
                "powder_make":      crm_cartridge_powder_make.get(),
                "powder_model":     crm_cartridge_powder_model.get(),
            }

            equipment = {
                "rifle":        rifle,
                "scope":        scope,
                "cartridge":    cartridge
            }

            # scores
            # Place a blank set of tags here for now, this is a new shooter so does not have any scores yet.
            # will be populated via the scoring entry window
            scores   = {
                "qualifying_score": 0,
                "final_score": 0,
                "qualifying": "",
                "final": ""
            }

            if len(first_name) == 0:
                change_background_color("#FFB2AE")
                return

            process_request('_INSERT_', guid_value, first_name, last_name, id_number, cell_phone, email, team, spotter, equipment, scores)

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.add_entry Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end add_entry

        def update_entry():


            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.update_entry Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            # shooter
            guid_value  = id_value.get()
            first_name  = crm_shooter_fn.get()
            last_name   = crm_shooter_ln.get()
            id_number   = crm_shooter_id_number.get()
            cell_phone  = crm_shooter_cellphone.get()
            email       = crm_shooter_email.get()
            team        = crm_shooter_team.get()
            spotter     = crm_shooter_spotter.get()

            # equipment
            # rifle
            rifle = {
                "make":             crm_rifle_make.get(),
                "model":            crm_rifle_model.get(),
                "caliber":          crm_rifle_cal.get(),
                "chassis":          crm_rifle_chassis.get(),
                "trigger":          crm_rifle_trigger.get(),
                "break":            crm_rifle_break.get(),
                "supressor":        crm_rifle_supressor.get(),
                "weight":           crm_rifle_weight.get(),
                "bipod":            crm_rifle_bipod.get(),
                "software":         crm_rifle_software.get(),
            }

            # scope
            scope = {
                "make":             crm_scope_make.get(),
                "model":            crm_scope_model.get(),
                "rings":            crm_scope_rings.get(),
                "moa_rise":         crm_scope_moa_rise.get()
            }

            # cartridge
            cartridge = {
                "brass_make":       crm_cartridge_brass_make.get(),
                "bullet_make":      crm_cartridge_bullet_make.get(),
                "bullet_model":     crm_cartridge_bullet_model.get(),
                "bullet_weight":    crm_cartridge_bullet_weight.get(),
                "primer_make":      crm_cartridge_primer_make.get(),
                "primer_model":     crm_cartridge_primer_model.get(),
                "powder_make":      crm_cartridge_powder_make.get(),
                "powder_model":     crm_cartridge_powder_model.get(),
            }

            equipment = {
                "rifle":        rifle,
                "scope":        scope,
                "cartridge":    cartridge
            }

            # !!!!!!!!!!!!!!! PLACE HOLDER !!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #m_qual_scores = 0
            #m_final_scores = 0
            # scores
            #scores = {
            #    "qualifying_score": 0,
            #    "final_score": 0,
            #    "qualifying": [{"scores": m_qual_scores}],
            #    "final": [{"scores": m_final_scores}]
            #}

            if len(first_name) == 0:
                change_background_color("#FFB2AE")
                return

            process_request('_UPDATE_', guid_value, first_name, last_name, id_number, cell_phone, email, team, spotter, equipment, scores)

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.update_entry Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end update_entry

        def load_edit_field_with_row_data(json_record):

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.load_edit_field_with_row_data Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            if len(json_record) == 0:
                return

            equipment   = json_record["equipment"]
            rifle       = equipment["rifle"]
            scope       = equipment["scope"]
            cartridge   = equipment["cartridge"]
            scores      = json_record["scores"]

            # shooter
            id_value.set(json_record["id"])
            crm_shooter_fn.delete(0, END)
            crm_shooter_fn.insert(0, json_record["first_name"])
            crm_shooter_ln.delete(0, END)
            crm_shooter_ln.insert(0, json_record["last_name"])
            crm_shooter_id_number.delete(0, END)
            crm_shooter_id_number.insert(0, json_record["id_number"])
            crm_shooter_cellphone.delete(0, END)
            crm_shooter_cellphone.insert(0, json_record["cell_phone"])
            crm_shooter_email.delete(0, END)
            crm_shooter_email.insert(0, json_record["email"])
            crm_shooter_team.delete(0, END)
            crm_shooter_team.insert(0, json_record["team"])
            crm_shooter_spotter.delete(0, END)
            crm_shooter_spotter.insert(0, json_record["spotter"])

            # Equipment
            # rifle
            crm_rifle_make.delete(0, END)
            crm_rifle_make.insert(0, rifle["make"])
            crm_rifle_model.delete(0, END)
            crm_rifle_model.insert(0, rifle["model"])
            crm_rifle_cal.delete(0, END)
            crm_rifle_cal.insert(0, rifle["caliber"])
            crm_rifle_chassis.delete(0, END)
            crm_rifle_chassis.insert(0, rifle["chassis"])
            crm_rifle_trigger.delete(0, END)
            crm_rifle_trigger.insert(0, rifle["trigger"])
            crm_rifle_break.delete(0, END)
            crm_rifle_break.insert(0, rifle["break"])
            crm_rifle_supressor.delete(0, END)
            crm_rifle_supressor.insert(0, rifle["supressor"])
            crm_rifle_weight.delete(0, END)
            crm_rifle_weight.insert(0, rifle["weight"])
            crm_rifle_bipod.delete(0, END)
            crm_rifle_bipod.insert(0, rifle["bipod"])
            crm_rifle_software.delete(0, END)
            crm_rifle_software.insert(0, rifle["software"])

            # Scope
            crm_scope_make.delete(0, END)
            crm_scope_make.insert(0, scope["make"])
            crm_scope_model.delete(0, END)
            crm_scope_model.insert(0, scope["model"])
            crm_scope_rings.delete(0, END)
            crm_scope_rings.insert(0, scope["rings"])
            crm_scope_moa_rise.delete(0, END)
            crm_scope_moa_rise.insert(0, scope["moa_rise"])

            # Cartridge
            crm_cartridge_brass_make.delete(0, END)
            crm_cartridge_brass_make.insert(0, cartridge["brass_make"])
            crm_cartridge_bullet_make.delete(0, END)
            crm_cartridge_bullet_make.insert(0, cartridge["bullet_make"])
            crm_cartridge_bullet_model.delete(0, END)
            crm_cartridge_bullet_model.insert(0, cartridge["bullet_model"])
            crm_cartridge_bullet_weight.delete(0, END)
            crm_cartridge_bullet_weight.insert(0, cartridge["bullet_weight"])
            crm_cartridge_primer_make.delete(0, END)
            crm_cartridge_primer_make.insert(0, cartridge["primer_make"])
            crm_cartridge_primer_model.delete(0, END)
            crm_cartridge_primer_model.insert(0, cartridge["primer_model"])
            crm_cartridge_powder_make.delete(0, END)
            crm_cartridge_powder_make.insert(0, cartridge["powder_make"])
            crm_cartridge_powder_model.delete(0, END)
            crm_cartridge_powder_model.insert(0, cartridge["powder_model"])

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.load_edit_field_with_row_data Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        if _mode == 'edit':
            load_edit_field_with_row_data(json_record)

        def process_request(command_type, guid_value, first_name, last_name, id_number, cell_phone, email, team, spotter, equipment, scores):
            global dirty
            dirty = True

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.process_request Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            if command_type == "_UPDATE_":
                row = find_row_in_my_shooter_list(guid_value)
                if row >= 0:
                    dict = {"id":           guid_value,
                            "first_name":   first_name,
                            "last_name":    last_name,
                            "id_number":    id_number,
                            "cell_phone":   cell_phone,
                            "email":        email,
                            "team":         team,
                            "spotter":      spotter,
                            "equipment":    equipment,
                            "scores":       scores
                            }

                    settings.my_shooter_list[row] = dict

                if debuglevel >= 2:
                    my_logger.info('{time}, shooters.load_all_shooters.process_request _UPDATE_'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))

            elif command_type == "_INSERT_":
                dict = {"id":           guid_value,
                        "first_name":   first_name,
                        "last_name":    last_name,
                        "id_number":    id_number,
                        "cell_phone":   cell_phone,
                        "email":        email,
                        "team":         team,
                        "spotter":      spotter,
                        "equipment":    equipment,
                        "scores":       scores
                        }

                settings.my_shooter_list.append(dict)

                if debuglevel >= 2:
                    my_logger.info('{time}, shooters.load_all_shooters.process_request _INSERT_'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))

            elif command_type == "_DELETE_":
                row = find_row_in_my_shooter_list(guid_value)
                if row >= 0:
                    del settings.my_shooter_list[row]

                if debuglevel >= 2:
                    my_logger.info('{time}, shooters.load_all_shooters.process_request _DELETE_'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))

            settings.save_json_to_file(settings.filename)
            clear_all_fields()

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.process_request Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end process_request

        def find_row_in_my_shooter_list(guid_value):

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.find_row_in_my_shooter_list Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            row = 0
            found = False

            for rec in settings.my_shooter_list:
                if rec["id"] == guid_value:
                    found = True
                    break
                row = row + 1

            if (found == True):
                return (row)

            return (-1)

        #end find_row_in_my_shooter_list


        def determineAction():

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.determineAction Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            if load_form == False:
                if _mode == "edit":
                    update_entry()
                else:
                    add_entry()

            reload_main_form()
            child.grab_release()
            child.destroy()
            child.update()

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.determineAction Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end determineAction


        def clear_all_fields():

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.clear_all_fields Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            crm_shooter_fn.delete(0, END)
            crm_shooter_ln.delete(0, END)
            crm_shooter_id_number.delete(0, END)
            crm_shooter_cellphone.delete(0, END)
            crm_shooter_email.delete(0, END)
            crm_shooter_team.delete(0, END)
            crm_shooter_spotter.delete(0, END)
            # Equipment

            crm_shooter_id.configure(text="")       # UUID
            crm_shooter_fn.focus_set()
            id_value.set(uuid.uuid4())
            change_background_color("#FFFFFF")

            if debuglevel >= 2:
                my_logger.info('{time}, shooters.load_all_shooters.clear_all_fields Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end clear_all_fields

        if debuglevel >= 2:
            my_logger.info('{time}, shooters.load_all_shooters.open_popup Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end open_popup

    trv.bind("<ButtonRelease>", MouseButtonUpCallBack)
    load_shooter_json_from_file(settings.filename)
    load_trv_with_json()

    if debuglevel >= 1:
        my_logger.info('{time}, shooters.load_all_shooters Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_shooters
