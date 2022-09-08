########################################################################################################################
#
#
#  	Project     	: 	ImpactXS - ScoreMaster
#   URL             :   http://www.impactxs.co.za
#
#                   :   Bredan Fike
#   eMail           :   brendan@impactxs.co.za
#
#   File            :   main.py
#
#	By              :   George Leonard ( georgelza@gmail.com )
#
#   Created     	:   0.0.1 - 5 September 2022
#
#   Changelog       :   0.0.1 - 8 Jul 2022
#
#
#   Notes       	:
#                   :   Menu bar :          https://www.pythontutorial.net/tkinter/tkinter-menu/
#                   :   Scott's Examples :  https://www.youtube.com/watch?v=cuIjKMPRn0k
#                   :   JSONLint :          https://jsonlint.com
#
########################################################################################################################
__author__      = "George Leonard"
__email__       = "georgelza@gmail.com"
__version__     = "0.0.1"

from api.apputils import *
import logging
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import Shooters
import Event
import uuid

global my_logger
global DEBUGLEVEL
global myevent_list
global myshooter_list
global currentRowIndex
global my_data_list

# Our lists.... Possible collapse into one list.
myevent_list    = []
myshooter_list  = []
my_data_list    = []

# Read/Define Environment variables
config_params   = getAppEnvVariables()
DEBUGLEVEL      = config_params["debuglevel"]
LOGLEVEL        = config_params["loglevel"]
SPLASH_TIME     = config_params["splash_time"]
App_Name        = "ImpactXS - ScoreMaster"

# Logging Handler
logging.root.handlers = []
FORMAT = '%(levelname)s :%(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT)

# create logger
my_logger = logging.getLogger(__name__)

