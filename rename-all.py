from genericpath import exists
import os
import re # regular expressions
import shutil
from os.path import isfile, join
from pathlib import Path
import reuse
#from reuse import formatName


#downloads_path = str(Path.home() / "Downloads")
folder_path = str(Path.home() / "Downloads" / "Torrents")
os.chdir(folder_path)

year_pattern = "((18|19|20|21)[0-9]{2})"
hd_pattern = "(480|720|1080)"

#print(formatName("hej.dsfj."))

def format_folder(x):
    findyear = re.findall(year_pattern,x)
    if findyear:
        year = findyear[0][0]
        print(year)
    #hej, rest = re.split(year_pattern, x, maxsplit=1)


def rename_all():
    for i in os.listdir(folder_path):
        if os.path.isdir(i):
            print("dir: ", i)
            format_folder(i)


rename_all()