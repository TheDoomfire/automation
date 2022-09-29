from genericpath import exists, isdir
import os
import re # regular expressions
import shutil
from os.path import isfile, join
from pathlib import Path
import glob
from reuse import clearCompletedTorrents


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
#downloads_path = str(Path.home() / "Downloads")

# Use this instead of harddrive if u want.
# Path.home()
harddrive = "D:\\"
downloads_path = harddrive + "Downloads" + "\\" + "2 - Torrents"
video_path = harddrive + "Videos"
movie_video_path = video_path + "\\" + "Movies" + "\\"
series_path = video_path + "\\" + "Series" + "\\"
books_path = harddrive + "Dokument"
reports_path = books_path + "\\" + "Company Reports"


""" downloads_path = str(harddrive / "Downloads" / "2 - Torrents")
video_path = str(Path.home() / "Videos")
series_path = video_path + "\\" + "Series"
books_path = str(Path.home() / "Dokument")
reports_path = books_path + "\\" + "Company Reports" """
# os.listdir(downloads_path)
# os.path.isdir(path) # Check if its a folder or file.


# Regular Expressions (RE) Patterns
# (Season|season|SEASON).(\d\d|\d)
year_pattern = re.compile("((18|19|20|21)[0-9]{2})")
serie_pattern = re.compile(".*((s|S)+[0-9]{2}(e|E)+[0-9]{2}).*(480|720|1080|2160).*")
serie_pattern_two = re.compile(".*(Season|season|SEASON).(\d\d|\d).*")
main_serie_patterns = [".*((s|S)+[0-9]{2}(e|E)+[0-9]{2}).*(480|720|1080|2160).*", ".*(Season|season|SEASON).(\d\d|\d).*"]
main_serie_pattern = "(" + ")|(".join(main_serie_patterns) + ")"


website_pattern = re.compile("(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})")

report_patterns = [".*(arsredovisning|Arsredovisning|ARSREDOVISNING).*((18|19|20|21)[0-9]{2}).*",
"(annualreport|Annualreport|ANNUALREPORT).*((18|19|20|21)[0-9]{2})"]
report_pattern = "(" + ")|(".join(report_patterns) + ")"

#movie_pattern = re.compile(".*((18|19|20|21)[0-9]{2}).*(480|720|1080|2160).*")
movie_patterns = [".*((18|19|20|21)[0-9]{2}).*(480|720|1080|2160).*"]
movie_pattern = "(" + ")|(".join(movie_patterns) + ")"

split_movie_patterns = ["(480|720|1080|2160)", "((18|19|20|21)[0-9]{2})"]
split_movie_pattern = "(" + ")|(".join(split_movie_patterns) + ")"

pixel_pattern = re.compile("(480|720|1080|2160)")


def checkIfWebsite(x):
    if website_pattern.match(x):
        x = re.sub(website_pattern, "", x)
    return x


def formatName(name):
    if website_pattern.match(name):
        name = re.sub(website_pattern, "", name)
    formattedName = name.strip()
    formattedName = formattedName.replace(".", " ")
    formattedName = formattedName.replace("-", " ")
    formattedName = formattedName.replace("_", " ")
    formattedName = formattedName.replace("(", " ")
    formattedName = formattedName.strip()
    formattedName = re.sub(" +", " ", formattedName) # Regex remove ALL double or more whitespace.
    formattedName = formattedName.title() # Makes every word start with a big letter.
    return formattedName


# Not Done
def formatFileName(name):
    name = checkIfWebsite(name)
    year = re.findall(year_pattern, name)
    year = year[0][0]
    pixel = re.findall(pixel_pattern, name)
    pixel = pixel[0]
    if re.match(movie_pattern, name) and not re.match(main_serie_pattern, name):
        nameSplit = re.split(split_movie_pattern, name, maxsplit=1)
        name = nameSplit[0]
    if year and pixel:
        name = formatName(name) + " " + "(" + year + ")" + " " + "[" + pixel + "]"
    return name


def justPath(thePath):
    tempVar = thePath.rsplit("\\", 1)
    tempVar = tempVar[0] + "\\"
    return tempVar

def getFolderName(thePath):
    thePath = thePath.rsplit("\\", 1)
    return thePath[1]


def makeDir(folderpath):
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)


def getFileExtention(filename):
    emptyVar, file_extention = os.path.splitext(filename)
    return file_extention


def removeFolder(thePath):
    allFilesInFolder = thePath + "*"
    contentOfFolder = glob.glob(allFilesInFolder)
    for f in contentOfFolder:
        print(f)
        #os.remove(f)
    #os.remove(thePath)
    print(allFilesInFolder)


