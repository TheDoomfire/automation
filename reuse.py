import psutil
from qbittorrent import Client


# Variables
torrent_client = Client("http://127.0.0.1:8080/") #Enable this in qbittorrent: Web User Interface (Remote Control)
torrent_login = "admin", "adminadmin" # Dont know if this can work.
torrent_login_username = "admin"
torrent_login_password = "adminadmin"
torrent_program = "qbittorrent.exe"


def checkIfProcessRunning(processName): # Example: "chrome.exe"
    for proc in psutil.process_iter(): # Iterate over the all the running process
        try:
            if processName.lower() in proc.name().lower(): # Check if process name contains the given name string.
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def clearCompletedTorrents(): # Delete all completed torrents.
    if checkIfProcessRunning("qbittorrent.exe") == True:
        torrent_client.login("admin", "adminadmin")
        for item in torrent_client.torrents(filter="completed"):
            torrent_client.delete(item["hash"])