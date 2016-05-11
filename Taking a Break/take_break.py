import webbrowser
import time

breaks = 3
breaknum = 1
print("This script began running on: " + time.ctime())

while (breaknum<=breaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=F90Cw4l-8NY")
    breaknum += 1
