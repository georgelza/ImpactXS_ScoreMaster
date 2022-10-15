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
echojson        = settings.echojson



# We will add the scores via the File/scores menu.
# For now ust build Scott's Treeview and user editor, then replace with my data.
def load_all_shooters_scores(main_window):

    global score_viewer
    global trv_all_shooter_scores
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

    score_viewer        = settings.score_viewer
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

    trv_all_shooter_scores = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="20")
    trv_all_shooter_scores.grid(row=0, column=0, rowspan=20, columnspan=6, sticky=E+W)

    trv_all_shooter_scores.heading(1, text="Place",        anchor="w")
    trv_all_shooter_scores.heading(2, text="",             anchor="center")
    trv_all_shooter_scores.heading(3, text="Shooter",      anchor="center")
    trv_all_shooter_scores.heading(4, text="Spotter",      anchor="center")
    trv_all_shooter_scores.heading(5, text="Caliber",      anchor="center")
    trv_all_shooter_scores.heading(6, text="Qualifying",   anchor="center")
    trv_all_shooter_scores.heading(7, text="Finals",       anchor="center")

    trv_all_shooter_scores.column("#1", anchor="w", width=50, stretch=True)
    trv_all_shooter_scores.column("#2", anchor="w", width=1, stretch=True)
    trv_all_shooter_scores.column("#3", anchor="w", width=259, stretch=True)
    trv_all_shooter_scores.column("#4", anchor="w", width=250, stretch=True)
    trv_all_shooter_scores.column("#5", anchor="w", width=200, stretch=False)
    trv_all_shooter_scores.column("#6", anchor="w", width=113, stretch=False)
    trv_all_shooter_scores.column("#7", anchor="w", width=113, stretch=False)


    # Read the Image
    image = Image.open("images/impactxs.png")
    # Resize the image using resize() method
    resize_impactxs = image.resize((930, 150))
    img2 = ImageTk.PhotoImage(resize_impactxs)
    # create label and add resize image
    label2 = Label(footer_frame, image=img2)
    label2.image = img2
    label2.grid(row=0, column=0, padx=5, pady=5)

    def load_all_shooter_scores_trv_with_json():

        for item in trv_all_shooter_scores.get_children():
            trv_all_shooter_scores.delete(item)

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters_scores.load_all_shooter_scores_trv_with_json Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        rowIndex = 1

        for key in settings.my_shooter_list:

            equipment   = key["equipment"]                          # Structure with equipment
            rifle       = equipment['rifle']                        # sub structure with rifle information
            scores      = key["scores"]                             # structure with scores

            trv_all_shooter_scores.insert('', index='end', iid=rowIndex, text="",
                                          values=(rowIndex,
                                                  key["id"],
                                                  key["first_name"].strip() + " " + key["last_name"].strip(),
                                                  key["spotter"],
                                                  rifle["caliber"],
                                                  scores['qualifying_score'],
                                                  scores['final_score']))

            rowIndex = rowIndex + 1

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters_scores.load_all_shooter_scores_trv_with_json Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    # end load_all_shooter_scores_trv_with_json

    def MouseButtonUpCallBack(event):
        global trv_all_shooter_scores

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters_scores.MouseButtonUpCallBack Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        currentRowIndex = trv_all_shooter_scores.selection()[0]

        my_logger.info('{time}, scores.load_all_shooters_scores.MouseButtonUpCallBack Called Cur Row Index: {currentRowIndex}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            currentRowIndex=currentRowIndex
        ))

        lastTuple = (trv_all_shooter_scores.item(currentRowIndex, 'values'))
        # Get from my_shooter_list dictionary the entire record matching the lastTuple[1], this is the id column
        my_row      = settings.find_row_in_my_shooter_list(lastTuple[1])
        my_jsonrec  = settings.my_shooter_list[my_row]
        # Lets edit/enter scores for selected shooter
        open_popup(my_jsonrec, tree_frame)

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters.MouseButtonUpCallBack Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end MouseButtonUpCallBack


    # Lets design/pain the popup, this is what is opened when the user clicks on a shooter in the treeview.
    def open_popup(json_record, primary):

        qualification_score = StringVar()
        final_score         = StringVar()

        def load_score_trv_with_json(array_of_targets, tree, _mode):

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters_scores.load_score_trv_with_json Called'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

                if echojson == 1:
                    settings.pp_json(array_of_targets)

            # clear out current treeview definition
            for item in tree.get_children():
                tree.delete(item)

            # end for item

            target_no = 0
            while target_no < len(array_of_targets):

                target_array    = array_of_targets[target_no]
                target_no       = target_array["target_number"]

                if target_no == 0:
                    if _mode == "qual":
                        target_name = "CB"
                    else:
                        target_name = "T" + str(target_no)
                else:
                    target_name = "T" + str(target_no)
                # end if target_no

                target_score    = target_array["target_score"]
                array_of_shots  = target_array["shots"]
                shot_no         = 0

                # Add the root objects - Targets
                if score_viewer == "tree":
                    tree.insert("", "end", target_name, text=target_name, values=(target_name, target_score))

                while shot_no < len(array_of_shots):
                    shots = array_of_shots[shot_no]

                    shot_name   = "S" + str( int(shots["shot_number"])+1)
                    hitt_miss   = shots["hit_miss"]
                    inspect     = shots["inspect"]

                    if score_viewer == "flat":
                        tree.insert(parent="",
                                    index=tk.END,
                                    text="",
                                    values=(target_name, shot_name, hitt_miss, inspect))
                    else:
                        tree.insert(parent=target_name,
                                    index=tk.END,
                                    text=shot_name,
                                    values=("", "", shot_name, hitt_miss, inspect))

                    # end if
                    shot_no = shot_no + 1

                # end while shot_no
                target_no = target_no + 1

            # end while target_no

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters_scores.load_score_trv_with_json Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        # end load_score_trv_with_json


        def save_score_to_file():

            q_score_json, q_score   = extract_score_from_trv(trv_qualification_scores, "qual")
            f_score_json, f_score   = extract_score_from_trv(trv_final_scores, "final")

            # save json structure for specific shooter back to file
            my_row = settings.find_row_in_my_shooter_list(json_record["id"])

            settings.my_shooter_list[my_row]["scores"]["qualifying_score"]  = q_score
            settings.my_shooter_list[my_row]["scores"]["final_score"]       = f_score
            settings.my_shooter_list[my_row]["scores"]["qualifying"]        = q_score_json
            settings.my_shooter_list[my_row]["scores"]["final"]             = f_score_json

            # Push everything back/down to the physical file - this allows other viewers to get updates as the scorer
            # saves updates to file.
            settings.save_json_to_file(settings.filename)

            # reload/refresh json structures from file
            # everything
            settings.my_event_list = settings.load_event_json_from_file(settings.filename)
            # all shooters
            settings.my_shooter_list    = settings.my_event_list["shooters"]
            settings.my_event_image     = settings.my_event_list["image"]

            # find specific shooter
            my_row      = settings.find_row_in_my_shooter_list(json_record["id"])
            my_shooter  = settings.my_shooter_list[my_row]
            # get scores for specific shooter
            list_of_all_scores_for_shooter = my_shooter["scores"]

            if debuglevel >= 2:
                my_logger.info(
                    '{time}, scores.load_all_shooters_scores.save_score_to_file Scores Reloaded from file'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))
                if echojson == 1:
                    settings.pp_json(list_of_all_scores_for_shooter)

            # end if

            # update displayed score: Qualification Round
            qualification_score.set(list_of_all_scores_for_shooter["qualifying_score"])
            # update displayed score: Final Round
            final_score.set(list_of_all_scores_for_shooter["final_score"])

            # reload treeviews
            load_score_trv_with_json(list_of_all_scores_for_shooter["qualifying"], trv_qualification_scores, "qual")
            load_score_trv_with_json(list_of_all_scores_for_shooter["final"], trv_qualification_scores, "final")

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters_scores.save_score_to_file Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        # end save_score_to_file


        def extract_score_from_trv(tree, mode):

            score       = 0

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters_scores.extract_score_from_trv Called, Mode: ({mode}) '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                    mode=mode
                ))
            # end if

            if score_viewer == "flat":

                targets = []
                shots   = []
                t_no    = 0
                for line in tree.get_children():

                    target_desc     = tree.item(line)['values'][0]
                    if target_desc == "CB":
                        target_number = 0
                    else:
                        target_number   = int(tree.item(line)['values'][0][1:])

                    # No target_score in this view
                    shot_no     = int(tree.item(line)['values'][1][1:])
                    hit_miss    = tree.item(line)['values'][2]
                    inspect     = tree.item(line)['values'][3]

                    # First time we get in here is on the 2nd loop, at which point we append the T=0 aka CB
                    if t_no + 1 == target_number:
                        # Append
                        dict = {"target_number" : t_no,     # t_no is the working target,
                                "target_score"  : 321,
                                "shots"         : shots
                                }
                        # Append list of shots
                        targets.append(dict)

                        print("Target: ", t_no)
                        settings.pp_json(targets)

                        # Reset the target we're working on
                        t_no = target_number
                        shots = []

                    shot = {"shot_number"   : shot_no,
                            "hit_miss"      : hit_miss,
                            "inspect"       : inspect}

                    shots.append(shot)

                # end for line

                # End list, we're completed the loop, lets add the last shots for the last target
                dict = {"target_number" : t_no,
                        "target_score"  : 321,
                        "shots"         : shots
                        }
                targets.append(dict)

            else:
                pass

            # end if score_viewer

            if debuglevel >= 2:
                my_logger.info('{time}, scores.load_all_shooters_scores.extract_score_from_trv Completed, Mode: ({mode})'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                    mode=mode
                ))

            # end if
            return targets, score

        # end extract_score_from_trv


        def discard_score():

            if debuglevel >= 2:
                my_logger.info('{time}, score.load_all_shooters_scores.open_popup.discard_score Called '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            # For now we just exit....
            child.destroy()

            if debuglevel >= 2:
                my_logger.info('{time}, score.load_all_shooters_scores.open_popup.discard_score Completed '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        # end discard_score


        # json_record comprises of the entire record of the current shooter, lets get the scores section only
        list_of_all_scores          = json_record["scores"]
        # now extract the qualifying and final round scores
        list_of_qualifying_scores   = list_of_all_scores["qualifying"]
        list_of_finals_scores       = list_of_all_scores["final"]

        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters.open_popup Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

            if echojson == 1:
                settings.pp_json(json_record)

        child = Toplevel(primary)
        child.title('Shooter Score Maintenance')
        child.geometry("1100x825")
        child.configure(bg=frame_bg)
        child.grab_set()  # allow it to receive events

        load_form = True

        shooter_frame       = Frame(child)
        scores_frame        = Frame(child)
        cntrls_frame        = Frame(child)

        shooter_frame.grid(row=0, column=0, sticky="W", pady=(1, 5))
        scores_frame.grid(row=1, column=0,  sticky="W", padx=(1, 5))
        cntrls_frame.grid(row=2, column=0,  sticky="W", pady=(5, 0))

        # Frame Layout
        shooter_lbframe = LabelFrame(shooter_frame, text='Shooter Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        shooter_lbframe.grid()

        # Frame Layout : Score Frame
        score_lbframe = LabelFrame(scores_frame, text='Scores', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        score_lbframe.grid()

        # Frame Layout : Qualifying Scores in score frame
        qualifying_lbframe = LabelFrame(scores_frame, text='Qualifying Scores', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        qualifying_lbframe.grid(row=0, column=0, sticky="W", padx=(1, 5))

        # Frame Layout : Final Scores in score frame
        final_lbframe = LabelFrame(scores_frame, text='Final Scores', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        final_lbframe.grid(row=0, column=1, sticky="W", padx=(1, 5))

        # Frame Layout : Buttons in buttons frame
        cntrls_lbframe = LabelFrame(cntrls_frame, bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size), relief=RIDGE)
        cntrls_lbframe.grid()

        # Shooter
        lb_shooter1 = Label(shooter_lbframe, text="First Name", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter2 = Label(shooter_lbframe, text="Last Name", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
        lb_shooter3 = Label(shooter_lbframe, text="Spotter", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

        lb_shooter1.grid(row=1, column=0, padx=5, pady=0)
        lb_shooter2.grid(row=2, column=0, padx=5, pady=0)
        lb_shooter3.grid(row=3, column=0, padx=5, pady=0)

        id_value = StringVar()
        id_value.set(json_record["id"])
        fname_value = StringVar()
        fname_value.set(json_record["first_name"])
        lname_value = StringVar()
        lname_value.set(json_record["last_name"])
        spotter_value = StringVar()
        spotter_value.set(json_record["spotter"])

        qualification_score.set(list_of_all_scores["qualifying_score"])
        final_score.set(list_of_all_scores["final_score"])

        # Shooter
        crm_shooter_fname = Label(shooter_lbframe, anchor="w", height=1, textvariable=fname_value, font=(txtfont, txtfont_size))
        crm_shooter_fname.grid(row=1, column=1, padx=20)

        crm_shooter_lname = Label(shooter_lbframe, anchor="w", height=1, textvariable=lname_value, font=(txtfont, txtfont_size))
        crm_shooter_lname.grid(row=2, column=1, padx=20)

        crm_shooter_spotter = Label(shooter_lbframe, anchor="w", height=1, textvariable=spotter_value, font=(txtfont, txtfont_size))
        crm_shooter_spotter.grid(row=3, column=1, padx=20)


        # Qualifications Score Layout
        lb_crm_q_score = Label(qualifying_lbframe, text="Score", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
        lb_crm_q_score.grid(column=0, row=0, padx=1, pady=0)
        crm_q_score   = Entry(qualifying_lbframe, textvariable = qualification_score, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_q_score.grid(row=0, column=2)

        # Qualification Scores treeview
        if score_viewer == "flat":
            trv_qualification_scores = settings.TreeviewEdit(qualifying_lbframe, columns=(1, 2, 3, 4), show="headings", height="18")
            trv_qualification_scores.grid(row=1, column=0, rowspan=16, columnspan=9)

            trv_qualification_scores.heading("#0", text="",             anchor="w")
            trv_qualification_scores.heading("#1", text="Target #",     anchor="center")
            trv_qualification_scores.heading("#2", text="Shot #",       anchor="center")
            trv_qualification_scores.heading("#3", text="Hitt/Miss",    anchor="center")
            trv_qualification_scores.heading("#4", text="Inspect",      anchor="center")
            trv_qualification_scores.column("#0", anchor="w", width=60,     stretch=True)
            trv_qualification_scores.column("#1", anchor="w", width=100,    stretch=True)
            trv_qualification_scores.column("#2", anchor="w", width=100,    stretch=True)
            trv_qualification_scores.column("#3", anchor="w", width=100,    stretch=True)
            trv_qualification_scores.column("#4", anchor="w", width=100,    stretch=True)
        else:
            trv_qualification_scores = settings.TreeviewEdit(qualifying_lbframe, columns=(1, 2, 3, 4, 6), show="headings", height="21")
            trv_qualification_scores.grid(row=1, column=0, rowspan=19, columnspan=9)

            trv_qualification_scores.heading("#0", text="",             anchor="w")
            trv_qualification_scores.heading("#1", text="Target #",     anchor="center")
            trv_qualification_scores.heading("#2", text="Target Score", anchor="center")
            trv_qualification_scores.heading("#3", text="Shot #",       anchor="center")
            trv_qualification_scores.heading("#4", text="Hitt/Miss",    anchor="center")
            trv_qualification_scores.heading("#5", text="Inspect",      anchor="center")
            trv_qualification_scores.column("#0", anchor="w", width=60,     stretch=True)
            trv_qualification_scores.column("#1", anchor="w", width=100,    stretch=True)
            trv_qualification_scores.column("#2", anchor="w", width=100,    stretch=True)
            trv_qualification_scores.column("#3", anchor="w", width=100,    stretch=True)
            trv_qualification_scores.column("#4", anchor="w", width=100,    stretch=True)
            trv_qualification_scores.column("#5", anchor="w", width=100,    stretch=True)

        qualifying_lbframe.grid(row=2, column=0)


        # Finals Score Layout
        lb_crm_f_score = Label(final_lbframe, text="Score", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
        lb_crm_f_score.grid(column=0, row=0, padx=1, pady=0)
        crm_f_score   = Entry(final_lbframe, textvariable = final_score, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_f_score.grid(row=0, column=2)


        # Finals Score treeview
        if score_viewer == "flat":
            trv_final_scores = settings.TreeviewEdit(final_lbframe, columns=(1, 2, 3, 4), show="headings", height="18")
            trv_final_scores.grid(row=1, column=0, rowspan=16, columnspan=9)

            trv_final_scores.heading("#0", text="",             anchor="w")
            trv_final_scores.heading("#1", text="Target #",     anchor="center")
            trv_final_scores.heading("#2", text="Shot #",       anchor="center")
            trv_final_scores.heading("#3", text="Hitt/Miss",    anchor="center")
            trv_final_scores.heading("#4", text="Inspect",      anchor="center")
            trv_final_scores.column("#0", anchor="w", width=60,     stretch=True)
            trv_final_scores.column("#1", anchor="w", width=100,    stretch=True)
            trv_final_scores.column("#2", anchor="w", width=100,    stretch=True)
            trv_final_scores.column("#3", anchor="w", width=100,    stretch=True)
            trv_final_scores.column("#4", anchor="w", width=100,    stretch=True)
        else:
            trv_final_scores = settings.TreeviewEdit(final_lbframe, columns=(1, 2, 3, 4, 5), show="headings", height="21")
            trv_final_scores.grid(row=1, column=0, rowspan=19, columnspan=9)

            trv_final_scores.heading("#0", text="",             anchor="w")
            trv_final_scores.heading("#1", text="Target #",     anchor="center")
            trv_final_scores.heading("#2", text="Target Score", anchor="center")
            trv_final_scores.heading("#3", text="Shot #",       anchor="center")
            trv_final_scores.heading("#4", text="Hitt/Miss",    anchor="center")
            trv_final_scores.heading("#5", text="Inspect",      anchor="center")
            trv_final_scores.column("#0", anchor="w", width=60,     stretch=True)
            trv_final_scores.column("#1", anchor="w", width=100,    stretch=True)
            trv_final_scores.column("#2", anchor="w", width=100,    stretch=True)
            trv_final_scores.column("#3", anchor="w", width=100,    stretch=True)
            trv_final_scores.column("#4", anchor="w", width=100,    stretch=True)
            trv_final_scores.column("#5", anchor="w", width=100,    stretch=True)

        final_lbframe.grid(row=2, column=1)

        load_score_trv_with_json(list_of_qualifying_scores, trv_qualification_scores, "qual")
        load_score_trv_with_json(list_of_finals_scores, trv_final_scores, "finals")

        # Add Buttons
        btnSave = Button(cntrls_lbframe, text="Save", padx=5, pady=10, command=save_score_to_file)
        btnSave.grid(row=0, column=0)

        btnExit = Button(cntrls_lbframe, text="Exit", padx=5, pady=10, command=discard_score)
        btnExit.grid(row=0, column=1)


        if debuglevel >= 2:
            my_logger.info('{time}, scores.load_all_shooters.open_popup Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end open_popup


    trv_all_shooter_scores.bind("<ButtonRelease>", MouseButtonUpCallBack)
    settings.load_all_shooter_scores_json_from_file(settings.filename)
    load_all_shooter_scores_trv_with_json()

    if debuglevel >= 2:
        my_logger.info('{time}, scores.load_all_shooters_scores Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_shooters_scores