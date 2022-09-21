from genericpath import exists
import os
import re # regular expressions
import shutil
from os.path import isfile, join
from pathlib import Path
#import reuse
from reuse import formatName


#downloads_path = str(Path.home() / "Downloads")
#folder_path = str(Path.home() / "Downloads" / "Torrents")
folder_path = "D:\\Videos\\Movies"
os.chdir(folder_path)


year_pattern = "((18|19|20|21)[0-9]{2})"
hd_pattern = "(480|720|1080)"

#print(formatName("hej.dsfj."))

def format_folder(x):
    findyear = re.findall(year_pattern,x)
    findhd = re.findall(hd_pattern,x)
    old_x = x
    year = None
    hd = None
    if findyear:
        year = findyear[0][0]
        x = re.split(year_pattern, x, maxsplit=1)
    if findhd:
        hd = findhd[0]
        if not findyear:
            x = re.split(hd_pattern, x, maxsplit=1)
            x = formatName(x[0])    
    if not findyear:
        x = formatName(x)
    else:
        x = formatName(x[0])
    if year is not None:
        x = x + " " + "(" + year + ")"
    if hd is not None:
        x = x + " " + "[" + hd + "p]"
    return x
    #x[0]
    
    #hej, rest = re.split(year_pattern, x, maxsplit=1)


# To Do:
# MMake not 
def rename_all():
    for i in os.listdir(folder_path):
        if os.path.isdir(i):
            old_path = folder_path + "\\" + i
            new_path = folder_path + "\\" + format_folder(i)
            if not old_path == new_path and not os.path.exists(new_path):
                os.rename(old_path, new_path)


rename_all()
print(folder_path)