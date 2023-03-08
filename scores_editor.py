########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
#
#   File            :   scores_editor.py
#
#	By              :   George Leonard ( georgelza@gmail.com )
#
#   Created     	:   0.0.1 - 6 September 2022
#
#   Changelog       :   0.0.1 -
#
#   Notes       	:
########################################################################################################################
__author__  = "George Leonard"
__email__   = "georgelza@gmail.com"
__version__ = "0.0.1"

from tkinter import *
from tkinter import ttk, Scrollbar
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
from os.path import join, dirname
import os

import settings, events, scores_display

my_logger       = settings.my_logger
debuglevel      = settings.debuglevel
echojson        = settings.echojson


# We will add the scores via the File/scores menu.
# For now ust build Scott's Treeview and user editor, then replace with my data.
def edit_all_shooters_scores(main_window):

    global score_viewer
    global trv_edt_shooter_scores
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
        my_logger.info('{time}, scores_editor.edit_all_shooters_scores.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    child = Toplevel(main_window)
    child.title = "Scores Editor"
    child.geometry("1130x800")
    child.configure(bg=frame_bg)

    # Disable Resize
    child.resizable(False, False)

    header_frame    = Frame(child)
    tree_frame      = Frame(child)
    footer_frame    = Frame(child)

    header_frame.pack(fill="both",  expand="yes", padx=10, pady=10)
    tree_frame.pack(fill="both",    expand="yes", padx=10, pady=10)
    footer_frame.pack(fill="both",  expand="yes", padx=10, pady=10)

    # Determine where we're running, as template and events are by default subdirectories of the App directory.
    directory = os.getcwd()

    if debuglevel >= 1:
        my_logger.info('{time}, scores_editor.edit_all_shooters_scores.Current App Directory {directory}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            directory=directory
        ))

    # Top Banner / Header
    # Read the Image
    image               = Image.open(join(dirname(__file__), "images/" + settings.my_event_image))
    # Resize the image using resize() method
    resize_image_event  = image.resize((150, 150))
    img1                = ImageTk.PhotoImage(resize_image_event)
    # create label and add resize image
    label1              = Label(header_frame, image=img1)
    label1.image        = img1
    label1.pack(side=tk.LEFT)

    yscrollbar = ttk.Scrollbar(tree_frame, orient='vertical')

    columns = ("Place", "", "Shooter", "Spotter", "Caliber", "Qualifying", "Finals", "Total")

    trv_edt_shooter_scores = ttk.Treeview(tree_frame, yscrollcommand=yscrollbar.set, columns=columns, show="headings", height="20")
    trv_edt_shooter_scores.grid(row=0, column=0, rowspan=20, columnspan=7, sticky=E+W)

    trv_edt_shooter_scores.heading("Place",      text="Place",      anchor="w")
    trv_edt_shooter_scores.heading("",           text="",           anchor="center")
    trv_edt_shooter_scores.heading("Shooter",    text="Shooter",    anchor="center")
    trv_edt_shooter_scores.heading("Spotter",    text="Spotter",    anchor="center")
    trv_edt_shooter_scores.heading("Caliber",    text="Caliber",    anchor="center")
    trv_edt_shooter_scores.heading("Qualifying", text="Qualifying", anchor="center")
    trv_edt_shooter_scores.heading("Finals",     text="Finals",     anchor="center")
    trv_edt_shooter_scores.heading("Total",      text="Total",      anchor="center")

    trv_edt_shooter_scores.column("#1", anchor="w", width=50,  stretch=True)
    trv_edt_shooter_scores.column("#2", anchor="w", width=1,   stretch=True)
    trv_edt_shooter_scores.column("#3", anchor="w", width=259, stretch=True)
    trv_edt_shooter_scores.column("#4", anchor="w", width=250, stretch=True)
    trv_edt_shooter_scores.column("#5", anchor="w", width=200, stretch=False)
    trv_edt_shooter_scores.column("#6", anchor="w", width=110, stretch=False)
    trv_edt_shooter_scores.column("#7", anchor="w", width=110, stretch=False)
    trv_edt_shooter_scores.column("#8", anchor="w", width=110, stretch=False)

    yscrollbar.configure(command=trv_edt_shooter_scores.yview())
    yscrollbar.grid(row=0, column=8, rowspan=10, sticky=NS)

    # Bottom Banner / Footer
    # Read the Image
    image           = Image.open(join(dirname(__file__), "images/" + settings.splash_footer))
    # Resize the image using resize() method
    resize_impactxs = image.resize((930, 150))
    img2            = ImageTk.PhotoImage(resize_impactxs)
    # create label and add resize image
    label2          = Label(footer_frame, image=img2)
    label2.image    = img2
    label2.grid(row=0, column=0, padx=5, pady=5)

    settings.trv_edt_shooter_scores = trv_edt_shooter_scores

    paintScoreTrv()

    def MouseButtonUpCallBack(event):

        if debuglevel >= 2:
            my_logger.info('{time}, scores_editor.edit_all_shooters_scores.MouseButtonUpCallBack.Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        try:
            currentRowIndex = trv_edt_shooter_scores.selection()[0]

            my_logger.info(
                '{time}, scores_editor.edit_all_shooters_scores.MouseButtonUpCallBack.Called Cur Row Index:{currentRowIndex}'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                    currentRowIndex=currentRowIndex
                ))

            lastTuple = (trv_edt_shooter_scores.item(currentRowIndex, 'values'))
            # Get from my_shooter_list dictionary the entire record matching the lastTuple[1], this is the id column
            my_row = settings.find_row_in_my_shooter_list(lastTuple[1])
            my_shooter = settings.my_shooter_list[my_row]

            # Lets edit/enter scores for selected shooter
            open_popup(my_shooter, tree_frame)

        except:
            # Not on grid, but rather on the header,
            pass

        if debuglevel >= 2:
            my_logger.info('{time}, scores_editor.edit_all_shooters_scores.MouseButtonUpCallBack.Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end MouseButtonUpCallBack


    # Lets design/pain the popup, this is what is opened when the user clicks on a shooter in the treeview.
    # We're going to add a event here when this screen is saved to repaint the main shooters trv, aka update it.
    def open_popup(json_record, primary):

        qualification_score = StringVar()
        final_score         = StringVar()
        total_score         = StringVar()

        # This is one of the 2 smaller treeviews, used to display the qualifying and the final scores
        # It's a generic routine thats used for both.
        def load_score_trv_with_json(array_of_targets, tree, _mode):

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.load_score_trv_with_json.Called ({mode})'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                    mode=_mode
                ))

                if echojson == 1:
                    settings.pp_json(array_of_targets)
            # end debuglevel

            # clear out current treeview definition
            for item in tree.get_children():
                tree.delete(item)

            # end for item
            if debuglevel >= 3:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.load_score_trv_with_json Treeview cleaned ({mode})'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                    mode=_mode
                ))

            my_logger.info(
                '{time}, scores_editor.edit_all_shooters_scores.open_popup.load_score_trv_with_json Treeview mode ({score_viewer})'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                    score_viewer=score_viewer
                ))

            target_no = 0
            while target_no < len(array_of_targets):

                target_array    = array_of_targets[target_no]

                if target_no == 0 and _mode == "qual":
                    target_name = "CB"

                else:
                    target_name = "T" + str(target_array["target_number"])

                # end if

                target_score    = target_array["target_score"]
                array_of_shots  = target_array["shots"]
                shot_no         = 0

                # Add the root objects - Targets
                if score_viewer == "tree":
                    tree.insert("", "end", target_name, text=target_name, values=(target_name, target_score), open=True)

                while shot_no < len(array_of_shots):

                    current_shot    = array_of_shots[shot_no]
                    shot_name       = "S" + str( current_shot["shot_number"]+1)
                    hit_miss        = current_shot["hit_miss"]
                    inspect         = current_shot["inspect"]
                    score           = current_shot["score"]

                    if score_viewer == "flat":
                        tree.insert(parent  = "",
                                    index   = tk.END,
                                    text    = "",
                                    values  = (target_name, shot_name, hit_miss, inspect))
                    else:  # tree

                        if debuglevel >= 3:
                            my_logger.info(
                                '{time}, scores_editor.edit_all_shooters_scores.open_popup.load_score_trv_with_json Treeview Insert Child to ({target_name}), ({shot_name}), ({hit_miss}), ({inspect}, {score})'.format(
                                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                    target_name=target_name,
                                    shot_name=shot_name,
                                    hit_miss=hit_miss,
                                    inspect=inspect,
                                    score=score
                                ))

                        tree.insert(parent  = target_name,
                                    index   = tk.END,
                                    text    = shot_name,
                                    values  = ("", "", shot_name, hit_miss, inspect),
                                    open=True)

                    # end if
                    shot_no = shot_no + 1

                # end while shot_no
                target_no = target_no + 1

            # end while target_no

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.load_score_trv_with_json.Completed ({mode})'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                    mode=_mode
                ))

        # end load_score_trv_with_json


        # Lets first extract and push the values back to the settings.* arrays
        # This helps us display the newest scored in score_display
        def update_scores_to_my_shooter_list():

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.update_scores_to_my_shooter_list.Called '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
            # end if

            # In these routines we calculate/update and extract the scores from the trv, for the displayed shooter.
            q_score_json, q_score = extract_score_from_trv(trv_qualification_scores, "qual")
            f_score_json, f_score = extract_score_from_trv(trv_final_scores, "final")
            t_score = q_score + f_score

            if debuglevel >= 3:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.update_scores_to_my_shooter_list Scores Extracted '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
            # end if

            # Find out which row in array the shooter is associated with
            my_row = settings.find_row_in_my_shooter_list(json_record["id"])

            if debuglevel >= 3:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.update_scores_to_my_shooter_list Locate array position of shooter '.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))
            # end if

            # Update that row in array with the values of the shooter that we've been busy with
            settings.my_shooter_list[my_row]["scores"]["qualifying_score"]  = q_score
            settings.my_shooter_list[my_row]["scores"]["final_score"]       = f_score
            settings.my_shooter_list[my_row]["scores"]["total_score"]       = t_score
            settings.my_shooter_list[my_row]["scores"]["qualifying"]        = q_score_json
            settings.my_shooter_list[my_row]["scores"]["final"]             = f_score_json

            # Update the entire event structure with the new shooters sub structure
            settings.my_event_list["shooters"] = settings.my_shooter_list

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.update_scores_to_my_shooter_list.Completed '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
            # end if

        # end update_scores_to_my_shooter_list


        # Refresh the 2 smaller TRV's and then also the 3 totals, qualifying, final and totals scores displayed from settings.my_event_list as primary source
        def refresh_trv_scores():

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.refresh_trv_scores.Called '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
            # end if

            # Refresh settings.[arrays]
            settings.my_event_list      = settings.load_event_json_from_file(settings.filename)
            settings.my_event_image     = settings.my_event_list["image"]
            settings.my_shooter_list    = settings.my_event_list["shooters"]
            my_row                      = settings.find_row_in_my_shooter_list(json_record["id"])

            if my_row != -1:
                # This is my specific shooter
                my_shooter = settings.my_shooter_list[my_row]

                if debuglevel >= 3:
                    my_logger.info(
                        '{time}, scores_editor.edit_all_shooters_scores.open_popup.refresh_trv_scores find_row_in_my_shooter_list Row:{row}'.format(
                            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            row=my_row
                        ))
                    if echojson == 1:
                        settings.pp_json(my_shooter)

                # end if
            else:
                # We need to figure out how to exit now... this implies we could not find our shooter in the array of shooters
                pass

            # get scores for specific shooter
            list_of_all_scores_for_shooter = my_shooter["scores"]

            if debuglevel >= 3:
                my_logger.info(
                    '{time}, scores_editor.edit_all_shooters_scores.open_popup.refresh_trv_scores list_of_all_scores_for_shooter'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))
                if echojson == 1:
                    settings.pp_json(list_of_all_scores_for_shooter)

            # end if

            # update displayed score: Qualification Round
            qualification_score.set(list_of_all_scores_for_shooter["qualifying_score"])
            if debuglevel >= 3:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.refresh_trv_scores Qualification Round: {qscore} '.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                        qscore=qualification_score.get()
                    ))
            # end if

            # update displayed score: Final Round
            final_score.set(list_of_all_scores_for_shooter["final_score"])
            if debuglevel >= 3:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.refresh_trv_scores Final Round: {fscore} '.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                        fscore=final_score.get()
                    ))
            # end if

            # update displayed score: Total for both rounds
            total_score.set(list_of_all_scores_for_shooter["total_score"])
            if debuglevel >= 3:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.refresh_trv_scores Total Score: {tscore} '.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                        tscore=total_score.get()
                    ))
            # end if

            # reload the 2 treeviews with new data
            # Load qualifying score trv
            load_score_trv_with_json(list_of_all_scores_for_shooter["qualifying"], trv_qualification_scores, "qual")
            if debuglevel >= 3:
                my_logger.info(
                    '{time}, scores_editor.edit_all_shooters_scores.open_popup.refresh_trv_scores Qual trv reloaded '.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))
            # end if

            # Load Final score trv
            load_score_trv_with_json(list_of_all_scores_for_shooter["final"], trv_final_scores, "final")
            if debuglevel >= 3:
                my_logger.info(
                    '{time}, scores_editor.edit_all_shooters_scores.open_popup.refresh_trv_scores Final trv reloaded '.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))
            # end if

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.refresh_trv_scores.Completed '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
            # end if

        # end refresh_scores

        # Extract the structure and hit/miss and inspects results entered from the TreeView back into the JSON structure for the score,
        # to be saved back for the current shooter.
        def extract_score_from_trv(tree, mode):

            # mode is "qual" or "final"

            targets = []
            shots = []
            target_score = 0
            round_score = 0

            if debuglevel >= 2:
                my_logger.info(
                    '{time}, scores_editor.edit_all_shooters_scores.open_popup.extract_score_from_trv.Called, Mode: ({mode}) '.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                        mode=mode
                    ))
            # end if

            # If we're using the flat display structure
            if score_viewer == "flat":

                if debuglevel >= 2:
                    my_logger.info(
                        '{time}, scores_editor.edit_all_shooters_scores.open_popup.extract_score_from_trv Entering Flat Extract '.format(
                            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            mode=mode
                        ))
                # end if

                for line in tree.get_children():

                    target_desc = tree.item(line)['values'][0]
                    if target_desc == "CB":
                        target_number = 0

                    else:
                        target_number = int(tree.item(line)['values'][0][1:])

                    # No target_score in this view
                    shot_no = int(tree.item(line)['values'][1][1:]) - 1
                    hit_miss = str(tree.item(line)['values'][2])
                    inspect = tree.item(line)['values'][3]

                    distance = settings.get_target_distance(target_number, mode)

                    # Multiplier is based on the shot_number,
                    # Cold bore is always shot_number == 0, thus = 5
                    #   shot 0 counts = 5 - shot_number  = 5
                    #   shot 1 counts = 5 - shot_number  = 4
                    #   shot 2 counts = 5 - shot_number  = 3
                    #   shot 3 counts = 5 - shot_number  = 2
                    #   shot 4 counts = 5 - shot_number  = 1

                    multiplier = 5 - shot_no

                    # Shot Score = Multiplier x (distance in yards x distance in yards)/3000

                    # Lets make sure we understand what was entered and try and correct to what we really wanted - Data Quality
                    if hit_miss == "y" or hit_miss == "Y" or hit_miss == "Yes" or hit_miss == "YES" or hit_miss == "True" or hit_miss == "TRUE" or hit_miss == "T":
                        hit_miss = "1"
                    elif hit_miss == "n" or hit_miss == "N" or hit_miss == "No" or hit_miss == "NO" or hit_miss == "False" or hit_miss == "FALSE" or hit_miss == "F":
                        hit_miss = "0"
                    elif hit_miss != "0" and hit_miss != "1":
                        hit_miss = "0"

                    if inspect == "true" or inspect == "TRUE" or inspect == "T" or inspect == "Y" or inspect == "Yes" or inspect == "YES" or inspect == "1":
                        inspect = "True"
                    elif inspect == "false" or inspect == "FALSE" or inspect == "F" or inspect == "N" or inspect == "No" or inspect == "NO" or inspect == "0":
                        inspect = "False"
                    elif inspect != "True" and inspect != "False":
                        inspect = "False"

                    # Cold Bore
                    if target_number == 0:
                        if hit_miss == "1":
                            shot_score = multiplier * round((distance * distance) / 3000)

                        else:
                            shot_score = 0

                        shot = {"shot_number": shot_no,
                                "hit_miss": str(hit_miss),
                                "inspect": inspect,
                                "score": shot_score}

                        # Append the individual shot to shot array
                        shots.append(shot)

                        # Add shot score to target score
                        target_score = target_score + shot_score

                        # Append
                        dict = {"target_number": 0,
                                "target_score": target_score,
                                "shots": shots
                                }

                        # Append list of shots
                        targets.append(dict)

                        # Add target score to round score
                        round_score = round_score + target_score

                        # Lets prep for the next T1 Target
                        shots = []
                        cur_target = 1
                        target_score = 0

                    else:

                        if cur_target != target_number:
                            # If this happens then it implies we've ticket over to the next started so lets append the shots and score...
                            # Append
                            dict = {"target_number": cur_target,  # t_no is the working target,
                                    "target_score": target_score,
                                    "shots": shots
                                    }

                            # Append list of shots
                            targets.append(dict)

                            # Add target score to round score
                            round_score = round_score + target_score

                            shots = []
                            cur_target = target_number
                            target_score = 0

                            # Calculate/Update score
                            if hit_miss == "1":
                                shot_score = multiplier * round((distance * distance) / 3000)

                            else:
                                shot_score = 0

                            shot = {"shot_number": shot_no,
                                    "hit_miss": str(hit_miss),
                                    "inspect": inspect,
                                    "score": shot_score}

                            shots.append(shot)

                            # Add shot score to target score
                            target_score = target_score + shot_score

                        else:

                            # Calculate/Update score
                            if hit_miss == "1":
                                shot_score = multiplier * (distance * distance) / 3000
                                shot_score = round(shot_score, 0)

                            else:
                                shot_score = 0

                            shot = {"shot_number": shot_no,
                                    "hit_miss": str(hit_miss),
                                    "inspect": inspect,
                                    "score": shot_score}

                            shots.append(shot)

                            # Add shot score to target score
                            target_score = target_score + shot_score

                    # end target_desc == 0
                # end for line in tree.get_children()

                # End list, we're completed the loop, lets add the last shots for the last target
                dict = {"target_number": cur_target,  # t_no is the working target,
                        "target_score": target_score,
                        "shots": shots
                        }
                # Append list of shots
                targets.append(dict)

                # Add target score to round score
                round_score = round_score + target_score

            # If we're using the Parent/Child Treeview display structure
            else:
                if debuglevel >= 2:
                    my_logger.info(
                        '{time}, scores_editor.edit_all_shooters_scores.open_popup.extract_score_from_trv Entering Tree Extract '.format(
                            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            mode=mode
                        ))
                # end if

            # end if score_viewer

            if debuglevel >= 2:
                my_logger.info(
                    '{time}, scores_editor.edit_all_shooters_scores.open_popup.extract_score_from_trv.Completed, Mode: ({mode})'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                        mode=mode
                    ))

            # end if

            return targets, round_score

        # end extract_score_from_trv

        def save_and_refresh_scores():

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.save_and_refresh_scores.Called '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
            # end if

            # In Memory
            # Update settings.* arrays
            update_scores_to_my_shooter_list()

            # Persists to file
            # Push everything back/down to the physical file - this allows other viewers to get updates as the scorer
            settings.save_event(settings.filename)

            # Refresh/Repaint the Qual and Final Treeviews
            refresh_trv_scores()

            #paintScoreTrv()                                     # Repaint the local (edit) trv
            events.dispatch("edit_all_shooters_scores")         # Update the score_display should it be active.

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.save_and_refresh_scores.Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        # end save_and_refresh_scores


        def exit_and_refresh_scores():

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.exit_and_refresh_scores.Called '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            # First we push the scores back to the settings.* arrays
            update_scores_to_my_shooter_list()

            # Push everything back/down to the physical file - this allows other viewers to get updates as the scorer
            # saves updates to file.
            settings.save_event(settings.filename)

            # For now we just exit....
            child.destroy()

            #paintScoreTrv()                                     # Repaint the local (edit) trv
            events.dispatch("edit_all_shooters_scores")         # this should call the paint function for the score displayer

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.exit_and_refresh_scores.Completed '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        # end exit_and_refresh_scores


        def discard_and_exit():

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.discard_and_exit.Called '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

            # For now we just exit....
            child.destroy()

            if debuglevel >= 2:
                my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.discard_and_exit.Completed '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

        # end discard_and_exit


        # json_record comprises of the entire record of the current shooter, lets get the scores section only
        list_of_all_scores          = json_record["scores"]
        # now extract the qualifying and final round scores
        list_of_qualifying_scores   = list_of_all_scores["qualifying"]
        list_of_finals_scores       = list_of_all_scores["final"]

        if debuglevel >= 2:
            my_logger.info('{time}, scores_editor.edit_all_shooters_scores.open_popup.Called'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

            if echojson == 1:
                settings.pp_json(json_record)

        child = Toplevel(primary)
        child.title('Shooter Score Maintenance')
        if score_viewer == "flat":
            child.geometry("825x685")
        else:
            child.geometry("1025x665")

        child.configure(bg=frame_bg)
        child.grab_set()  # allow it to receive events

        load_form = True

        shooter_frame       = Frame(child)
        scores_frame        = Frame(child, bg=frame_bg)
        cntrls_frame        = Frame(child)

        shooter_frame.grid(row=0, column=0, sticky="W", pady=(1, 5))
        scores_frame.grid(row=1, column=0,  sticky="W", padx=(1, 5))
        cntrls_frame.grid(row=2, column=0,  sticky="NS", pady=(5, 5), padx=(1, 25))

        # Frame Layout
        shooter_lbframe = LabelFrame(shooter_frame, text='Shooter Profile', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        shooter_lbframe.grid()

        # Frame Layout : Score Frame
        score_lbframe = LabelFrame(scores_frame, text='Scores', bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        score_lbframe.grid()

        # Frame Layout : Qualifying Scores in score frame
        qualifying_lbframe = LabelFrame(scores_frame, text='Qualifying Scores', bg=frame_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        qualifying_lbframe.grid(row=1, column=0, sticky="W", padx=(1, 5))

        # Frame Layout : Final Scores in score frame
        final_lbframe = LabelFrame(scores_frame, text='Final Scores', bg=frame_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size))
        final_lbframe.grid(row=1, column=1, sticky="W", padx=(1, 5))

        # Frame Layout : Buttons in buttons frame
        cntrls_lbframe = LabelFrame(cntrls_frame, bg=label_text_bg, fg=label_text_fg, font=(lblframefont, lblframefont_size), relief=GROOVE)
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
        total_score.set(list_of_all_scores["total_score"])

        # Shooter
        crm_shooter_fname = Entry(shooter_lbframe, textvariable=fname_value, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_fname.grid(row=1, column=1, padx=20)

        crm_shooter_lname = Entry(shooter_lbframe, textvariable=lname_value, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_lname.grid(row=2, column=1, padx=20)

        crm_shooter_spotter = Entry(shooter_lbframe, textvariable=spotter_value, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_shooter_spotter.grid(row=3, column=1, padx=20)

        # Qualifications Score Layout
        lb_crm_q_score = Label(qualifying_lbframe, text="Score", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
        lb_crm_q_score.grid(column=0, row=0, padx=1, pady=0)
        crm_q_score   = Entry(qualifying_lbframe, textvariable=qualification_score, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_q_score.grid(row=0, column=2)

        # Qualification Scores treeview
        if score_viewer == "flat":
            trv_qualification_scores = settings.TreeviewEdit(qualifying_lbframe, columns=(1, 2, 3, 4), show="headings", height="18")
            trv_qualification_scores.grid(row=1, column=0, rowspan=16, columnspan=9)

            trv_qualification_scores.heading("#0", text="",                     anchor="w")
            trv_qualification_scores.heading("#1", text="Target #",             anchor="center")
            trv_qualification_scores.heading("#2", text="Shot #",               anchor="center")
            trv_qualification_scores.heading("#3", text="Hitt/Miss (0 or 1)",   anchor="center")
            trv_qualification_scores.heading("#4", text="Inspect (True or False)", anchor="center")
            trv_qualification_scores.column("#0", anchor="w", width=50,     stretch=True)
            trv_qualification_scores.column("#1", anchor="w", width=80,     stretch=True)
            trv_qualification_scores.column("#2", anchor="w", width=80,     stretch=True)
            trv_qualification_scores.column("#3", anchor="w", width=120,    stretch=True)
            trv_qualification_scores.column("#4", anchor="w", width=120,    stretch=True)

        else:
            trv_qualification_scores = settings.TreeviewEdit(qualifying_lbframe, columns=(1, 2, 3, 4, 5), show="headings", height="21")
            trv_qualification_scores.grid(row=1, column=0, rowspan=19, columnspan=9)

            trv_qualification_scores.heading("#0", text="",                         anchor="w")
            trv_qualification_scores.heading("#1", text="Target #",                 anchor="center")
            trv_qualification_scores.heading("#2", text="Target Score",             anchor="center")
            trv_qualification_scores.heading("#3", text="Shot #",                   anchor="center")
            trv_qualification_scores.heading("#4", text="Hitt/Miss (0 or 1)",       anchor="center")
            trv_qualification_scores.heading("#5", text="Inspect (True or False)",  anchor="center")

            trv_qualification_scores.column("#0", anchor="w", width=60,     stretch=True)
            trv_qualification_scores.column("#1", anchor="w", width=80,     stretch=True)
            trv_qualification_scores.column("#2", anchor="w", width=100,    stretch=True)
            trv_qualification_scores.column("#3", anchor="w", width=80,     stretch=True)
            trv_qualification_scores.column("#4", anchor="w", width=120,    stretch=True)
            trv_qualification_scores.column("#5", anchor="w", width=120,    stretch=True)

        qualifying_lbframe.grid(row=2, column=0)


        # Finals Score Layout
        lb_crm_f_score = Label(final_lbframe, text="Score", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
        lb_crm_f_score.grid(column=0, row=0, padx=1, pady=0)
        crm_f_score   = Entry(final_lbframe, textvariable = final_score, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_f_score.grid(row=0, column=2)

        # Total Score Layout
        lb_total = Label(score_lbframe, text="Total Score", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(lblfont, lblfont_size))
        lb_total.grid(column=0, row=0, padx=1, pady=0)
        crm_t_score   = Entry(score_lbframe, textvariable = total_score, width=20, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
        crm_t_score.grid(row=0, column=2)

        # Finals Score treeview
        if score_viewer == "flat":
            trv_final_scores = settings.TreeviewEdit(final_lbframe, columns=(1, 2, 3, 4), show="headings", height="18")
            trv_final_scores.grid(row=1, column=0, rowspan=16, columnspan=9)

            trv_final_scores.heading("#0", text="",                         anchor="w")
            trv_final_scores.heading("#1", text="Target #",                 anchor="center")
            trv_final_scores.heading("#2", text="Shot #",                   anchor="center")
            trv_final_scores.heading("#3", text="Hitt/Miss (0 or 1)",       anchor="center")
            trv_final_scores.heading("#4", text="Inspect (True or False)",  anchor="center")
            trv_final_scores.column("#0", anchor="w", width=50,     stretch=True)
            trv_final_scores.column("#1", anchor="w", width=80,     stretch=True)
            trv_final_scores.column("#2", anchor="w", width=80,     stretch=True)
            trv_final_scores.column("#3", anchor="w", width=120,    stretch=True)
            trv_final_scores.column("#4", anchor="w", width=120,    stretch=True)
        else:
            trv_final_scores = settings.TreeviewEdit(final_lbframe, columns=(1, 2, 3, 4, 5), show="headings", height="21")
            trv_final_scores.grid(row=1, column=0, rowspan=19, columnspan=9)

            trv_final_scores.heading("#0", text="",                         anchor="w")
            trv_final_scores.heading("#1", text="Target #",                 anchor="center")
            trv_final_scores.heading("#2", text="Target Score",             anchor="center")
            trv_final_scores.heading("#3", text="Shot #",                   anchor="center")
            trv_final_scores.heading("#4", text="Hitt/Miss (0 or 1)",       anchor="center")
            trv_final_scores.heading("#5", text="Inspect (True or False)",  anchor="center")
            trv_final_scores.column("#0", anchor="w", width=60,     stretch=True)
            trv_final_scores.column("#1", anchor="w", width=80,     stretch=True)
            trv_final_scores.column("#2", anchor="w", width=100,    stretch=True)
            trv_final_scores.column("#3", anchor="w", width=80,     stretch=True)
            trv_final_scores.column("#4", anchor="w", width=120,    stretch=True)
            trv_final_scores.column("#5", anchor="w", width=120,    stretch=True)

        final_lbframe.grid(row=2, column=1)

        load_score_trv_with_json(list_of_qualifying_scores, trv_qualification_scores, "qual")
        load_score_trv_with_json(list_of_finals_scores, trv_final_scores, "finals")

        # Add Buttons
        btnSave = Button(cntrls_lbframe, text="Save", padx=5, pady=10, command=save_and_refresh_scores)
        btnSave.grid(row=0, column=0)

        btnExit = Button(cntrls_lbframe, text="Exit", padx=5, pady=10, command=exit_and_refresh_scores)
        btnExit.grid(row=0, column=1)

        btnExit = Button(cntrls_lbframe, text="Cancel", padx=5, pady=10, command=discard_and_exit)
        btnExit.grid(row=0, column=2)

        if debuglevel >= 2:
            my_logger.info('{time}, scores_editor.load_all_shooters_scores.open_popup.Completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    #end open_popup


    trv_edt_shooter_scores.bind("<ButtonRelease>", MouseButtonUpCallBack)
    settings.load_all_shooter_scores_json_from_file(settings.filename)
    paintScoreTrv()

    if debuglevel >= 2:
        my_logger.info('{time}, scores_editor.edit_all_shooters_scores.Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end edit_all_shooters_scores

def paintScoreTrv():

    if debuglevel >= 2:
        my_logger.info('{time}, scores_editor.paintScoreTrv.Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    #Retrieve the treeview into which we're going to pain
    trv_edt_shooter_scores = settings.trv_edt_shooter_scores

    # Cleanout my score trv structure
    for item in trv_edt_shooter_scores.get_children():
        trv_edt_shooter_scores.delete(item)

    # paint/repaint it
    rowIndex = 1
    for key in settings.my_shooter_list:

        equipment   = key["equipment"]                          # Structure with equipment
        rifle       = equipment['rifle']                        # sub structure with rifle information
        scores      = key["scores"]                             # structure with scores

        trv_edt_shooter_scores.insert('', index='end', iid=rowIndex, text="",
                                      values=(rowIndex,
                                              key["id"],
                                              key["first_name"].strip() + " " + key["last_name"].strip(),
                                              key["spotter"],
                                              rifle["caliber"],
                                              scores['qualifying_score'],
                                              scores['final_score'],
                                              scores['total_score']))

        rowIndex = rowIndex + 1

    if debuglevel >= 2:
        my_logger.info('{time}, scores_editor.paintScoreTrv.Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end paintScoreTrv