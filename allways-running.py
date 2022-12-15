import psutil
import subprocess
import os, signal


# VLC media player
# Kill flux.exe if vlc.exe is running.

# Works.
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def killProccess(processName):
    try:
        os.system("taskkill /im " + processName)
        print("Killed: " + processName)
    except:
        print("ERROR: " + processName + " sadly survived.")


# killProccess("vlc.exe")