import json
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Scrollbar
import uuid


def load_shooters():
    with open("c:\\YOUTUBE\\python\\scoreMaster\\events\\20220901_shooters.json","r") as fh:
        my_shooter_list = json.load(fh)
    fh.close
    return my_shooter_list

def open_popup(root):
    child = Toplevel(root);
    child.geometry("768x500");
    child.title="Shooters";
    #child.grap_set();

    
    child.configure(bg='LightBlue');
    load_form = True;
    id_value = StringVar()
    id_value.set(uuid.uuid4())

    input_frame = LabelFrame(child, text='Shooter Profile',
                                bg="lightgray",
                                font=('Consolas',14))

    input_frame.grid(row=0,rowspan=6,column=0)

    l1 = Label(input_frame, text="ID",         width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
    l2 = Label(input_frame, text="First Name", width=25, height=2, anchor="w", relief="ridge", font=('Consolas',14))
   
    crm_id=Label(input_frame,   anchor="w",     height=1,
                relief="ridge", textvariable=id_value,      
                font=('Consolas',14))

    crm_id.grid(row=0, column=1, padx=20)

    crm_fn      =Entry(input_frame,width=30,borderwidth=2,
                    fg="black",font=('Consolas',14))

    crm_fn.grid(row=1, column=1)
    load_form = False;