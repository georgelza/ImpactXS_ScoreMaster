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

import logging
from api.apputils import *

def init():

    global my_logger
    global my_event_list
    global my_shooter_list

    global debuglevel
    global loglevel
    global appname
    global splashtime
    global currentRowIndex
    global filename


    # Our List of fields for the event and then a lists of shooters...
    # collpsed into one json structure in the file.
    my_event_list       = []
    my_shooter_list     = []

    config_params = getAppEnvVariables()

    # Read/Define Environment variables
    config_params   = getAppEnvVariables()
    loglevel        = config_params["loglevel"]
    splashtime      = config_params["splashtime"]
    debuglevel      = config_params["debuglevel"]
    appname         = "ImpactXS - ScoreMaster"

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
        my_logger.info('{time}, INFO LEVEL Activated'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    elif loglevel == 'DEBUG':
        my_logger.setLevel(logging.DEBUG)
        my_logger.debug('{time}, DEBUG LEVEL Activated'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    elif loglevel == 'CRITICAL':
        my_logger.setLevel(logging.CRITICAL)
        my_logger.critical('{time}, CRITICAL LEVEL Activated'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    # end DEBUGLEVEL

    if debuglevel >= 1:
        print_config(config_params, my_logger)

#end init