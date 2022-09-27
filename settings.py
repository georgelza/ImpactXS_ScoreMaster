########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
#
#   File            :   settings.py
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

from datetime import datetime
from tkinter import filedialog as fd
from tkinter import ttk
import tkinter as tk

import logging
import os, socket, uuid, sys, json, time


def init():

    global my_logger

    global my_event_list
    global my_qualifying_target_list
    global my_finals_target_list
    global my_shooter_list

    global appname
    global debuglevel
    global loglevel
    global echojson
    global splashtime
    global score_viewer
    global currentRowIndex
    global filename
    global my_event_image
    global event_mode

    # Colours
    global frame_bg
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

    # Our Lists of fields for the event, qualifying round setup and final round setup and then a
    # lists of shooters...
    # all collapsed into one json structure when written to a file.
    my_event_list               = []
    my_qualifying_target_list   = []
    my_finals_target_list       = []
    my_shooter_list             = []

    appname             = "ImpactXS - ScoreMaster"

    # Read/Define Environment variables
    config_params       = getAppEnvVariables()
    loglevel            = config_params["loglevel"]
    echojson            = config_params['echojson']
    splashtime          = config_params["splashtime"]
    debuglevel          = config_params["debuglevel"]
    my_event_image      = ""
    event_mode          = ""
    score_viewer        = config_params["score_viewer"]

    # Global colors, to be moved to the environment variables, config_params
    frame_bg            = config_params["frame_bg"]
    label_text_bg       = config_params["label_text_bg"]
    label_text_fg       = config_params["label_text_fg"]
    entry_text_bg       = config_params["entry_text_bg"]
    entry_text_fg       = config_params["entry_text_fg"]
    txtfont             = config_params["txtfont"]
    txtfont_size        = config_params["txtfont_size"]
    lblfont             = config_params["lblfont"]
    lblfont_size        = config_params["lblfont_size"]
    lblframefont        = config_params["lblframefont"]
    lblframefont_size   = config_params["lblframefont_size"]

    # Logging Handler
    logging.root.handlers = []
    FORMAT = '%(levelname)s :%(message)s'
    logging.basicConfig(
        level=logging.INFO,
        format=FORMAT)

    my_logger = logging.getLogger(__name__)

    # create logger
    # Set Logging level
    if loglevel == 'INFO':
        my_logger.setLevel(logging.INFO)
        my_logger.info('{time}, settings.INFO LEVEL Activated'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    elif loglevel == 'DEBUG':
        my_logger.setLevel(logging.DEBUG)
        my_logger.debug('{time}, settings.DEBUG LEVEL Activated'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    elif loglevel == 'CRITICAL':
        my_logger.setLevel(logging.CRITICAL)
        my_logger.critical('{time}, settings.CRITICAL LEVEL Activated'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # end DEBUGLEVEL

    if debuglevel >= 1:
        print_config(config_params)

#end init

def getAppEnvVariables():

    Params = dict()

    Params['debuglevel']                = int(os.environ.get("DEBUGLEVEL"))
    Params['loglevel']                  = os.environ.get("LOGLEVEL")
    Params['echojson']                  = int(os.environ.get("ECHOJSON"))
    Params['splashtime']                = int(os.environ.get("SPLASHTIME"))
    Params['score_viewer']              = os.environ.get('SCORE_VIEWER')

    Params['frame_bg']                  = os.environ.get("frame_bg")
    Params['label_text_bg']             = os.environ.get("label_text_bg")
    Params['label_text_fg']             = os.environ.get("label_text_fg")
    Params['entry_text_bg']             = os.environ.get("entry_text_bg")
    Params['entry_text_fg']             = os.environ.get("entry_text_fg")

    Params['txtfont']                   = os.environ.get("txtfont")
    Params['txtfont_size']              = os.environ.get("txtfont_size")
    Params['lblfont']                   = os.environ.get("lblfont")
    Params['lblfont_size']              = os.environ.get("lblfont_size")
    Params['lblframefont']              = os.environ.get("lblframefont")
    Params['lblframefont_size']         = os.environ.get("lblframefont_size")

    return Params

# end getAppEnvVariables():

#
# Lets get the Hostname and IP address so that we can include this into the Log stream
#
def get_system_info():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]

    except:
        IP = '127.0.0.1'

    finally:
        s.close()

    HOSTNAME = os.getenv('HOSTNAME')
    if not HOSTNAME:
        HOSTNAME = socket.gethostname()

    return IP, HOSTNAME

#end get_system_info

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

def print_config(config_params):

    if debuglevel >= 1:
        my_logger.info('*******************************************')
        my_logger.info('*                                         *')
        my_logger.info('*      Welcome to ImpactXS ScoreMaster    *')
        my_logger.info('*                                         *')
        my_logger.info('*          '+ time.strftime('%Y/%m/%d %H:%M:%S') + '            *')
        my_logger.info('*                                         *')
        my_logger.info('*     by georgel@bankservafrica.com       *')
        my_logger.info('*                                         *')
        my_logger.info('*******************************************')
        my_logger.info('**')
        my_logger.info('**    DEBUGLEVEL            : ' + str(config_params['debuglevel']))
        my_logger.info('**    LOGLEVEL              : ' + str(config_params['loglevel']))
        my_logger.info('**    ECHOJSON              : ' + str(config_params['echojson']))
        my_logger.info('**    SPLASHTIME            : ' + str(config_params['splashtime']))
        my_logger.info('**    SCORE_VIEWER          : ' + str(config_params['score_viewer']))
        my_logger.info('**')
        my_logger.info('**    frame_bg              : ' + str(config_params['frame_bg']))
        my_logger.info('**    label_text_bg         : ' + str(config_params['label_text_bg']))
        my_logger.info('**    label_text_fg         : ' + str(config_params['label_text_fg']))
        my_logger.info('**    entry_text_bg         : ' + str(config_params['entry_text_bg']))
        my_logger.info('**    entry_text_fg         : ' + str(config_params['entry_text_fg']))
        my_logger.info('**')
        my_logger.info('**    txtfont               : ' + str(config_params['txtfont']))
        my_logger.info('**    txtfont_size          : ' + str(config_params['txtfont_size']))
        my_logger.info('**    lblfont               : ' + str(config_params['lblfont']))
        my_logger.info('**    lblfont_size          : ' + str(config_params['lblfont_size']))
        my_logger.info('**    lblframefont          : ' + str(config_params['lblframefont']))
        my_logger.info('**    lblframefont_size     : ' + str(config_params['lblframefont_size']))
        my_logger.info('**')
        my_logger.info('*******************************************')

    # end if DEBUGLEVEL >= 1:

#end print_config()


def find_row_in_my_shooter_list(guid_value):

    global my_shooter_list

    if debuglevel >= 2:
        my_logger.info('{time}, settings.find_row_in_my_shooter_list Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    row = 0
    found = False

    for rec in my_shooter_list:
        if rec["id"] == guid_value:
            found = True
            break
        row = row + 1

    if (found == True):
        return (row)

    return (-1)

#end find_row_in_my_shooter_list

# Open/Select file dialog box
def file_dialog(mode):

    filetypes = (
        ('json files', '*.json'),
        ('All files', '*.*')
    )

    if debuglevel >= 1:
        my_logger.info('{time}, settings.file_dialog Called, Mode: ({mode})'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            mode=mode
        ))

    # Determine where we're running, as template and events are by default subdirectories of the App directory.
    directory = os.getcwd()
    if debuglevel >= 1:
        my_logger.info('{time}, settings.file_dialog.Current App Directory {directory}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            directory=directory
        ))

    if mode == "Load_Template":
        # We're creating a new event, so lets present a event template.
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir=directory + '/template',
            filetypes=filetypes)

    elif mode == "Initial_Event_Save":
        filename = fd.asksaveasfile(
            title='Save file As',
            initialdir=directory + '/events',
            filetypes=filetypes)

        filename = filename.name

    else:
        #we're opening a previous defined event, so lets show saved events from ./events folder as default.
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir=directory + '/events',
            filetypes=filetypes)

    if filename:
        if debuglevel >= 1:
            my_logger.info('{time}, settings.file_dialog.File: {file}'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                file=filename
            ))

        return filename
    else:
        if debuglevel >= 1:
            my_logger.info('{time}, settings.file_dialog.Aborted, No File Selected'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))
        return ""

