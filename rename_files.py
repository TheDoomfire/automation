import os
import re # regular expressions
from os.path import isfile, join
from pathlib import Path



# TODO
# If movie? folder contains
# Check if folder contains movie extentions
# Create a regular expressions to see if the text matches a movie name.


# https://en.wikipedia.org/wiki/Video_file_format
video_ext = [".mp4", ".mkv", ".avi", ".webm", ".wmv"]
downloads_path = str(Path.home() / "Downloads")
# os.listdir(downloads_path)


# Need to work for:
# Batman.v.Superman.Dawn.of.Justice.2016.BLABLABLA-XDAWEFFF
# Eye.in.the.Sky.2015.1080p.BluRay
# Eye.in.the.Sky.2015.bla.bla.720.blueray
# [19|20]+[\d\d]   [720|1080]  [sS]+[\d|\d\d]
serie_pattern = re.compile(r"abc")


""" pattern = re.compile("^([A-Z][0-9]+)+$")
pattern.match(string) """


""" def fileRenamer():
    var = 1 """


# Check if Series
def series():
    for i in os.listdir(downloads_path):
        if i.endswith(tuple(video_ext)):
            if os.path.getsize(downloads_path + "\\" + i) < 400000000: # If its bigger than about 400mb, maybe will remove this later.
                print(i)


series()