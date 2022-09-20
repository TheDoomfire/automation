from genericpath import exists
import os
import re # regular expressions
import shutil
from os.path import isfile, join
from pathlib import Path
import reuse
from reuse import formatName


#downloads_path = str(Path.home() / "Downloads")
folder_path = str(Path.home() / "Downloads" / "Torrents")
os.chdir(folder_path)

pattern_anyfile = "\.[^\\]+$"

#print(formatName("hej.dsfj."))

# next(os.walk('.'))[1]
#os.listdir(folder_path)
def rename_all():
    for i in os.listdir(folder_path):
        if os.path.isdir(i):
            print("dir: ", i)


rename_all()