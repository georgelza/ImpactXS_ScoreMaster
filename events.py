########################################################################################################################
#
#
#  	Project     	: 	ScoreMaster
#
#
#   File            :   events.py
#
#	By              :   George Leonard ( georgelza@gmail.com )

#
#   Created     	:   0.0.1 - 5 Mar 2023
#
#   Changelog       :   0.0.1 -
#
#
#   Notes       	:   https://www.youtube.com/watch?v=en7ZlbcW0X4
#
########################################################################################################################
__author__      = "George Leonard"
__email__       = "georgelza@gmail.com"
__version__     = "0.0.1"

import settings
from datetime import datetime


my_logger       = settings.my_logger
debuglevel      = settings.debuglevel


# register functions to be called for a event.
def register_events(event: str, function: callable):

    if debuglevel >= 1:
        my_logger.info('{time}, events.register_events.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    handlers = settings.events.get(event)

    if handlers is None:
        settings.events[event] = [function]

    else:
        handlers.append(function)

    if debuglevel >= 2:
        my_logger.info('{time}, events.register_events.We re going to call {function} when {event} is dispatched/called'.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
            function=function,
            event=event
        ))

    if debuglevel >= 1:
        my_logger.info('{time}, events.register_events.Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

#end register_events


# Dispatch, call functions as registered for the function name = event
def dispatch(event: str):

    if debuglevel >= 1:
        my_logger.info('{time}, events.dispatch.Called '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

    handlers = settings.events.get(event)

    if handlers != None:
        for handler in handlers:
            if debuglevel >= 2:
                my_logger.info(
                    '{time}, events.dispatch.Handler {handler} being called'.format(
                        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                        handler=handler
                    ))
            handler()

    if debuglevel >= 1:
        my_logger.info('{time}, events.dispatch.Completed '.format(
            time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        ))

#end dispatch