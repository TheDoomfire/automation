import requests
import re
from qbittorrent import Client
import sys, string, os
import psutil


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
    return False;

def movie_download():
   if checkIfProcessRunning("qbittorrent.exe") == False:
      os.popen(r"D:\Installed\Programs\qBittorrent\qbittorrent.exe")
      
   #Enable this in qbittorrent: Web User Interface (Remote Control)
   torrent_client = Client("http://127.0.0.1:8080/")
   torrent_client.login("admin", "adminadmin")

   movie_name = movie['name'].strip()
   movie_name = movie_name.replace(" ", "%20")
   movie_name = movie_name.replace("[", "%5B")
   movie_name = movie_name.replace("]", "%5D")
   movie_name = movie_name.replace(":", "%3A")

   trackers = "&tr=udp://tracker.cyberia.is:6969/announce&tr=udp://tracker.port443.xyz:6969/announce&tr=http://tracker3.itzmx.com:6961/announce&tr=udp://tracker.moeking.me:6969/announce&tr=http://vps02.net.orel.ru:80/announce&tr=http://tracker.openzim.org:80/announce&tr=udp://tracker.skynetcloud.tk:6969/announce&tr=https://1.tracker.eu.org:443/announce&tr=https://3.tracker.eu.org:443/announce&tr=http://re-tracker.uz:80/announce&tr=https://tracker.parrotsec.org:443/announce&tr=udp://explodie.org:6969/announce&tr=udp://tracker.filemail.com:6969/announce&tr=udp://tracker.nyaa.uk:6969/announce&tr=udp://retracker.netbynet.ru:2710/announce&tr=http://tracker.gbitt.info:80/announce&tr=http://tracker2.dler.org:80/announce"
   magnet = "magnet:?xt=urn:btih:"
   movie_magnet = magnet + movie['info_hash'] + "&dn=" + movie_name + trackers

   torrent_client.download_from_link(movie_magnet)
   #print("Downloading: " + movie['name'])


def format_movies(movie_name):
   file_name, all_trash = re.split("19\d\d|20\d\d|\(", movie_name, maxsplit=1)
   file_name = file_name.replace(".", " ")
   file_name = file_name.replace(":", "")
   file_name = file_name.replace("-", "")
   file_name = file_name.replace("{", "")
   file_name = file_name.replace("}", "")
   file_name = file_name.replace("\n", "")
   file_name = file_name.replace(" +", " ")
   file_name = re.sub("\s\s+", " ", file_name)
   file_name = file_name.strip()
   formatted_movie = file_name.lower()
   return formatted_movie


def dublicates():
      for i in range(len(movie_list)):
       if movie_list[i] == format_movies(movie['name']):
         istrue = True
         break
      else:
         istrue = False
      return istrue

#NOT IN USE
#Check in list if find_this exists.
def is_true(the_list, find_this):
   for i in range(len(the_list)):
      if the_list[i] == find_this:
        istrue = True
        break
      else:
         istrue = False
      return istrue

def trusted_user():
   if movie['status'] == 'vip' or 'trusted':
      is_trusted = True
   else:
      is_trusted = False
   return(is_trusted)


blocked_list = ["cam","hqcam", "hdcam", "hdts", "hindi", "aac", "720", "telesync"]
movie_list = [  ]
url_movies = "https://apibay.org/precompiled/data_top100_207.json"
json_data = requests.get(url_movies).json()

with open('movie_data.txt', 'r+') as f:
    movie_list = [movie_lists.rstrip() for movie_lists in f]
    for movie in json_data:
        if not any(blocked in movie['name'].lower() for blocked in blocked_list) and len(format_movies(movie['name'])) > 2 and dublicates() is False and movie['seeders'] > 2000 and trusted_user() is True:
            f.write(format_movies(movie['name']) + "\n")
            movie_list.append(format_movies(movie['name']))
            movie_download()

# Maybe: and len(format_movies(movie['name'])) > 2
# Is not needed anymore.