########################################################################################################################
#
#
#  	Project     	: 	ImpactXS ScoreMaster
#
#   File            :   apputils.py
#
#	By              :   George Leonard ( georgelza@gmail.com )
#
#   Created     	:   25 Mar 2022
#
#   Changelog       :   See bottom
#
#   Notes       	:
#
#######################################################################################################################
__author__      = "George Leonard"
__email__       = "georgelza@gmail.com"
__version__     = "0.0.1"


import os, socket, uuid, sys, json, time
from datetime import datetime


#
# Get all the application generic/common variables from the environment settings set in the .run_socket_switch.bsh file
#
def getAppEnvVariables():

    Params = dict()

    Params['debuglevel']                = int(os.environ.get("DEBUGLEVEL"))
    Params['loglevel']                  = os.environ.get("LOGLEVEL")
    Params['splash_time']                = int(os.environ.get("SPLASH_TIME"))

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


# Generate a 15 digit uuid
def gen_endToEndId():

    txnid = str(uuid.uuid4().hex)[:15]

    print('{time}, Assigned {txnid}'.format(
        time=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
        txnid=txnid))

    sys.stdout.flush()
    return txnid

#end gen_endToEndId

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

def print_config(config_params, my_logger):

    DEBUGLEVEL = config_params["debuglevel"]

    if DEBUGLEVEL >= 1:
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
        my_logger.info('**')
        my_logger.info('*******************************************')

    # end if DEBUGLEVEL >= 1:

#end print_config()