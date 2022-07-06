import os
import re
import urllib
import requests
from bs4 import BeautifulSoup

my_path = r"C:\Users\Emma_\Downloads\Torrents"

movie_extension = [".mkv", ".mp4"]

subtitle_extension = [".srt", ".src"]

my_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
headers = {"User-Agent" : my_useragent}

myarray = os.listdir(my_path)

#print(myarray)

series = ["s01", "s02", "s03"]
#if any(serie in movie_name.lower() for serie in series):

def format_movies_for_download(movie_name):
    if any(serie in movie_name.lower() for serie in series):
        file_name, all_trash = re.split("s\d\de\d\d", movie_name.lower(), maxsplit=1)
        if "s01" in movie_name.lower():
            season = "-first-season"
        if "s02" in movie_name.lower():
            season = "-second-season"
        if "s03" in movie_name.lower():
            season = "-third-season"
    else:
        file_name, all_trash = re.split("19\d\d|20\d\d|\(", movie_name, maxsplit=1)
        season = ""
    file_name = file_name.replace(".", " ")
    file_name = file_name.strip()
    file_name = file_name.replace(" ", "-")
    file_name = file_name.replace(":", "")
    file_name = file_name.replace("{", "")
    file_name = file_name.replace("}", "")
    file_name = file_name.replace("\n", "")
    file_name = file_name.replace(" +", " ")
    file_name = re.sub("\s\s+", " ", file_name)
    file_name = file_name.strip()
    formatted_movie = file_name.lower() + season
    return formatted_movie
   

def subtitle_file_exist():
    for folder_item in folder:
        if folder_item.endswith(tuple(subtitle_extension)):
            subtilte_true = True
        else:
            subtilte_true = False
        return(subtilte_true)


def remove_extention(movie_name):
    file_name, extension = re.split(".mkv|.avi|.mp4", movie_name.lower(), maxsplit=1)
    file_name = file_name.strip()
    return(file_name)


#Not Done.
def download_movie_subtitle(movie_name):
    url = requests.get("https://www.subscene.com/subtitles/" + format_movies_for_download(movie_name) + "/english", headers=headers)
    print(format_movies_for_download(movie_name))
    soup = BeautifulSoup(url.content, features="lxml")
    #find_link = soup.find_all("a", "span"=re.compile(remove_extention(movie_name)))
    a_tags = soup.find("span", string="Who.Is.America.S01E02")
    print(a_tags)


for item in myarray:
    folder = os.listdir(my_path + "\\" + item)
    if subtitle_file_exist() == True:
        print("Subtitle already exist")
    else:
        for folder_item in folder:
            if folder_item.endswith(tuple(movie_extension)):
                #print(format_movies(folder_item))
                #print(remove_extention(folder_item))
                download_movie_subtitle(folder_item)
"""             if not folder_item.endswith(tuple(subtitle_extension)):
                print(folder) """