# Check if Series
def series():
    for i in os.listdir(downloads_path):
        if i.endswith(tuple(video_ext)):
            if os.path.getsize(downloads_path + "\\" + i): #400000000: # If its bigger than about 400mb, maybe will remove this later.
                if serie_pattern.match(i):
                    serieSplit = re.split("((s|S)+[0-9]{2}(e|E)+[0-9]{2})", i, maxsplit=1)
                    serieSeason = re.search("((s|S)+[0-9]{2})", i)[0]
                    serieSeason = serieSeason.replace("s", "")
                    serieSeason = serieSeason.replace("S", "")
                    if serieSeason[0] == "0":
                        serieSeason = serieSeason[1:]
                    serie_season_path = series_path + "\\" + formatName(serieSplit[0]) + "\\" + "Season " + serieSeason
                    makeDir(series_path + "\\" + formatName(serieSplit[0]) + "\\" + "Season " + serieSeason)
                    shutil.move(downloads_path + "\\" + i, serie_season_path + "\\" + i)
"""                     print(i)
                    print(serie_season_path) """


def seriesSecond(mypath):
    files = os.listdir(mypath)
    for item in files:
        if os.path.isdir(os.path.join(mypath, item)):
            seriesSecond(os.path.join(mypath, item))
        else:
            if item.endswith(tuple(video_ext)):
                print(os.path.join(mypath, item))


# Trying to make a standard for every file.
def sorterThis(ext, pattern, maxbyte=0, path=downloads_path): # A list of Extentions, regex Pattern. maxbytes??
    for i in os.listdir(path):
        if i.endswith(tuple(ext)) and pattern.match(i):
            isTrue = True
            if not maxbyte == 0:
                print(maxbyte)
    return(isTrue)


def annualreports():
    for i in os.listdir(downloads_path):
        if i.endswith(tuple(text_ext)):
            if re.match(report_pattern, i):
                reportSplit = re.split("(arsredovisning|Arsredovisning|ARSREDOVISNING)", i, maxsplit=1)
                yearSplit = re.split("((18|19|20|21)[0-9]{2})", i, maxsplit=1)
                print(formatName(reportSplit[0]), yearSplit[1])
                newPath = reports_path + "\\" + formatName(reportSplit[0]) + "\\" + yearSplit[1]
                #makeDir(newPath)
                #shutil.move(downloads_path + "\\" + i, newPath + "\\" + i)
                print(newPath)


""" movieSorter()
series()
annualreports() """
#seriesSecond(downloads_path)
#series()


def old():
    for i in os.listdir(downloads_path):
        if i.endswith(tuple(video_ext)) and re.match(movie_pattern, i):
            print(0)
        elif re.match(year_pattern, i):
            print(i)


# Bullet.Train.1080p.WEB-DL.DDP5.1.H.264-EVO[TGx]
# Dosent get moved!!!
def movieSorter(mypath):
    #files = os.listdir(mypath)
    hej = 1
    for root,dirs,files in os.walk(mypath):
        for file in files:
            if file.endswith(tuple(video_ext)) and re.match(movie_pattern, file) and not re.match(main_serie_pattern, file) and not hej == 2:
                if os.path.exists(movie_video_path + getFolderName(root)):
                    print("It already exists: ", movie_video_path + getFolderName(root))
                    print("Delete This: ", root + "\\")
                    #shutil.rmtree(root)
                else:
                    if mypath == root: # If its a file
                        newDestination = movie_video_path + formatFileName(file) + "\\"
                        oldDestination = root + "\\" + file
                        makeDir(newDestination)
                        shutil.move(oldDestination, newDestination)
                        print("File, Old: ", oldDestination) # TEMPORARLY
                        print("File, New: ",newDestination) # TEMPORARLY
                    else: # If its not a file
                        shutil.move(root, movie_video_path)
                        os.rename(movie_video_path + getFolderName(root), movie_video_path + formatFileName(file))
                        print("Folder, Old: ", root) # TEMPORARLY
                        print("Folder, New: ", movie_video_path + formatFileName(file)) # TEMPORARLY


def testSeries(myPath):
    for root,dirs, files in os.walk(myPath):
        for f in files:
            if f.endswith(tuple(video_ext)) and re.match(main_serie_pattern, f):
                if os.path.exists(series_path + getFolderName(root)):
                    print("Folder: ", root)
                else: # if File
                    if myPath == root: # If its a file
                        print("Hej ",root)
                        #shutil.move(root, series_path)
                    else:
                        print(root)


"""         for i in os.listdir(mypath):
            if i.endswith(tuple(video_ext)) and re.match(movie_pattern, i) and not re.match(main_serie_pattern, i):
                print(0)
            elif re.match(year_pattern, i):
                print(i) """


clearCompletedTorrents()
#movieSorter(downloads_path)
testSeries(downloads_path)