# Set Logging level
if LOGLEVEL == 'INFO':
    my_logger.setLevel(logging.INFO)
    my_logger.info('{time}, INFO LEVEL Activated'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

elif LOGLEVEL == 'DEBUG':
    my_logger.setLevel(logging.DEBUG)
    my_logger.debug('{time}, DEBUG LEVEL Activated'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

elif LOGLEVEL == 'CRITICAL':
    my_logger.setLevel(logging.CRITICAL)
    my_logger.critical('{time}, CRITICAL LEVEL Activated'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

# end DEBUGLEVEL


############## LETS Start ##############
my_logger.info('{time}, --------------------------------------------------'.format(
    time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
))


### Build the SplashScreen

# Create object
splash_root = Tk()

# Adjust size
splash_root.geometry("1000x600")

# Set Title
splash_root.title(App_Name)

# Read the Image
image = Image.open("images/1mile.png")
# Resize the image using resize() method
resize_image1 = image.resize((350, 350))
img1 = ImageTk.PhotoImage(resize_image1)
# create label and add resize image
label1 = Label(image=img1)
label1.image = img1
label1.place(x=0, y=0)

# Read the Image
image = Image.open("images/2mile.png")
# Resize the image using resize() method
resize_image2 = image.resize((350, 350))
img2 = ImageTk.PhotoImage(resize_image2)
# create label and add resize image
label2 = Label(image=img2)
label2.image = img2
label2.place(x=650, y=0)

# Read the Image
image = Image.open("images/impactxs.png")
# Resize the image using resize() method
resize_impactxs = image.resize((1000, 125))
impactxs = ImageTk.PhotoImage(resize_impactxs)
# create label and add resize image
labelimpactxs = Label(image=impactxs)
labelimpactxs.image = impactxs
labelimpactxs.place(x=0, y=450)

# Finish Building Splash screen


# Our Functions
def exitProgram():
    my_logger.info('{time}, exitProgram Called '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))
    exit()

# end exitProgram


def main():
    global my_logger
    global main_window

    my_logger.info('{time}, Main Starting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    # destroy splash window
    splash_root.destroy()

    # As we're destroying the above TK object we happy to create a new one, otherwise we'de use TopLevel()
    # Execute tkinter
    root = Tk()
    root.state("zoomed")

    # Adjust size
    root.geometry("600x400")

    # Set Title
    root.title(App_Name)
    root.iconbitmap("images/impactxs_ico.jpg")

    # Lets Build the Menu Structure
    menu = Menu(root)
    root.config(menu=menu)
    fileMenu = Menu(menu, tearoff=0)

    # Open file dialog, allowing user to select 1 Mile or 2 Mile Template
    fileMenu.add_command(label="New Event", command=newEvent)

    # Open file dialog allowing user to select event file
    fileMenu.add_command(label="Load Event", command=loadEvent)

    # Load all shooters as per the event file loaded into Treeview, if it is a new event with no shooters open
    # empty treeview, with only Add button enabled
    fileMenu.add_command(label="Shooters...", command=load_all_shooters)

    # #1 Load the shooters and scores into treeview
    # #2 if auto update is selected, disable edit mode, allow user to select Qualify or Final as the order, initiate
    # auto refresh, for now every 10 seconds, change to refresh when shooter score is updated,
    fileMenu.add_command(label="Scores...")

    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exitProgram)
    menu.add_cascade(label="File", menu=fileMenu)

    helpMenu = Menu(menu, tearoff=0)
    helpMenu.add_command(label="Welcome")
    helpMenu.add_command(label="About...")
    menu.add_cascade(label="Help", menu=helpMenu)

    fileMenu.bind("")
    main_window = root

# end main

# Open/Select file dialog box
def select_file(mode):

    global myfile

    my_logger.info('{time}, select_file Starting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    filetypes = (
        ('json files', '*.json'),
        ('All files', '*.*')
    )

    # Determine where we running, as template and events are by default subdirectories of the App directory.
    directory = os.getcwd()
    my_logger.info('{time}, Current App Directory {directory}'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
        directory=directory
    ))

    if mode == "new":
        # We're creating a new event, so lets present a event template.
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir=directory + '/template',
            filetypes=filetypes)
    else:
        #we're opening a previous defined event, so lets show saved events from ./events folder as default.
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir=directory + '/events',
            filetypes=filetypes)

    if filename:
        my_logger.info('{time}, File Selected: {file}'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            file=filename
        ))
        myfile = filename
        return filename
    else:
        my_logger.info('{time}, Aborted, No File Selected'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end select_file


def newEvent():
    global my_logger
    global DEBUGLEVEL
    global myevent_list
    global main_window

    my_logger.info('{time}, newEvent Starting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    # Popup file open window, allowing user to select 1Mile or 2 Mile event.json template file
    filename = select_file("new")
    if filename:
        myevent_list = Event.load_event_data(filename, my_logger, DEBUGLEVEL)
        myevent_list["uuid"] = str(uuid.uuid4())
        Event.open_event_screen(main_window, myevent_list, my_logger, DEBUGLEVEL)

# end newEvent


def loadEvent():
    global my_logger
    global DEBUGLEVEL
    global myevent_list
    global main_window

    my_logger.info('{time}, loadEvent Starting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    filename = select_file("")
    if filename:
        myevent_list = Event.load_event_data(filename, my_logger, DEBUGLEVEL)
        Event.open_event_screen(main_window, myevent_list, my_logger, DEBUGLEVEL)

# end loadEvent


# We will add the scores via the File/scores menu.
# For now ust build Scott's Treeview and user editor, then replace with my data.
def load_all_shooters():
    global main_window
    global trv
    global myevent_list

    global my_logger
    global DEBUGLEVEL

    child = Toplevel(main_window)
    child.geometry("1200x700")
    child.title = "Events"

    my_logger.info('{time}, load_all_shooters Starting '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    # Determine where we running, as template and events are by default subdirectories of the App directory.
    directory = os.getcwd()
    my_logger.info('{time}, Current App Directory {directory}'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
        directory=directory
    ))

    my_logger.info('{time}, load_all_shooters Entering '.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    ))

    def make_new_record():
        #rifleTuple = ('','','','','','','')
        #scopeTuple = ('','','','')
        #cartridgeTuple = ('','','','','','')
        #equipmentTuple = (rifleTuple, scopeTuple, cartridgeTuple)
        #blankTuple = ('', '', '', '', '', '', '', '', equipmentTuple)
        blankTuple = ('', '', '', '', '', '', '', '','','')
        open_popup('add', blankTuple, child)

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

    # Reload all shooters from myfile into my_data_list
    def load_json_from_file():
        global my_data_list
        global myfile

        with open(myfile, "r") as file_handler:
            my_data = json.load(file_handler)
            my_data_list = my_data["shooters"]
            pp_json(my_data_list)

        file_handler.close
        print('file has been read and closed')

    def remove_all_data_from_trv():
        for item in trv.get_children():
            trv.delete(item)

    # Reload trv with all shooters data
    def load_trv_with_json():
        global my_data_list

        remove_all_data_from_trv()

        rowIndex = 1

        for key in my_data_list:
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

    def MouseButtonUpCallBack(event):
        global trv
        currentRowIndex = trv.selection()[0]
        lastTuple = (trv.item(currentRowIndex, 'values'))
        open_popup('edit', lastTuple, child)

    def open_popup(_mode, _tuple, primary):
        global myname

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

        def child_cancel():
            child.grab_release()
            child.destroy()
            child.update()

        def reload_main_form():
            load_trv_with_json()

        def change_background_color(new_color):
            crm_fn.config(bg=new_color)
            crm_ln.config(bg=new_color)
            crm_id_number.config(bg=new_color)
            crm_cellphone.config(bg=new_color)
            crm_email.config(bg=new_color)
            crm_spotter.config(bg=new_color)

        def add_entry():
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

        def update_entry():
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

        def load_edit_field_with_row_data(_tuple):
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

        if _mode == 'edit':
            load_edit_field_with_row_data(_tuple)

        def process_request(command_type, guid_value, first_name, last_name, id_number, cell_phone, email, spotter, equipment, scores):
            global my_data_list
            global dirty

            dirty = True

            if command_type == "_UPDATE_":
                row = find_row_in_my_data_list(guid_value)
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

                    my_data_list[row] = dict

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

                my_data_list.append(dict)

            elif command_type == "_DELETE_":
                row = find_row_in_my_data_list(guid_value)
                if row >= 0:
                    del my_data_list[row]

            save_json_to_file()
            clear_all_fields()

        def find_row_in_my_data_list(guid_value):
            global my_data_list
            row = 0
            found = False

            for rec in my_data_list:
                if rec["id"] == guid_value:
                    found = True
                    break
                row = row + 1

            if (found == True):
                return (row)

            return (-1)

        def determineAction():
            if load_form == False:
                if _mode == "edit":
                    update_entry()
                else:
                    add_entry()

            reload_main_form()
            child.grab_release()
            child.destroy()
            child.update()

        def save_json_to_file():
            global my_data_list
            global myevent_list
            global myfile

            with open(myfile, "w") as file_handler:
                myevent_list["shooters"] = my_data_list
                json.dump(myevent_list, file_handler, indent=4)

            file_handler.close
            print('file has been written to and closed')

        def load_json_from_file():
            global my_data_list
            global myevent_list
            global myfile

            with open(myfile, "r") as file_handler:
                myevent_list = json.load(file_handler)
                my_data_list = myevent_list["shooters"]

            file_handler.close
            print('file has been read and closed')

        def clear_all_fields():
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

    trv.bind("<ButtonRelease>", MouseButtonUpCallBack)
    load_json_from_file()
    load_trv_with_json()

# end load_all_shooters

# Set the Splash screen Interval
splash_root.after(SPLASH_TIME, main)

# Execute tkinter program
mainloop()