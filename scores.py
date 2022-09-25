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

    if debuglevel >= 1:
        my_logger.info('{time}, scores.load_shooter_scores_json_from_file my_shooter_list '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))
        settings.pp_json(settings.my_shooter_list)

    if debuglevel >= 1:
        my_logger.info('{time}, scores.load_shooter_scores_json_from_file.file has been read and closed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_shooter_scores_json_from_file


def find_rec_in_my_shooter_list(guid_value):

    if debuglevel >= 2:
        my_logger.info('{time}, scores.find_rec_in_my_shooter_list Called'.format(
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
def load_all_shooters_scores(main_window):

    global trv_shooter_scores
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

    trv_shooter_scores = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="20")
    trv_shooter_scores.grid(row=0, column=0, rowspan=20, columnspan=6, sticky=E+W)

    trv_shooter_scores.heading(1, text="Place",        anchor="w")
    trv_shooter_scores.heading(2, text="",             anchor="center")
    trv_shooter_scores.heading(3, text="Shooter",      anchor="center")
    trv_shooter_scores.heading(4, text="Spotter",      anchor="center")
    trv_shooter_scores.heading(5, text="Caliber",      anchor="center")
    trv_shooter_scores.heading(6, text="Qualifying",   anchor="center")
    trv_shooter_scores.heading(7, text="Finals",       anchor="center")

    trv_shooter_scores.column("#1", anchor="w", width=50, stretch=True)
    trv_shooter_scores.column("#2", anchor="w", width=1, stretch=True)
    trv_shooter_scores.column("#3", anchor="w", width=259, stretch=True)
    trv_shooter_scores.column("#4", anchor="w", width=250, stretch=True)
    trv_shooter_scores.column("#5", anchor="w", width=200, stretch=False)
    trv_shooter_scores.column("#6", anchor="w", width=113, stretch=False)
    trv_shooter_scores.column("#7", anchor="w", width=113, stretch=False)


    # Read the Image
    image = Image.open("images/impactxs.png")
    # Resize the image using resize() method
    resize_impactxs = image.resize((930, 150))
    img2 = ImageTk.PhotoImage(resize_impactxs)
    # create label and add resize image
    label2 = Label(footer_frame, image=img2)
    label2.image = img2
    label2.grid(row=0, column=0, padx=5, pady=5)

    def load_all_schooter_scores_trv_shooter_scores_with_json():

        for item in trv_shooter_scores.get_children():
            trv_shooter_scores.delete(item)

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters_scores.load_all_schooter_scores_trv_shooter_scores_with_json Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        rowIndex = 1

        for key in settings.my_shooter_list:

            equipment           = key["equipment"]                          # Structure with equipment
            rifle               = equipment['rifle']                        # sub structure with rifle information
            scores              = key["scores"]                             # structure with scores

            trv_shooter_scores.insert('', index='end', iid=rowIndex, text="",
                       values=(rowIndex,
                               key["id"],
                               key["first_name"].strip() + " " + key["last_name"].strip(),
                               key["spotter"],
                               rifle["caliber"],
                               scores['qualifying_score'],
                               scores['final_score']))

            rowIndex = rowIndex + 1

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters_scores.load_all_schooter_scores_trv_shooter_scores_with_json Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end load_all_schooter_scores_trv_shooter_scores_with_json

    load_all_schooter_scores_trv_shooter_scores_with_json()


    def MouseButtonUpCallBack(event):
        global trv_shooter_scores

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters_scores.MouseButtonUpCallBack Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        currentRowIndex = trv_shooter_scores.selection()[0]

        my_logger.info('{time}, scores.load_all_shooters_scores.MouseButtonUpCallBack Called Cur Row Index: {currentRowIndex}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            currentRowIndex=currentRowIndex
        ))

        lastTuple = (trv_shooter_scores.item(currentRowIndex, 'values'))
        # Get from my_shooter_list dictionary the entire record matching the lastTuple[1], this is the id column
        my_jsonrec = find_rec_in_my_shooter_list(lastTuple[1])
        # Lets edit/enter scores for selected shooter
        open_popup('edit', my_jsonrec, tree_frame)

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters.MouseButtonUpCallBack Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end MouseButtonUpCallBack


    # Lets design/pain the popup, this is what is opened when the user clicks on a shooter in the treeview.
    def open_popup(_mode, json_record, primary):

        # json_record is the entire record of the current shooter, lets get the scores only
        all_scores          = json_record["scores"]
        qualifying_scores   = all_scores["qualifying"]
        finals_scores       = all_scores["finals"]

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters.open_popup Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

            my_logger.info('{time}, scores.load_all_shooters.open_popup Current Shooter'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))
            settings.pp_json(json_record)

        child = Toplevel(primary)
        child.title('Shooter Score Maintenance')
        child.geometry("1100x825")
        child.configure(bg=frame_bg)
        child.grab_set()  # allow it to receive events

        load_form = True

        shooter_frame               = Frame(child)
        qualifications_score_frame  = Frame(child)
        finals_score_frame          = Frame(child)

        cntrls_frame    = Frame(child)

        # Frame Layout
        shooter_lbframe = LabelFrame(shooter_frame, text='Shooter Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        shooter_lbframe.grid()
        shooter_frame.grid(row=0, rowspan=10, column=0, columnspan=4, sticky="W", pady=(1, 5))

        # Qualifications frame to hold the Qual scores
        qual_scores_lbframe = LabelFrame(qualifications_score_frame, text='Qualifications Scores', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        qual_scores_lbframe.grid()
        qualifications_score_frame.grid(row=0, rowspan=10, column=0, columnspan=4, sticky="W", pady=(1, 5))

        # Finals frame to hold the Final scores
        finals_scores_lbframe = LabelFrame(finals_score_frame, text='Finals Scores', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        finals_scores_lbframe.grid()
        finals_score_frame.grid(row=0, rowspan=10, column=0, columnspan=4, sticky="W", pady=(1, 5))

        # Frame Layout : Buttons
        cntrls_lbframe = LabelFrame(cntrls_frame, bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size), relief=RIDGE)
        cntrls_lbframe.grid()
        cntrls_frame.grid(row=22, rowspan=4, column=0, columnspan=8, sticky="W", pady=(5, 0))

        # Shooter
        lb_shooter1 = Label(shooter_lbframe, text="",               width=2, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter2 = Label(shooter_lbframe, text="First Name",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter3 = Label(shooter_lbframe, text="Last Name",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter4 = Label(shooter_lbframe, text="Spotter",       width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

        lb_shooter1.grid(row=1, column=0, padx=5, pady=0)
        lb_shooter2.grid(row=2, column=0, padx=5, pady=0)
        lb_shooter3.grid(row=3, column=0, padx=5, pady=0)
        lb_shooter4.grid(row=4, column=0, padx=5, pady=0)

        id_value = StringVar()
        id_value.set(uuid.uuid4())

        # Shooter
        crm_shooter_id = Label(shooter_lbframe, anchor="w", height=1, relief="ridge", textvariable=id_value, font=(txtfont, txtfont_size))
        crm_shooter_id.grid(row=1, column=1, padx=20)

        crm_shooter_fn = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_fn.grid(row=2, column=1)

        crm_shooter_ln = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_ln.grid(row=3, column=1)

        crm_shooter_spotter = Entry(shooter_lbframe, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_spotter.grid(row=8, column=1)

        # Qualifications
        crm_qualification_score = Label(qualifications_score_frame, anchor="w", height=1, relief="ridge", textvariable=id_value, font=(txtfont, txtfont_size))
        crm_qualification_score.grid(row=1, column=1, padx=20)

        # Finals
        crm_final_score = Label(finals_score_frame, anchor="w", height=1, relief="ridge", textvariable=id_value, font=(txtfont, txtfont_size))
        crm_final_score.grid(row=1, column=1, padx=20)

        # button
        btnSave = Button(cntrls_lbframe, text="Save", padx=5, pady=10, command=lambda: determineAction())
        btnSave.grid(row=0, column=0)

        btnCancel = Button(cntrls_lbframe, text="Cancel", padx=5, pady=10, command=lambda: child_cancel())
        btnCancel.grid(row=0, column=1)

        load_form = False

        def child_cancel():

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.child_cancel Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            child.grab_release()
            child.destroy()
            child.update()

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.child_cancel Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        # end child_cancel

        def reload_main_form():

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.reload_main_form Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            load_all_schooter_scores_trv_shooter_scores_with_json()

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.reload_main_form Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        # end reload_main_form

        def change_background_color(new_color):

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.change_background_color Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            # Shooter
            crm_shooter_fn.config(bg=new_color)
            crm_shooter_ln.config(bg=new_color)
            crm_shooter_spotter.config(bg=new_color)

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.change_background_color Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end change_background_color


        def update_entry():


            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.update_entry Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            # shooter



            process_request('_UPDATE_', json_record, {})

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.update_entry Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end update_entry


        def process_request(command_type, json_record, scores):
            global dirty
            dirty = True

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.process_request Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            if command_type == "_UPDATE_":
                guid_value  = json_record["id"]
                row         = find_row_in_my_shooter_list(guid_value)
                if row >= 0:

                    json_record["scores"] = scores

                    settings.my_shooter_list[row] = json_record

                if debuglevel >= 2:
                    my_logger.info('{time}, shooters.load_all_shooters.process_request _UPDATE_'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))


            settings.save_json_to_file(settings.filename)
            clear_all_fields()

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.process_request Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end process_request


        def find_row_in_my_shooter_list(guid_value):

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.find_row_in_my_shooter_list Called'.format(
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
                my_logger.info('{time}, scores.load_all_shooters.determineAction Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            if load_form == False:
                if _mode == "edit":
                    update_entry()

            reload_main_form()
            child.grab_release()
            child.destroy()
            child.update()

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.determineAction Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end determineAction


        def clear_all_fields():

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.clear_all_fields Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            crm_shooter_id.configure(text="")       # UUID
            crm_shooter_fn.focus_set()
            id_value.set(uuid.uuid4())
            change_background_color("#FFFFFF")

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters.clear_all_fields Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        #end clear_all_fields


        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters.open_popup Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end open_popup


    if debuglevel >= 2:
        my_logger.info('{time}, scores.load_all_shooters_scores Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_shooters_scores
