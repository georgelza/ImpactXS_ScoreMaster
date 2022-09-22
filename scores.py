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
#   Created     	:   0.0.1 - 22 September 2022
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

import uuid
import json
import os

import settings

my_logger       = settings.my_logger
debuglevel      = settings.debuglevel

def load_all_scores(main_window):

    if debuglevel >= 1:
        my_logger.info('{time}, scores.load_all_scores Called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # ...

    if debuglevel >= 1:
        my_logger.info('{time}, scores.load_all_scores Completed'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

# end load_all_scores