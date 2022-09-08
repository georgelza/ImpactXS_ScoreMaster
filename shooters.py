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
from api.apputils import *

import uuid
import json

import settings

my_logger       = settings.my_logger
debuglevel      = settings.debuglevel


def load_json_from_file(myfile):

    if debuglevel >= 1:
        my_logger.info('{time}, load_json_from_file Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    with open(myfile, "r") as file_handler:
        settings.my_event_list = json.load(file_handler)
        settings.my_shooter_list = settings.my_event_list["shooters"]

    file_handler.close

    if debuglevel >= 1:
        my_logger.info('{time}, load_json_from_file.file has been read and closed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_json_from_file


# We will add the scores via the File/scores menu.
# For now ust build Scott's Treeview and user editor, then replace with my data.
def load_shooters(main_window):

    global trv

    if debuglevel >= 1:
        my_logger.info('{time}, load_shooters Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    child = Toplevel(main_window)
    child.geometry("1200x700")
    child.title = "Events"

    # Determine where we running, as template and events are by default subdirectories of the App directory.
    directory = os.getcwd()

    if debuglevel >= 1:
        my_logger.info('{time}, load_shooters.Current App Directory {directory}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            directory=directory
        ))

    def make_new_record():

        if debuglevel >= 2:
            my_logger.info('{time}, load_shooters.make_new_record Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        #rifleTuple = ('','','','','','','')
        #scopeTuple = ('','','','')
        #cartridgeTuple = ('','','','','','')
        #equipmentTuple = (rifleTuple, scopeTuple, cartridgeTuple)
        #blankTuple = ('', '', '', '', '', '', '', '', equipmentTuple)
        blankTuple = ('', '', '', '', '', '', '', '','','')
        open_popup('add', blankTuple, child)

    #end make_new_record

    btnNewRecord = Button(child, text="Add New", bg="#34d2eb",
                          padx=2, pady=3, command=lambda: make_new_record())
    btnNewRecord.grid(row=0, column=0, sticky="w")

    trv = ttk.Treeview(child, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="16")
    trv.grid(row=1, column=0, rowspan=16, columnspan=8)

    trv.heading(1, text="Action", anchor="w")
    trv.heading(2, text="ID", anchor="center")
    trv.heading(3, text="First Name", anchor="center")
    trv.heading(4, text="Last Name", anchor="center")
    trv.heading(5, text="ID Number", anchor="center")
    trv.heading(6, text="Cell Phone", anchor="center")
    trv.heading(7, text="eMail", anchor="center")
    trv.heading(8, text="Spotter", anchor="center")
    # Equipment
    # ... How to display ?

    trv.column("#1", anchor="w", width=100, stretch=True)
    trv.column("#2", anchor="w", width=270, stretch=True)
    trv.column("#3", anchor="w", width=140, stretch=False)
    trv.column("#4", anchor="w", width=140, stretch=False)
    trv.column("#5", anchor="w", width=140, stretch=False)
    trv.column("#6", anchor="w", width=140, stretch=False)
    trv.column("#7", anchor="w", width=140, stretch=False)
    trv.column("#8", anchor="w", width=140, stretch=False)
    # Equipment
    # ... How ?


    def remove_all_data_from_trv():

        if debuglevel >= 2:
            my_logger.info('{time}, load_shooters.remove_all_data_from_trv Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        for item in trv.get_children():
            trv.delete(item)

        if debuglevel >= 2:
            my_logger.info('{time}, load_shooters.remove_all_data_from_trv Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # Reload trv with all shooters data

    def load_trv_with_json():

        if debuglevel >= 2:
            my_logger.info('{time}, load_shooters.load_trv_with_json Called'.format(
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
            spotter     = key["spotter"]

            trv.insert('', index='end', iid=rowIndex, text="",
                       values=('edit', guid_value, first_name, last_name, id_number, cell_phone, email, spotter))
            rowIndex = rowIndex + 1

        if debuglevel >= 2:
            my_logger.info('{time}, load_shooters.load_trv_with_json Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end load_trv_with_json

    def MouseButtonUpCallBack(event):
        global trv

        if debuglevel >= 2:
            my_logger.info('{time}, load_shooters.MouseButtonUpCallBack Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        currentRowIndex = trv.selection()[0]
        lastTuple = (trv.item(currentRowIndex, 'values'))
        open_popup('edit', lastTuple, child)

        if debuglevel >= 2:
            my_logger.info('{time}, load_shooters.MouseButtonUpCallBack Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end MouseButtonUpCallBack

    def open_popup(_mode, _tuple, primary):

        if debuglevel >= 2:
            my_logger.info('{time}, load_shooters.open_popup Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        child = Toplevel(primary)
        child.geometry("1200x800")
        child.title('Shooter Maintenance')
        child.grab_set()  # allow it to receive events
        # and prevent users from interacting
        # with the main window

        child.configure(bg='LightBlue')
        load_form = True
        input_frame = LabelFrame(child, text='Enter New Record',bg="lightgray",font=('Consolas', 14))

        input_frame.grid(row=0, rowspan=12, column=0)

        l1 = Label(input_frame, text="ID", width=25, height=2, anchor="w", relief="ridge", font=('Consolas', 14))
        l2 = Label(input_frame, text="First Name", width=25, height=2, anchor="w", relief="ridge",font=('Consolas', 14))
        l3 = Label(input_frame, text="Last Name", width=25, height=2, anchor="w", relief="ridge", font=('Consolas', 14))
        l4 = Label(input_frame, text="ID Number", width=25, height=2, anchor="w", relief="ridge",font=('Consolas', 14))
        l5 = Label(input_frame, text="Cell Phone", width=25, height=2, anchor="w", relief="ridge",font=('Consolas', 14))
        l6 = Label(input_frame, text="eMail", width=25, height=2, anchor="w", relief="ridge",font=('Consolas', 14))
        l7 = Label(input_frame, text="Spotter", width=25, height=2, anchor="w", relief="ridge",font=('Consolas', 14))

        l1.grid(row=0, column=0, padx=1, pady=0)
        l2.grid(row=1, column=0, padx=1, pady=0)
        l3.grid(row=2, column=0, padx=1, pady=0)
        l4.grid(row=3, column=0, padx=1, pady=0)
        l5.grid(row=4, column=0, padx=1, pady=0)
        l6.grid(row=5, column=0, padx=1, pady=0)
        l7.grid(row=6, column=0, padx=1, pady=0)

        id_value = StringVar()
        id_value.set(uuid.uuid4())

        crm_id = Label(input_frame, anchor="w", height=1,relief="ridge", textvariable=id_value, font=('Consolas', 14))
        crm_id.grid(row=0, column=1, padx=20)

        crm_fn = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
        crm_fn.grid(row=1, column=1)

        crm_ln = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
        crm_ln.grid(row=2, column=1)

        crm_id_number = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
        crm_id_number.grid(row=3, column=1)

        crm_cellphone = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
        crm_cellphone.grid(row=4, column=1)

        crm_email = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
        crm_email.grid(row=5, column=1)

        crm_spotter = Entry(input_frame, width=30, borderwidth=2, fg="black", font=('Consolas', 14))
        crm_spotter.grid(row=6, column=1)

        btnAdd = Button(input_frame, text="Save", padx=5, pady=10, command=lambda: determineAction())
        btnAdd.grid(row=11, column=0)

        btnDelete = Button(input_frame, text="Delete", padx=5, pady=10, command=lambda: delete_record())
        btnDelete.grid(row=11, column=3)

        btnCancel = Button(input_frame, text="Cancel", padx=5, pady=10, command=lambda: child_cancel())
        btnCancel.grid(row=11, column=4)

        load_form = False

        def delete_record():

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.delete_record Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            guid_value  = id_value.get()
            first_name  = crm_fn.get()
            last_name   = crm_ln.get()
            id_number   = crm_id_number.get()
            cell_phone  = crm_cellphone.get()
            email       = crm_email.get()
            spotter     = crm_spotter.get()

            process_request('_DELETE_', guid_value, first_name, last_name, id_number, cell_phone, email, spotter)
            reload_main_form()
            child.grab_release()
            child.destroy()
            child.update()

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.delete_record Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end delete_record

        def child_cancel():

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.child_cancel Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            child.grab_release()
            child.destroy()
            child.update()

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.child_cancel Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end child_cancel

        def reload_main_form():

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.reload_main_form Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            load_trv_with_json()

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.reload_main_form Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
        def change_background_color(new_color):

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.change_background_color Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            crm_fn.config(bg=new_color)
            crm_ln.config(bg=new_color)
            crm_id_number.config(bg=new_color)
            crm_cellphone.config(bg=new_color)
            crm_email.config(bg=new_color)
            crm_spotter.config(bg=new_color)

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.change_background_color Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end change_background_color

        def add_entry():

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.add_entry Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            guid_value  = id_value.get()
            first_name  = crm_fn.get()
            last_name   = crm_ln.get()
            id_number   = crm_id_number.get()
            cell_phone  = crm_cellphone.get()
            email       = crm_email.get()
            spotter     = crm_spotter.get()
            # equipment
            rifle = {
                "make":     "",
                "model":    "",
                "caliber":  "",
                "chassis":  "",
                "trigger":  "",
                "break":    "",
                "supressor":""
            }
            scope = {
                "make":             "",
                "model":            "",
                "rings":            "",
                "picatinny_raise":  ""
            }
            cartridge = {
                "brass_make":       "",
                "bullet_make":      "",
                "bullet_model":     "",
                "bullet_weight":    "",
                "primer_make":      "",
                "primer_model":     ""
            }
            equipment = {
                "rifle":        rifle,
                "scope":        scope,
                "cartridge":    cartridge
            }
            # scores
            scores   = {
                "qualify" : "",
                "final" :   ""
            }

            if len(first_name) == 0:
                change_background_color("#FFB2AE")
                return

            process_request('_INSERT_', guid_value, first_name, last_name, id_number, cell_phone, email, spotter, equipment, scores)

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.add_entry Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end add_entry

        def update_entry():

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.update_entry Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            guid_value  = id_value.get()
            first_name  = crm_fn.get()
            last_name   = crm_ln.get()
            id_number   = crm_id_number.get()
            cell_phone  = crm_cellphone.get()
            email       = crm_email.get()
            spotter     = crm_spotter.get()
            # equipment
            rifle = {
                "make":         "",
                "model":        "",
                "caliber":      "",
                "chassis":      "",
                "trigger":      "",
                "break":        "",
                "supressor":    ""
            }
            scope = {
                "make":             "",
                "model":            "",
                "rings":            "",
                "picatinny_raise":  ""
            }
            cartridge = {
                "brass_make":       "",
                "bullet_make":      "",
                "bullet_model":     "",
                "bullet_weight":    "",
                "primer_make":      "",
                "primer_model":     ""
            }
            equipment = {
                "rifle":        rifle,
                "scope":        scope,
                "cartridge":    cartridge
            }
            # scores
            scores   = {
                "qualify":  "",
                "final":    ""
            }

            if len(first_name) == 0:
                change_background_color("#FFB2AE")
                return

            process_request('_UPDATE_', guid_value, first_name, last_name, id_number, cell_phone, email, spotter, equipment, scores)

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.update_entry Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end update_entry

        def load_edit_field_with_row_data(_tuple):

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.load_edit_field_with_row_data Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            if len(_tuple) == 0:
                return

            id_value.set(_tuple[1])
            crm_fn.delete(0, END)
            crm_fn.insert(0, _tuple[2])
            crm_ln.delete(0, END)
            crm_ln.insert(0, _tuple[3])
            crm_id_number.delete(0, END)
            crm_id_number.insert(0, _tuple[4])
            crm_cellphone.delete(0, END)
            crm_cellphone.insert(0, _tuple[5])
            crm_email.delete(0, END)
            crm_email.insert(0, _tuple[6])
            crm_spotter.delete(0, END)
            crm_spotter.insert(0, _tuple[7])

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.load_edit_field_with_row_data Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        if _mode == 'edit':
            load_edit_field_with_row_data(_tuple)

        def process_request(command_type, guid_value, first_name, last_name, id_number, cell_phone, email, spotter, equipment, scores):
            global dirty
            dirty = True

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.process_request Called'.format(
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
                            "spotter":      spotter,
                            "equipment":    equipment,
                            "scores":       scores
                            }

                    settings.my_shooter_list[row] = dict

                if debuglevel >= 2:
                    my_logger.info('{time}, load_shooters.process_request _UPDATE_'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))

            elif command_type == "_INSERT_":
                dict = {"id":           guid_value,
                        "first_name":   first_name,
                        "last_name":    last_name,
                        "id_number":    id_number,
                        "cell_phone":   cell_phone,
                        "email":        email,
                        "spotter":      spotter,
                        "equipment":    equipment,
                        "scores":       scores
                        }

                settings.my_shooter_list.append(dict)

                if debuglevel >= 2:
                    my_logger.info('{time}, load_shooters.process_request _INSERT_'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))

            elif command_type == "_DELETE_":
                row = find_row_in_my_shooter_list(guid_value)
                if row >= 0:
                    del settings.my_shooter_list[row]

                if debuglevel >= 2:
                    my_logger.info('{time}, load_shooters.process_request _DELETE_'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))

            save_json_to_file(settings.filename)
            clear_all_fields()

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.process_request Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end process_request

        def find_row_in_my_shooter_list(guid_value):

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.find_row_in_my_shooter_list Called'.format(
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
                my_logger.info('{time}, load_shooters.determineAction Called'.format(
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
                my_logger.info('{time}, load_shooters.determineAction Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end determineAction

        def save_json_to_file(myfile):

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.save_json_to_file Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            with open(myfile, "w") as file_handler:
                settings.my_event_list["shooters"] = settings.my_shooter_list
                json.dump(settings.my_event_list, file_handler, indent=4)

            file_handler.close

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.save_json_to_file.file has been written to and closed '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end save_json_to_file

        def clear_all_fields():

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.clear_all_fields Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            crm_fn.delete(0, END)
            crm_ln.delete(0, END)
            crm_id_number.delete(0, END)
            crm_cellphone.delete(0, END)
            crm_email.delete(0, END)
            crm_spotter.delete(0, END)
            # Equipment

            crm_id.configure(text="")
            crm_fn.focus_set()
            id_value.set(uuid.uuid4())
            change_background_color("#FFFFFF")

            if debuglevel >= 2:
                my_logger.info('{time}, load_shooters.clear_all_fields Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end clear_all_fields

        if debuglevel >= 2:
            my_logger.info('{time}, load_shooters.open_popup Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end open_popup

    trv.bind("<ButtonRelease>", MouseButtonUpCallBack)
    load_json_from_file(settings.filename)
    load_trv_with_json()

    if debuglevel >= 1:
        my_logger.info('{time}, load_shooters Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_shooters


def load_scores(main_window):

    if debuglevel >= 1:
        my_logger.info('{time}, load_scores Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # ...

    if debuglevel >= 1:
        my_logger.info('{time}, load_scores Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_scores