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
__author__  = "George Leonard"
__email__   = "georgelza@gmail.com"
__version__ = "0.0.1"

from datetime import datetime
from tkinter import filedialog as fd
from tkinter import ttk
import tkinter as tk
from io import BytesIO

import logging
import os, socket, uuid, sys, json, time

import xlsxwriter

def init():


    global first_start_mode
    global my_event_list
    global my_qualifying_target_list
    global my_finals_target_list
    global my_shooter_list
    global my_logger

    global appname
    global debuglevel
    global loglevel
    global echojson
    global splashtime
    global score_viewer
    global auto_refresh
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
    first_start_mode            = True
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
    auto_refresh        = config_params["auto_refresh"]

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


def load_event_json_from_file(file):
    global my_event_list
    global my_event_image
    global my_qualifying_target_list
    global my_finals_target_list
    global my_shooter_list
    global first_start_mode

    if debuglevel >= 1:
        my_logger.info('{time}, event.load_event_json_from_file.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

        my_logger.info('{time}, event.load_event_json_from_file.Loading file: {file}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=file
        ))

    try:
        with open(file, "r") as fh:
            my_event_list               = json.load(fh)
            my_event_image              = my_event_list["image"]
            my_qualifying_target_list   = my_event_list["qualifying"]
            my_finals_target_list       = my_event_list["final"]
            my_shooter_list             = my_event_list["shooters"]
            first_start_mode            = False

        if debuglevel >= 2:
            my_logger.info('{time}, event.load_event_json_from_file.File Loaded, global variables refreshed '.format(
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
        fh.close
        if debuglevel >= 1:
            my_logger.info('{time}, event.load_event_json_from_file.File Closed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        if debuglevel >= 2 and echojson == 1:
            my_logger.info('{time}, event.load_event_json_from_file.Printing global dictionaries'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

            print("------ Event                 ------")
            pp_json(my_event_list)

            print("------ Qualifying Target's   ------")
            pp_json(my_qualifying_target_list)

            print("------ Finals Target's       ------")
            pp_json(my_finals_target_list)

            print("------ Shooters              ------")
            pp_json(my_shooter_list)

            print("-----------------------------------")

        if debuglevel >= 1:
            my_logger.info('{time}, event.load_event_json_from_file.Completed '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        return my_event_list

# end load_event_json_from_file


def getAppEnvVariables():

    Params = dict()

    Params['debuglevel']                = int(os.environ.get("DEBUGLEVEL"))
    Params['loglevel']                  = os.environ.get("LOGLEVEL")
    Params['echojson']                  = int(os.environ.get("ECHOJSON"))
    Params['splashtime']                = int(os.environ.get("SPLASHTIME"))
    Params['score_viewer']              = os.environ.get('SCORE_VIEWER')
    Params["auto_refresh"]              = int(os.environ.get("AUTOREFRESH"))

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
        my_logger.info('**    AUTO_REFRESH          : ' + str(config_params['auto_refresh']))
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


# Find shooter in array of shooters (my_shooter_list) based on guid_value
def find_row_in_my_shooter_list(guid_value):

    global my_shooter_list      # Global variable, list of shooters

    if debuglevel >= 2:
        my_logger.info('{time}, settings.find_row_in_my_shooter_list Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    row     = 0
    found   = False

    for rec in my_shooter_list:
        if rec["id"] == guid_value:
            found = True
            break
        row = row + 1

    if (found == True):
        if debuglevel >= 2:
            my_logger.info('{time}, settings.find_row_in_my_shooter_list.Completed Shooter:{row} '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                row=row
            ))

        return (row)

    else:
        if debuglevel >= 2:
            my_logger.info('{time}, settings.find_row_in_my_shooter_list.Completed Shooter:NOT FOUND '.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        return (-1)

#end find_row_in_my_shooter_list


def update_shooter(myfile, my_shooter):

    if debuglevel >= 2:
        my_logger.info('{time}, settings.update_shooter.Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    row                     = find_row_in_my_shooter_list(my_shooter["id"])
    my_shooter_list[row]    = my_shooter
    save_event(myfile)

    if debuglevel >= 2:
        my_logger.info('{time}, settings.update_shooter.Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))
# end save_shooter


def save_event(myfile):

    global my_event_list
    global my_qualifying_list
    global my_final_list
    global my_shooter_list
    global event_mode

    if debuglevel >= 2:
        my_logger.info('{time}, settings.save_event.Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    if event_mode == "Initial_Event_Save":
        myfile      = file_dialog("Initial_Event_Save")
        event_mode  = "Load_Event"

    my_event_list["qualifying"] = my_qualifying_target_list
    my_event_list["final"]      = my_finals_target_list
    my_event_list["shooters"]   = my_shooter_list

    if debuglevel >= 2:
        my_logger.info('{time}, settings.save_event.Event data reassembled'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    save_json_to_file(myfile, my_event_list)

    if debuglevel >= 2:
        my_logger.info('{time}, settings.save_event.Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end save_event


def save_json_to_file(myfile, my_event):

    if debuglevel >= 2:
        my_logger.info('{time}, settings.save_json_to_file.Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    try:
        if myfile:
            with open(myfile, "w") as file_handler:

                json.dump(my_event, file_handler, indent=4)

                if debuglevel >= 2:
                    my_logger.info('{time}, settings.save_json_to_file.File Saved'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                    ))
        else:
            if debuglevel >= 2:
                my_logger.info('{time}, settings.save_json_to_file.No target file defined. File Save Aborted!!! '.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

    except IOError as e:
        my_logger.error('{time}, settings.save_json_to_file.I/O error: {file}, {errno}, {strerror}"'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=filename,
            errno=e.errno,
            strerror=e.strerror
        ))

    except:  # handle other exceptions such as attribute errors
        my_logger.error('{time}, settings.save_json_to_file.Unexpected error: {file}, {error}"'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=filename,
            error=sys.exc_info()[0]
        ))


    finally:
        try:
            file_handler.close
            if debuglevel >= 2:
                my_logger.info('{time}, settings.save_json_to_file.File closed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))
        finally:
            if debuglevel >= 2:
                my_logger.info('{time}, settings.save_json_to_file.Completed'.format(
                    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                ))

#end save_json_to_file

def save_json_to_excelfile(filename):

    global my_event_list
    global my_qualifying_list
    global my_final_list
    global my_shooter_list

    sheet               = my_event_list["distance"]
    my_qualifying_list  = my_event_list["qualifying"]
    my_final_list       = my_event_list["final"]
    my_shooter_list     = my_event_list["shooters"]

    qColRoot            = 9
    qRowRoot            = 3
    fColRoot            = 22
    fRowRoot            = 3
    shooterDataRoot     = fRowRoot + 7

    if debuglevel >= 2:
        my_logger.info('{time}, settings.save_json_to_excelfile.Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    try:

        # Open file
        workbook = xlsxwriter.Workbook(filename)
        if debuglevel >= 2:
            my_logger.info('{time}, settings.save_json_to_excelfile.Workbook opened {workbook}'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                workbook=filename
            ))

        worksheet = workbook.add_worksheet(sheet)
        if debuglevel >= 2:
            my_logger.info('{time}, settings.save_json_to_excelfile.Worksheet Added'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        # Write to Excel

        # King Image
        img_name = my_event_list["image"]
        file = open("images/"+img_name, 'rb')
        data = BytesIO(file.read())
        file.close()
        worksheet.insert_image('A1', filename, {'image_data': data, 'x_scale': 0.25, 'y_scale': 0.25})

        # Impact Image
        img_name = "impactxs.png"
        file = open("images/"+img_name, 'rb')
        data = BytesIO(file.read())
        file.close()
        worksheet.insert_image('D1', filename, {'image_data': data, 'x_scale': 0.2, 'y_scale': 0.35})


        # https://xlsxwriter.readthedocs.io/format.html#set_num_format
        cell_bold_format = workbook.add_format({'bold': True, 'font_color': 'red'})
        # or
        #cell_bold_format.set_bold()
        #cell_bold_format.set_font_color('red')

        # => Headers
        worksheet.write(qRowRoot + 0, qColRoot - 1, my_event_list["start_date"] + " -> " + my_event_list["end_date"])
        worksheet.write(qRowRoot + 1, qColRoot - 1, my_event_list["name"])
        worksheet.write(qRowRoot + 2, qColRoot - 1, "Target Size: (mm)", cell_bold_format)
        worksheet.write(qRowRoot + 3, qColRoot - 1, "Meter:", cell_bold_format)
        worksheet.write(qRowRoot + 4, qColRoot - 1, "Yards:", cell_bold_format)

        # Create a format to use in the merged range.
        red_merge_format = workbook.add_format({
            'bold': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_color': 'red'
        })

        blck_merge_format = workbook.add_format({
            'bold': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_color': 'black'
        })

        s1 = '{sc}{row}:{ec}{row}'.format(sc=xlsxwriter.utility.xl_col_to_name(1), ec=xlsxwriter.utility.xl_col_to_name(2), row=fRowRoot + 6)
        s2 = '{sc}{row}:{ec}{row}'.format(sc=xlsxwriter.utility.xl_col_to_name(3), ec=xlsxwriter.utility.xl_col_to_name(4), row=fRowRoot + 6)
        s3 = '{sc}{row}:{ec}{row}'.format(sc=xlsxwriter.utility.xl_col_to_name(5), ec=xlsxwriter.utility.xl_col_to_name(6), row=fRowRoot + 6)
        s4 = '{sc}{row}:{ec}{row}'.format(sc=xlsxwriter.utility.xl_col_to_name(7), ec=xlsxwriter.utility.xl_col_to_name(8), row=fRowRoot + 6)

        worksheet.merge_range(s1, "PLACE", red_merge_format)
        worksheet.merge_range(s2, "SHOOTER", red_merge_format)
        worksheet.merge_range(s3, "SPOTTER", red_merge_format)
        worksheet.merge_range(s4, "CALIBRE", red_merge_format)

        x = 0
        while x < int(my_qualifying_list["no_of_targets"]):
            if my_qualifying_list["target_list"][x]["target_no"] == 0:
                worksheet.write(qRowRoot + 2, qColRoot, my_qualifying_list["target_list"][x]["target_size"])
                worksheet.write(qRowRoot + 3, qColRoot, f'{(my_qualifying_list["target_list"][x]["distance"] * 0.9144):.0f}')
                worksheet.write(qRowRoot + 4, qColRoot, str(my_qualifying_list["target_list"][x]["distance"]))
                worksheet.write(qRowRoot + 5, qColRoot, "CB", cell_bold_format)

            else:
                sc = qColRoot + 1+(int(my_qualifying_list["no_of_shots"]) * (x-1))
                ec = sc + int(my_qualifying_list["no_of_shots"])-1
                start_col = xlsxwriter.utility.xl_col_to_name(sc)
                end_col = xlsxwriter.utility.xl_col_to_name(ec)

                s1 = '{sc}{row}:{ec}{row}'.format(sc=start_col, ec=end_col, row=qRowRoot + 3)
                s2 = '{sc}{row}:{ec}{row}'.format(sc=start_col, ec=end_col, row=qRowRoot + 4)
                s3 = '{sc}{row}:{ec}{row}'.format(sc=start_col, ec=end_col, row=qRowRoot + 5)
                s4 = '{sc}{row}:{ec}{row}'.format(sc=start_col, ec=end_col, row=qRowRoot + 6)

                worksheet.merge_range(s1, my_qualifying_list["target_list"][x]["target_size"], blck_merge_format)
                worksheet.merge_range(s2, f'{(my_qualifying_list["target_list"][x]["distance"] * 0.9144):.0f}', blck_merge_format)
                worksheet.merge_range(s3, str(my_qualifying_list["target_list"][x]["distance"]), blck_merge_format)
                worksheet.merge_range(s4, "T" + str(my_qualifying_list["target_list"][x]["target_no"]), red_merge_format)

            x += 1
        # end while

        y = 0
        while y < int(my_final_list["no_of_targets"]):
            sc = fColRoot + (int(my_final_list["no_of_shots"]) * y)
            ec = sc + int(my_final_list["no_of_shots"]) - 1
            start_col = xlsxwriter.utility.xl_col_to_name(sc)
            end_col = xlsxwriter.utility.xl_col_to_name(ec)

            s1 = '{sc}{row}:{ec}{row}'.format(sc=start_col, ec=end_col, row=qRowRoot + 3)
            s2 = '{sc}{row}:{ec}{row}'.format(sc=start_col, ec=end_col, row=qRowRoot + 4)
            s3 = '{sc}{row}:{ec}{row}'.format(sc=start_col, ec=end_col, row=qRowRoot + 5)
            s4 = '{sc}{row}:{ec}{row}'.format(sc=start_col, ec=end_col, row=qRowRoot + 6)

            worksheet.merge_range(s1, my_final_list["target_list"][y]["target_size"], blck_merge_format)
            worksheet.merge_range(s2, f'{(my_final_list["target_list"][y]["distance"] * 0.9144):.0f}', blck_merge_format)
            worksheet.merge_range(s3, str(my_final_list["target_list"][y]["distance"]), blck_merge_format)
            worksheet.merge_range(s4, "T" + str(my_final_list["target_list"][y]["target_no"] + int(my_qualifying_list["no_of_targets"])), red_merge_format)

            y += 1
        # end while

        worksheet.write(fRowRoot + 5, fColRoot + (int(my_final_list["no_of_shots"]) * (y-1))+int(my_final_list["no_of_shots"]), "SCORE", cell_bold_format)

        # =>  Shooter / Score Data
        fShooters = len(my_shooter_list)
        a = 0
        while a < fShooters:
            qscores = my_shooter_list[a]["scores"]["qualifying"]
            fscores = my_shooter_list[a]["scores"]["final"]
            total = my_shooter_list[a]["scores"]["total_score"]

            shooterDataRow = shooterDataRoot + a
            print("Shooter Data ", a, " ",shooterDataRow)

            s1 = '{sc}{row}:{ec}{row}'.format(sc=xlsxwriter.utility.xl_col_to_name(qColRoot - 8), ec=xlsxwriter.utility.xl_col_to_name(qColRoot - 8 + 1), row=shooterDataRow)
            s2 = '{sc}{row}:{ec}{row}'.format(sc=xlsxwriter.utility.xl_col_to_name(qColRoot - 6), ec=xlsxwriter.utility.xl_col_to_name(qColRoot - 6 + 1), row=shooterDataRow)
            s3 = '{sc}{row}:{ec}{row}'.format(sc=xlsxwriter.utility.xl_col_to_name(qColRoot - 4), ec=xlsxwriter.utility.xl_col_to_name(qColRoot - 4 + 1), row=shooterDataRow)
            s4 = '{sc}{row}:{ec}{row}'.format(sc=xlsxwriter.utility.xl_col_to_name(qColRoot - 2), ec=xlsxwriter.utility.xl_col_to_name(qColRoot - 2 + 1), row=shooterDataRow)

            worksheet.merge_range(s1, "")
            worksheet.merge_range(s2, my_shooter_list[a]["first_name"] + " " + my_shooter_list[a]["last_name"])
            worksheet.merge_range(s3, my_shooter_list[a]["spotter"])
            worksheet.merge_range(s4, my_shooter_list[a]["equipment"]["rifle"]["caliber"])

            print("qScores ", a, " ", shooterDataRow)

            ColInc = 0
            # Qualifying scores
            for score in qscores:
                for shots in score["shots"]:
                    worksheet.write(shooterDataRow-1, qColRoot + ColInc, shots["hit_miss"])
                    ColInc += 1
                #end for
            #end for

            print("fScores ", a, " ",shooterDataRow)

            # Final Scores
            for score in fscores:
                for shots in score["shots"]:
                    worksheet.write(shooterDataRow-1, qColRoot + ColInc, shots["hit_miss"])
                    ColInc += 1
                #end for
            #end for

            # Total Score
            worksheet.write(shooterDataRow-1, qColRoot + ColInc, total)

            a += 1
        # end while

        if debuglevel >= 2:
            my_logger.info('{time}, settings.save_json_to_excelfile.Worksheet writes completed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

        # => Footers


    except:  # handle other exceptions such as attribute errors
        my_logger.error('{time}, settings.save_json_to_excelfile.Unexpected error: {file}, {error}"'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=filename,
            error=sys.exc_info()[0]
        ))

    finally:
        # Close file
        workbook.close()
        if debuglevel >= 2:
            my_logger.info('{time}, settings.save_json_to_excelfile.Worksheet Closed'.format(
                time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            ))

    if debuglevel > 2:
        pp_json(my_event_list)

    if debuglevel >= 2:
        my_logger.info('{time}, settings.save_json_to_excelfile.Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

#end save_json_to_excelfile

# Refresh data in memory from file (include updating global settings variable),
# shooters include their personal data,
# equipment and scores
def load_all_shooter_scores_json_from_file(filename):

    global my_event_list
    global my_shooter_list

    if debuglevel >= 1:
        my_logger.info('{time}, settings.load_all_shooter_scores_json_from_file.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # Refreshes my_event_list structure from file
    my_event_list = load_event_json_from_file(filename)

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


# Open/Select file dialog box
def file_dialog(mode):

    filetypes = (
        ('json files', '*.json'),
        ('Excel files', '*.xlsm'),
        ('All files', '*.*')
    )

    if debuglevel >= 1:
        my_logger.info('{time}, settings.file_dialog.Called, Mode: ({mode})'.format(
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

    elif mode == "Save_to_Excel":
        filetypes = (
            ('Excel files', '*.xlsx'),
        )

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
            my_logger.info('{time}, settings.file_dialog.Completed File: {file}'.format(
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

def get_target_distance(target_number, mode):

    if debuglevel >= 1:
        my_logger.info('{time}, settings.get_target_distance.Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    if mode == "qual":
        target_list = my_qualifying_target_list["target_list"]

    else:
        target_list = my_finals_target_list["target_list"]

    distance = target_list[target_number]["distance"]

    if debuglevel >= 2:
        my_logger.info('{time}, settings.get_target_distance Mode: {mode}, Distance: {distance}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            mode=mode,
            distance=distance
        ))

    if debuglevel >= 1:
        my_logger.info('{time}, settings.get_target_distance.Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    return distance

# end get_target_distance

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