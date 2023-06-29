@ECHO OFF
:: Can make "vlc" work but need enviroment variables.
:: vlc --playlist-enqueue "D:\Videos\Series\Black Monday\Black.Monday.S01.COMPLETE.720p.AMZN.WEBRip.x264-GalaxyTV[TGx]\*.mp4"

:: START "" "C:\Program Files\VideoLAN\VLC\vlc.exe" --enqueue "D:\Downloads\2 - Torrents\Lost (2004) Season 2 S02 + Extras (1080p BluRay x265 HEVC 10bit AAC 5.1 Silence)\*.mp4"

START "" "C:\Program Files\VideoLAN\VLC\vlc.exe" --playlist-autostart --playlist-tree "D:\Downloads\2 - Torrents\Lost (2004) Season 2 S02 + Extras (1080p BluRay x265 HEVC 10bit AAC 5.1 Silence)\*.mp4"
PAUSE
EXIT