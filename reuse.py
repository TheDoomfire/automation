import psutil
from qbittorrent import Client


# Variables
torrent_client = Client("http://127.0.0.1:8080/") #Enable this in qbittorrent: Web User Interface (Remote Control)
torrent_login = "admin", "adminadmin"
torrent_login_username = "admin"
torrent_login_password = "adminadmin"
torrent_program = "qbittorrent.exe"


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName. 
    Example "qbittorrent.exe"
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


def clearCompletedTorrents(): # Delete all completed torrents.
    if checkIfProcessRunning("qbittorrent.exe") == True:
        torrent_client.login("admin", "adminadmin")
        for item in torrent_client.torrents(filter="completed"):
            torrent_client.delete(item["hash"])