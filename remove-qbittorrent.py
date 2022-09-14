from qbittorrent import Client
from reuse import checkIfProcessRunning, clearCompletedTorrents


if checkIfProcessRunning("qbittorrent.exe") == True:
    print("qBittorrent is running.")
    clearCompletedTorrents
