import os
from subprocess import check_output
import time

SCREEN_NAME = "DISCOVERY_RUNNER"


def run( filename ):
    cmd = f'screen -dmSL {SCREEN_NAME} python {filename} > blog'
    os.system( cmd )


def stop():
    cmd = "screen -X -S " + SCREEN_NAME + " quit"
    os.system( cmd )


def stop_all():
    os.system( "killall screen" )


def is_running():
    var = check_output( [ "screen -ls; true" ], shell=True )
    if f'.{SCREEN_NAME}\t(' in var.decode():
        return True
    else:
        return False

# stop_all()

# run("tester.py")

# while True:
#    if is_running():
#        print("Running\n")
#    else:
#	print("Not Running\n")