# end file_dialog

def save_json_to_file(myfile):

    global my_event_list
    global my_qualifying_list
    global my_final_list
    global my_shooter_list
    global event_mode

    if debuglevel >= 2:
        my_logger.info('{time}, settings.save_json_to_file Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    if event_mode == "Initial_Event_Save":
        myfile      = file_dialog("Initial_Event_Save")
        event_mode  = "Load_Event"

    try:
        if myfile:
            with open(myfile, "w") as file_handler:
                my_event_list["qualifying"] = my_qualifying_target_list
                my_event_list["final"]      = my_finals_target_list
                my_event_list["shooters"]   = my_shooter_list

                json.dump(my_event_list, file_handler, indent=4)
        else:
            if debuglevel >= 2:
                my_logger.info('{time}, settings.save_json_to_file.No target file defined. File Save Aborted!!! '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))


    except IOError as e:
        my_logger.error('{time}, settings.load_event_json_from_file.I/O error: {file}, {errno}, {strerror}"'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=filename,
            errno=e.errno,
            strerror=e.strerror
        ))

    except:  # handle other exceptions such as attribute errors
        my_logger.error('{time}, settings.load_event_json_from_file.Unexpected error: {file}, {error}"'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=filename,
            error=sys.exc_info()[0]
        ))


    finally:
        file_handler.close

        if debuglevel >= 2:
            my_logger.info('{time}, settings.save_json_to_file.file has been written to and closed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

#end save_json_to_file


def load_event_json_from_file(filename):

    if debuglevel >= 1:
        my_logger.info('{time}, settings.load_event_json_from_file Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

        my_logger.info('{time}, settings.load_event_json_from_file.Loading file: {file}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=filename
        ))

    try:
        with open(filename, "r") as file_handler:
            my_event   = json.load(file_handler)

        if echojson == 1:
            if debuglevel >= 2:
                my_logger.info('{time}, settings.load_event_json_from_file.Printing my_event_list'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

                print("------ my_event_list ------")
                pp_json(my_event)

                print("--------------------------------")

    except IOError:
        my_logger.error('{time}, settings.load_event_json_from_file.Could not read file: {file}"'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=filename
        ))

    except:  # handle other exceptions such as attribute errors
        my_logger.error('{time}, settings.load_event_json_from_file.Unexpected error: {file}, {error}"'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=filename,
            error=sys.exc_info()[0]
        ))

    finally:
        file_handler.close

        if debuglevel >= 1:
            my_logger.info('{time}, settings.load_event_json_from_file Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        return my_event

# end load_event_json_from_file

# Refresh data in memory from file (include updating global settings variable),
# shooters include their personal data,
# equipment and scores
def load_all_shooter_scores_json_from_file(filename):

    global my_event_list

    if debuglevel >= 1:
        my_logger.info('{time}, settings.load_all_shooter_scores_json_from_file Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # Refreshes my_event_list structure from file
    load_event_json_from_file(filename)

    # extract array for shooters data from larger my_event_list structure
    my_shooter_list = my_event_list["shooters"]

    if debuglevel >= 1:
        if echojson == 1:
            my_logger.info('{time}, settings.load_all_shooter_scores_json_from_file my_shooter_list '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))
            pp_json(my_shooter_list)

        my_logger.info('{time}, settings.load_all_shooter_scores_json_from_file.file has been read and closed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_shooter_scores_json_from_file


# Our special Treeview class that allows us to edit cells in place
class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.bind("<Double-1>", self.on_double_click)

    def on_double_click(self, event):
        region_clicked = self.identify_region(event.x, event.y)

        if region_clicked not in ("tree", "cell"):
            return

        column = self.identify_column(event.x)
        column_index = int(column[1:]) - 1
        selected_iid = self.focus()
        select_values = self.item(selected_iid)

        if column == "#0":
            selected_text = select_values.get("text")
        else:
            selected_text = select_values.get("values")[column_index]

        # This gives us the X/Y of the box and then the Width/Height
        column_box = self.bbox(selected_iid, column, )
        entry_edit = ttk.Entry(self, width=column_box[2])

        # Record the column index and item iid
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_iid = selected_iid

        entry_edit.insert(0, selected_text)
        entry_edit.select_range(0, tk.END)

        entry_edit.focus()
        entry_edit.bind("<FocusOut>", self.on_focus_out)
        entry_edit.bind("<Return>", self.on_enter_pressed)

        entry_edit.place(x=column_box[0],
                         y=column_box[1],
                         w=column_box[2],
                         h=column_box[3])

    def on_focus_out(self, event):
        event.widget.destroy()

    def on_enter_pressed(self, event):
        new_text = event.widget.get()

        # Such as I002
        selected_iid = event.widget.editing_item_iid

        # Such as -1 (tree column), 0 (first self defined column), etc.
        column_index = event.widget.editing_column_index

        if column_index == -1:
            self.item(selected_iid, text=new_text)
        else:
            curret_values = self.item(selected_iid).get("values")
            curret_values[column_index] = new_text
            self.item(selected_iid, values=curret_values)

        event.widget.destroy()

# end TreeviewEdit