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
__author__  = "George Leonard"
__email__   = "georgelza@gmail.com"
__version__ = "0.0.1"

from tkinter import *

from datetime import datetime
from tkcalendar import DateEntry

import json
import os

import settings

my_logger       = settings.my_logger
debuglevel      = settings.debuglevel
echojson        = settings.echojson

def open_event_screen(root):

    my_event            = settings.my_event_list
    my_qualify          = settings.my_qualifying_target_list
    my_finals           = settings.my_finals_target_list
    my_shooters         = settings.my_shooter_list
    my_event_image      = settings.my_event_image

    # color'ing
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


    def make_new_quals_record():

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.make_new_quals_record.Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        # Add record to json
        my_qualifying_target_list = settings.my_qualifying_target_list["target_list"]
        my_qualifying_target_list.append({"target_no": len(my_qualifying_target_list),
                                "qb": 0,
                                "distance": 0,
                                "target_size": ""})
        settings.my_qualifying_target_list["target_list"]      = my_qualifying_target_list
        settings.my_qualifying_target_list["no_of_targets"]    = str(len(my_qualifying_target_list))

        crm_q_targets.delete(0, END)
        crm_q_targets.insert(0, settings.my_qualifying_target_list["no_of_targets"])

        # reload treeview
        load_trv_with_json(trv_qual, "quals")

    # end make_new_quals_record

    # Delete Row to Treeview
    def remove_quals_record():

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.remove_quals_record.Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        # Remove item from treeview
        selected_item = trv_qual.selection()[0]  ## get selected item
        trv_qual.delete(selected_item)

        # dumb treeview to json
        my_qualifying_target_list = create_json_from_treeview(trv_qual, "quals")

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.remove_quals_record Update Qualifying Target List'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

            if echojson == 1:
                settings.pp_json(my_qualifying_target_list)

        # Update settings:
        settings.my_qualifying_target_list["target_list"]      = my_qualifying_target_list
        settings.my_qualifying_target_list["no_of_targets"]    = str(len(my_qualifying_target_list))

        crm_q_targets.delete(0, END)
        crm_q_targets.insert(0, settings.my_qualifying_target_list["no_of_targets"])

        # reload treeview
        load_trv_with_json(trv_qual, "quals")

    # end remove_quals_record

    # Add Row to Treeview
    def make_new_finals_record():

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.make_new_finals_record.Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        # Add record to json
        my_finals_target_list = settings.my_finals_target_list["target_list"]
        my_finals_target_list.append({"target_no": len(my_finals_target_list),
                                        "distance": 0,
                                        "target_size": ""})
        settings.my_finals_target_list["target_list"]      = my_finals_target_list
        settings.my_finals_target_list["no_of_targets"]    = str(len(my_finals_target_list))

        crm_f_targets.delete(0, END)
        crm_f_targets.insert(0, settings.my_finals_target_list["no_of_targets"])

        # reload treeview
        load_trv_with_json(trv_finals, "finals")

    # end make_new_finals_record

    # Delete Row to Treeview
    def remove_finals_record():

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.remove_finals_record.Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

            # Remove item from treeview
            selected_item = trv_finals.selection()[0]  ## get selected item
            trv_finals.delete(selected_item)

            # dumb treeview to json
            my_finals_target_list = create_json_from_treeview(trv_finals, "finals")

            if debuglevel >= 2:
                my_logger.info('{time}, event.open_event_screen.remove_finals_record Update Finals Target List'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

                if echojson == 1:
                    settings.pp_json(my_finals_target_list)

            # Update settings:
            settings.my_finals_target_list["target_list"]   = my_finals_target_list
            settings.my_finals_target_list["no_of_targets"] = str(len(my_finals_target_list))

            crm_f_targets.delete(0, END)
            crm_f_targets.insert(0, settings.my_finals_target_list["no_of_targets"])

    # end remove_finals_record


    # Populate Qualify Treeview
    def load_trv_with_json(treeview, mode):

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.load_trv_with_json.Called Mode: ({mode})'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                mode=mode
            ))

            if echojson == 1:
                if mode == "quals":
                    settings.pp_json(settings.my_qualifying_target_list)
                else:
                    settings.pp_json(settings.my_finals_target_list)

        rowIndex = 1
        if mode == "quals":
            # Clean out current painted treeview
            for item in treeview.get_children():
                trv_qual.delete(item)

            for key in my_qualify["target_list"]:
                target_no   = key["target_no"]
                qb          = key["qb"]
                distance    = key["distance"]
                target_size = key["target_size"]

                trv_qual.insert('', index='end', iid=rowIndex, text="", values=(target_no, qb, distance, target_size))
                rowIndex = rowIndex + 1

        else:
            # Clean out current painted treeview
            for item in treeview.get_children():
                trv_finals.delete(item)

            for key in my_finals["target_list"]:
                target_no   = key["target_no"]
                distance    = key["distance"]
                target_size = key["target_size"]

                trv_finals.insert('', index='end', iid=rowIndex, text="", values=(target_no, distance, target_size))
                rowIndex = rowIndex + 1


        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.load_trv_with_json.Completed Mode: ({mode})'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                mode=mode
            ))

    # end load_trv_with_json


    def cancel_Event_Update():

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.cancel_Event_Update.Called '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        # Reload screen from current Saved state.
        # For now we just exit....
        child.destroy()

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.cancel_Event_Update.Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end cancel_Event_Update

    def Exit_Event():

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.Exit_Event.Called '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        child.destroy()

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.Exit_Event.Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end Exit_Event


    def create_json_from_treeview(treeview, mode):

        json_record = []

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.create_json_from_treeview.Called Mode: ({mode})'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                mode=mode
            ))

        if mode == "quals":
            for line in treeview.get_children():
                values = treeview.item(line)['values']
                json_record.append({"target_no":    values[0],
                                    "qb":           values[1],
                                    "distance":     values[2],
                                    "target_size":  values[3]})

        else:
            for line in treeview.get_children():
                values = treeview.item(line)['values']
                json_record.append({"target_no":    values[0],
                                    "distance":     values[1],
                                    "target_size":  values[2]})

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.create_json_from_treeview.Completed Mode: ({mode})'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                mode=mode
            ))
        return json_record

    # end create_json_from_treeview


    # Save event data to file
    def save_Main_Event_json_data_to_file():

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.save_Main_Event_json_data_to_file.Called '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        # Save data to my_event_list
        my_event = {
            "name":         crm_eventname.get(),
            "location":     crm_Location.get(),
            "start_date":   crm_Start_Date.get(),
            "end_date":     crm_End_Date.get(),
            "distance":     crm_Distance.get(),
            "image":        settings.my_event_image
        }

        # Retrieve the data from the treeview
        m_qual_targets = create_json_from_treeview(trv_qual, "quals")

        # Build Qualifying json record
        my_qualifying = {
            "no_of_targets":    crm_q_targets.get(),
            "no_of_shots":      crm_q_shots.get(),
            "time_limit":       crm_q_time_limit.get(),
            "target_list":      m_qual_targets
        }

        # Retrieve the data from the treeview
        m_finals_targets = create_json_from_treeview(trv_finals, "finals")

        # Build Finals json record
        my_final = {
            "no_of_targets":    crm_f_targets.get(),
            "no_of_shots":      crm_f_shots.get(),
            "time_limit":       crm_q_time_limit.get(),
            "target_list":      m_finals_targets
        }

        # Save - Main Event structures
        settings.my_event_list              = my_event
        settings.my_qualifying_target_list  = my_qualifying
        settings.my_finals_target_list      = my_final
        settings.my_shooter_list            = my_shooters

        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.save_Main_Event_json_data_to_file Writing JSON to event file '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

            if echojson == 1:
                my_logger.info('{time}, event.open_event_screen.save_Main_Event_json_data_to_file Event Information '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
                settings.pp_json(my_event)

                my_logger.info('{time}, event.open_event_screen.save_Main_Event_json_data_to_file Qualifying Information '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
                settings.pp_json(my_qualifying)

                my_logger.info('{time}, event.open_event_screen.save_Main_Event_json_data_to_file Finals Information '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
                settings.pp_json(my_final)

        settings.save_event(settings.filename)

        # cleanup
        child.destroy()


        if debuglevel >= 2:
            my_logger.info('{time}, event.open_event_screen.save_Main_Event_json_data_to_file.Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end save_Main_Event_json_data_to_file


    ###################################################################################################
    # Ok Lets Start
    ###################################################################################################

    if debuglevel >= 1:
        my_logger.info('{time}, event.open_event_screen.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    child = Toplevel(root)
    child.title = "Events Maintenance"
    child.geometry("825x675")
    child.configure(bg=frame_bg)

    # Disable Resize
    child.resizable(False, False)

    load_form = True

    input_frame     = Frame(child, bg="lightgray", relief=GROOVE)
    score_frame     = Frame(child, bg="lightgray", relief=GROOVE)
    crtls_frame     = Frame(child, bg="lightgray", relief=GROOVE)

    input_frame.grid(row=0, column=0, sticky="W", pady=(1, 5))
    score_frame.grid(row=1, column=0, sticky="W", pady=(1, 5))
    crtls_frame.grid(row=2, column=0, sticky="NS", pady=(5, 0))

    # Main Event Frame Layout
    input_lbframe = LabelFrame(input_frame, text='Event Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
    input_lbframe.grid(row=0, column=0,  sticky="W", padx=(0, 5))

    # Qualifications Event Layout
    qual_lbframe = LabelFrame(score_frame, text='Qualifying Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
    qual_lbframe.grid(row=0, column=0,  sticky="W", padx=(0, 5))

    # Finals Event Layout
    final_lbframe = LabelFrame(score_frame, text='Final Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
    final_lbframe.grid(row=0, column=1, sticky="W", padx=(0, 5))

    # Controlling Buttons
    crtls_lbframe = LabelFrame(crtls_frame, bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
    crtls_lbframe.grid(row=0, column=0, sticky="NS", padx=(0, 5))


    # Main Event Frame Layout
    lb_crm_eventname    = Label(input_lbframe, text="Event Name",   width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_Location     = Label(input_lbframe, text="Location",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_Start_Date   = Label(input_lbframe, text="Start Date",   width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_End_Date     = Label(input_lbframe, text="End Date",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_Distance     = Label(input_lbframe, text="Distance",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))

    lb_crm_eventname.grid   (column=0, row=0, padx=1, pady=0)
    lb_crm_Location.grid    (column=0, row=1, padx=1, pady=0)
    lb_crm_Start_Date.grid  (column=0, row=2, padx=1, pady=0)
    lb_crm_End_Date.grid    (column=0, row=3, padx=1, pady=0)
    lb_crm_Distance.grid    (column=0, row=4, padx=1, pady=0)

    crm_eventname   = Entry(input_lbframe,      width=40, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
    crm_Location    = Entry(input_lbframe,      width=40, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))

    crm_Start_Date  = DateEntry(input_lbframe,  width=39, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size), date_pattern='dd/mm/yyyy', selectmode='day')
    crm_End_Date    = DateEntry(input_lbframe,  width=39, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size), date_pattern='dd/mm/yyyy', selectmode='day')
    crm_Distance    = Entry(input_lbframe,      width=40, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))

    crm_Start_Date._top_cal.overrideredirect(False)
    crm_End_Date._top_cal.overrideredirect(False)

    crm_eventname.grid  (column=1, row=0)
    crm_Location.grid   (column=1, row=1)
    crm_Start_Date.grid (column=1, row=2)
    crm_End_Date.grid   (column=1, row=3)
    crm_Distance.grid   (column=1, row=4)

    # Qualifications Event Layout
    lb_crm_q_targets    = Label(qual_lbframe, text="No Of Targets", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_q_shots      = Label(qual_lbframe, text="No of Shots",   width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_q_time_limit = Label(qual_lbframe, text="Time Limit",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))

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
    lb_crm_f_targets    = Label(final_lbframe, text="No of Targets",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_f_shots      = Label(final_lbframe, text="No of Shots",      width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
    lb_crm_f_time_limit = Label(final_lbframe, text="Time Limit",       width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))

    lb_crm_f_targets.grid(column=0, row=0, padx=1, pady=0)
    lb_crm_f_shots.grid(column=0, row=1, padx=1, pady=0)
    lb_crm_f_time_limit.grid(column=0, row=2, padx=1, pady=0)

    crm_f_targets       = Entry(final_lbframe, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
    crm_f_shots         = Entry(final_lbframe, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
    crm_f_time_limit    = Entry(final_lbframe, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))

    crm_f_targets.grid(column=2, row=0, padx=1, pady=0)
    crm_f_shots.grid(column=2, row=1, padx=1, pady=0)
    crm_f_time_limit.grid(column=2, row=2, padx=1, pady=0)


    # Lets add some Treeviews
    # Qualifications
    tree_qualframe  = Frame(qual_lbframe, bg=label_text_bg)
    tree_qualframe.grid(row=4, column=0, rowspan=5, columnspan=9)

    btnQualNewRecord = Button(tree_qualframe, text="Add", bg="#34d2eb", padx=2, pady=3, command=lambda: make_new_quals_record())
    btnQualNewRecord.grid(row=0, column=0, sticky="w")
    btnQualDelRecord = Button(tree_qualframe, text="Delete", bg="#34d2eb", padx=2, pady=3, command=lambda: remove_quals_record())
    btnQualDelRecord.grid(row=0, column=1, sticky="W")

    trv_qual = settings.TreeviewEdit(tree_qualframe, columns=(1, 2, 3, 4), show="headings", height="7")
    trv_qual.grid(row=1, column=0, rowspan=5, columnspan=9)

    trv_qual.heading(1, text="Target #",        anchor="w")
    trv_qual.heading(2, text="QB",              anchor="center")
    trv_qual.heading(3, text="Distance (yrds)", anchor="center")
    trv_qual.heading(4, text="Target Size",     anchor="center")
    trv_qual.column("#1", anchor="w", width=60, stretch=True)
    trv_qual.column("#2", anchor="w", width=100, stretch=True)
    trv_qual.column("#3", anchor="w", width=100, stretch=True)
    trv_qual.column("#4", anchor="w", width=100, stretch=True)

    tree_qualframe.grid(row=4, column=0)
    load_trv_with_json(trv_qual, "quals")


    # Finals shots
    tree_finalframe = Frame(final_lbframe, bg=label_text_bg)
    tree_finalframe.grid(row=4, column=0, rowspan=5, columnspan=9)

    btnFinalsNewRecord = Button(tree_finalframe, text="Add", bg="#34d2eb", padx=2, pady=3, command=lambda: make_new_finals_record())
    btnFinalsNewRecord.grid(row=0, column=0, sticky="w")
    btnFinalsDelRecord = Button(tree_finalframe, text="Delete", bg="#34d2eb", padx=2, pady=3, command=lambda: remove_finals_record())
    btnFinalsDelRecord.grid(row=0, column=1, sticky="W")

    trv_finals = settings.TreeviewEdit(tree_finalframe, columns=(1, 2, 3), show="headings", height="7")
    trv_finals.grid(row=1, column=0, rowspan=5, columnspan=9)
    # Make space for a "Add" and "Delete" button

    trv_finals.heading(1, text="Target #",          anchor="w")
    trv_finals.heading(2, text="Distance (yrds)",   anchor="center")
    trv_finals.heading(3, text="Target Size",       anchor="center")
    trv_finals.column("#1", anchor="w", width=60, stretch=True)
    trv_finals.column("#2", anchor="w", width=150, stretch=True)
    trv_finals.column("#3", anchor="w", width=150, stretch=True)

    tree_finalframe.grid(row=4, column=0)
    load_trv_with_json(trv_finals, "finals")


    # Main Event Common Data

    btnSave = Button(crtls_lbframe, text="Save", padx=5, pady=10, command=save_Main_Event_json_data_to_file)
    btnSave.grid(row=13, column=0)

#    btnCancel = Button(crtls_lbframe, text="Cancel", padx=5, pady=10, command=cancel_Event_Update)
#    btnCancel.grid(row=13, column=1)

    btnExit = Button(crtls_lbframe, text="Exit", padx=5, pady=10, command=Exit_Event)
    btnExit.grid(row=13, column=2)

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
    crm_q_targets.insert(0, my_qualify["no_of_targets"])
    crm_q_shots.delete(0, END)
    crm_q_shots.insert(0, my_qualify["no_of_shots"])
    crm_q_time_limit.delete(0, END)
    crm_q_time_limit.insert(0, my_qualify["time_limit"])
    # Now paint the Treeview

    # Finals Event
    crm_f_targets.delete(0, END)
    crm_f_targets.insert(0, my_finals["no_of_targets"])
    crm_f_shots.delete(0, END)
    crm_f_shots.insert(0, my_finals["no_of_shots"])
    crm_f_time_limit.delete(0, END)
    crm_f_time_limit.insert(0, my_finals["time_limit"])
    # Now paint the Treeview

    load_form = False

    # Add Treeview (and buttons Add/Edit/Delete) to define Qualifying and Final distances.

    if debuglevel >= 1:
        my_logger.info('{time}, event.open_event_screen.Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end open_event_screen


