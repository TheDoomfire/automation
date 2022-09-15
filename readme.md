# Automate all PC stuff

## Install All Modules

1. pip install -r requirements.txt

If you going to work on this project.

## Subtitles

Check if any folder has a [movie file] and not a [subtitle file].
Download the Movie File


https://medium.com/byte-tales/python-script-to-download-subtitles-6371cef1d681

https://stackoverflow.com/questions/21018612/how-to-download-to-a-specific-directory

<table>, <tbody>, <tr>, <td class="a1">, <a>, second: <span>


for a_link in tbody > tr > td > a:
a_link(find_all(span)[1])

check every <a> tag has a <span>[1] that contains myString. then prints the href

### Resources

Test regex: https://pythex.org/

### TODO

**Downloader:**
1. Check if a movie is on https://subscene.com/browse/popular/film/1
1. Check IMDB rating, eng/swe language etc.
1. Download on TPB or other.
1. When download finished, move and sort. run clearCompletedTorrents()
1. Run Subtitle downloader.

**Sorter/renamer:**
1. Check if serie
1. Fix regex for serie.
1. Look inside folder and see if it contains a serie. DONT look inside temp folder.
1. If no .srt, download and place it in the same folder.
1. Format the serie name.
1. Change .srt to same name as serie.
1. Check if a serieName folder exist.
1. Move it.
1. Or create the correct season folder.
1. Move it to the correct folder.
1. Save the serie + episode to a database??? For auto-downloading new episodes??

If file make a folder and place both the serieFile + srt.
If no srt avaiable for download, make one with moviePy ????