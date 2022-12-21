from genericpath import exists, isdir
import os
import re # regular expressions
import shutil
from os.path import isfile, join
import os.path
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
switch_ext = [".nsp"]
gamecube_ext = [".rvz", ".wbfs", ".ciso"]
extracted_ext = [".7z", ".rar"]


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

episode_serie_patterns = ["((s|S)+[0-9]{2}(e|E)+[0-9]{2})", "((Season|season|SEASON).(\d\d|\d))", "((s|S)+[0-9]{2})"]
episode_serie_pattern = "(" + ")|(".join(episode_serie_patterns) + ")"


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


def remove_empty_folders(path_abs):
    #os.rmdir(path_abs)
    print("Running empty folders")
    #print(path_abs)
    #print(os.listdir(path_abs))
    for item in os.listdir(path_abs):
        #print(item)
        the_path = path_abs + "\\" + item
        #print(os.path.isdir(the_path))
        if os.path.isdir(the_path):
            #print(the_path)
            #print(os.path.isdir(the_path))
            if not os.listdir(the_path): # IF folder is EMPTY!
                #print(os.path.join(path_abs, item))
                os.removedirs(os.path.join(path_abs, item))
"""     walk = list(os.walk(path_abs))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.remove(path) """


# Get serie season then make it to a path.
def getSeriePath(i):
    serieSplit = re.split("((s|S)+[0-9]{2}(e|E)+[0-9]{2})", i, maxsplit=1)
    serieSeason = re.search("((s|S)+[0-9]{2})", i)[0]
    serieSeason = serieSeason.replace("s", "")
    serieSeason = serieSeason.replace("S", "")
    if serieSeason[0] == "0":
        serieSeason = serieSeason[1:]
    serie_season_path = series_path + formatName(serieSplit[0]) + "\\" + "Season " + serieSeason + "\\" 
    return serie_season_path
    #makeDir(series_path + "\\" + formatName(serieSplit[0]) + "\\" + "Season " + serieSeason)
    #shutil.move(downloads_path + "\\" + i, serie_season_path + "\\" + i)

# NOT DONE, MAY DELETE
def formatSeriePath(i):
    serieSplit = re.split("((s|S)+[0-9]{2}(e|E)+[0-9]{2})", i, maxsplit=1)
    serieSeason = re.search("((s|S)+[0-9]{2})", i)[0]
    serieSeason = serieSeason.replace("s", "")
    serieSeason = serieSeason.replace("S", "")
    if serieSeason[0] == "0":
        serieSeason = serieSeason[1:]
    serie_season_path = series_path + formatName(serieSplit[0]) + "\\" + "Season " + serieSeason + "\\" 
    return serie_season_path



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
    if re.findall(year_pattern, name):
        year = re.findall(year_pattern, name)
        year = year[0][0]
    else:
        year = None

    if re.findall(pixel_pattern, name):
        pixel = re.findall(pixel_pattern, name)
        pixel = pixel[0]
    else:
        pixel = None

    if re.findall(episode_serie_pattern, name):
        episode = re.findall(episode_serie_pattern, name)
        episode = episode[0]
        episode = list(filter(None, episode))
        episode = episode[0]
    else:
        episode = None

    if re.match(movie_pattern, name) and not re.match(main_serie_pattern, name):
        isMovie = True
        nameSplit = re.split(split_movie_pattern, name, maxsplit=1)
        name = nameSplit[0]
    else:
        isMovie = False

    if re.match(main_serie_pattern, name) and not re.match(movie_pattern, name):
        isSerie = True
        nameSplit = re.split(episode_serie_pattern, name, maxsplit=1)
        name = nameSplit[0]
    else:
        isSerie = False

    if not year == None and not pixel == None and isMovie == True:
        name = formatName(name) + " " + "(" + year + ")" + " " + "[" + pixel + "]"


    if isSerie == True and not pixel == None:
        name = formatName(name) + " " + episode.upper() + " " + "[" + pixel + "]"
    elif isSerie == True and pixel == None:
        name = formatName(name) + " " + episode.upper()

    #if not episode == None:
    #    name = episode
    return name


# Delete?
def formatSerieName(name):
    name = checkIfWebsite(name)
    if re.findall(year_pattern, name):
        year = re.findall(year_pattern, name)
        year = year[0][0]
    else:
        year = None

    if re.findall(pixel_pattern, name): # 720, 1080p etc.
        pixel = re.findall(pixel_pattern, name)
        pixel = pixel[0]
    else:
        pixel = None

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


""" def removeFolder(thePath):
    allFilesInFolder = thePath + "*"
    contentOfFolder = glob.glob(allFilesInFolder)
    for f in contentOfFolder:
        print(f)
        #os.remove(f)
    #os.remove(thePath)
    print(allFilesInFolder)
 """

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
        #print(dirs)
        for f in files:
            if f.endswith(tuple(video_ext)) and re.match(main_serie_pattern, f):
                if os.path.exists(series_path + getFolderName(root)):
                    print("Already Exists: ", series_path + getFolderName(root))
                    # If it already exists where I want to move it.
                else: # if File
                    if myPath == root: # If its a file
                        print("Hej ", root)
                        # shutil.move(root, series_path)
                    else: # if inside a folder.
                        newDestination = getSeriePath(f) + formatFileName(f)
                        makeDir(newDestination)
                        print("Moved: ", root)
                        print("To: ", newDestination)
                        isExists = os.path.exists(newDestination)
                        if not isExists: # Maybe should change this...
                            for file in os.listdir(root): # Dosent work if entire season is in the same folder.
                                oldDestination = root + "\\" + file
                                # print("HEJ: ", oldDestination)
                                shutil.move(oldDestination, newDestination)
                            #remove_empty_folders(root)
        try:
            for folder in dirs: # Need to make it look inside of folders.
                folder = myPath  + "\\" + folder
                #folder = os.path.join(myPath, folder)
                print(folder) # Dosent add subfolders on nested folders.
                # Error seems to skip looking at underlying
                for i in os.listdir(folder): # Get error: FileNotFoundError: [WinError 3] The system cannot find the path specified: 'D:\\Downloads\\2 - Torrents\\Nathan for You S00 Nathan on Your Side (240p re-tvrip)'
                    file = os.path.join(folder, i)
                    if os.path.isfile(file): # IF its a file. # ERROR: FileNotFoundError on directories!
                        print("ITEM: ", file)
                        # Not tried this code yet
                        newDestination = folder + formatFileName(file)
                        makeDir("New Destination: ", newDestination)
                        print(newDestination)
                        print("Moved: ", root)
                        print("To: ", newDestination)
                        #isExists = os.path.exists(newDestination)
        except:
            print("Error! Couldnt find a directory in dirs")
            hej = 1


"""                 elif os.path.isdir(folder):
                    print("DIR: ", file) """
            #for item in :


"""         for i in os.listdir(mypath):
            if i.endswith(tuple(video_ext)) and re.match(movie_pattern, i) and not re.match(main_serie_pattern, i):
                print(0)
            elif re.match(year_pattern, i):
                print(i) """

# ModuleNotFoundError: No module named 'psutil'
# clearCompletedTorrents()
movieSorter(downloads_path)
print("Running Python...")
testSeries(downloads_path)
#series()
remove_empty_folders(downloads_path)

print("Its Done.")
# TODO
# Sort series inside folders.

# NEED TO REMOVE ALL EMPTY FOLDERS