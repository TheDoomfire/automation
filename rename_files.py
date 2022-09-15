import os
import re # regular expressions
from os.path import isfile, join
from pathlib import Path



# TODO
# If movie? folder contains
# Check if folder contains movie extentions
# Create a regular expressions to see if the text matches a movie name.

# Extentions
video_ext = [".mp4", ".mkv", ".avi", ".webm", ".wmv", ".3g2", ".3gp", ".flv", ".h264", ".m4v", ".mov", ".mpg", ".mpeg", ".rm", ".swf", ".vob"]
audio_ext = [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"]
compressed_ext = [".7z", ".rar", ".arj", ".deb", ".pkg", ".rpm", ".tar.gz", ".z", ".zip"]
text_ext = [".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wpd"]


# Folder to find files from.
downloads_path = str(Path.home() / "Downloads")
video_path = str(Path.home() / "Videos")
series_path = video_path + "\\" + "Series"
# os.listdir(downloads_path)
# os.path.isdir(path) # Check if its a folder or file.


# Regular Expressions (RE) Patterns
serie_pattern = re.compile(".*((s|S)+[0-9]{2}(e|E)+[0-9]{2}).*(480|720|1080|2160).*")
movie_pattern = re.compile(".*((18|19|20|21)[0-9]{2}).*(480|720|1080|2160).*")


# .title() makes every word strt with a big letter.
def formatName(name):
    formattedName = name.strip()
    formattedName = formattedName.replace(".", " ")
    formattedName = formattedName.replace("   ", " ")
    formattedName = formattedName.replace("  ", " ")
    formattedName = formattedName.replace("-", " ")
    formattedName = formattedName.title()
    return formattedName


def makeDir(folderpath):
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)


# Check if Series
def series():
    for i in os.listdir(downloads_path):
        if i.endswith(tuple(video_ext)):
            if os.path.getsize(downloads_path + "\\" + i) < 400000000: # If its bigger than about 400mb, maybe will remove this later.
                if serie_pattern.match(i):
                    print("Serie: "+i)
                    serieSplit = re.split("((s|S)+[0-9]{2}(e|E)+[0-9]{2})", i, maxsplit=1)
                    print(formatName(serieSplit[0]))
                    makeDir(series_path)
                    makeDir(series_path + "\\" + formatName(serieSplit[0]))
                    tempvar = re.search("((s|S)+[0-9]{2})", i)[0]
                    tempvar = tempvar.replace("s", "")
                    tempvar = tempvar.replace("S", "")
                    if tempvar[0] == "0":
                        tempvar = tempvar[1:]
                    print(tempvar)


def sorterThis(ext, pattern, maxbyte=0, path=downloads_path): # A list of Extentions, regex Pattern. maxbytes??
    for i in os.listdir(path):
        if i.endswith(tuple(ext)) and pattern.match(i):
            print("hej! " + i)
            if not maxbyte == 0:
                print(maxbyte)


""" sorterThis(video_ext, serie_pattern)
sorterThis(video_ext, movie_pattern) """


series()
print(series_path)