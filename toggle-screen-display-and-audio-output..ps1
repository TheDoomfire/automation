Set-DisplayResolution -DeviceName "DISPLAY1" -Width 1920 -Height 1080 -Frequency 60 -BitsPerPel 32

# Duplicate
Set-DisplayResolution -DeviceName "DISPLAY1" -Duplicate

# Extend
Set-DisplayResolution -DeviceName "DISPLAY1" -Extend

# Second screen only
Set-DisplayResolution -DeviceName "DISPLAY2" -Width 1920 -Height 1080 -Frequency 60 -BitsPerPel 32

# 1 = TV
# 2 = Main Display
# 3 = Right display

# TODO

# Toggle between:
# Extend screen 1 + 2
# Dublicate 1 + 2

# If dublicate = true
# Change output device to TV



