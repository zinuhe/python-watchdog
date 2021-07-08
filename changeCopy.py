# https://pythonhosted.org/watchdog/
# http://thepythoncorner.com/dev/how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/

# You can use pip to install watchdog quickly and easily:
# $ pip install watchdog
# Python3 -m pip install watchdog

# The following example program will monitor the current directory recursively for file system changes 
# and copy a specified changed file to another folder

# Python3 changeCopy.py

import time
import os, shutil, glob
import os.path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# File to watch
fileToWatch = "processPhotoVideoSony.py" #"*.py" #"*"

# Destination path to copy
#DESTINATION = "/Users/jimmysaavedra/Documents/DEV/Python/SourceCode/Watchdog/tmp/changeCopy.py"
DESTINATION = "/Users/jimmysaavedra/Documents/DEV/Python/DCIM_Jun-24/processPhotoVideoSony.py"

if __name__ == "__main__":
    patterns = [fileToWatch]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):
    print(f"-- {event.src_path} has been created")

def on_deleted(event):
    print(f"-- {event.src_path} was deleted")

def on_modified(event):
    #print(f"-- {event.src_path} has been modified")
    now = datetime.now()
    now = now.strftime("%d/%b/%Y %H:%M:%S")
    print(f"Copying... {now}")
    print(f"Src: {event.src_path}")
    print(f"Dst: {DESTINATION} \n")
    copyFile(event.src_path, DESTINATION)

def on_moved(event):
    print(f"-- {event.src_path} was moved to {event.dest_path}")


def copyFile(source, destination, symlinks=False, ignore=None):    
    #if os.path.isdir(source):
    # shutil.copytree(source, destination, symlinks, ignore)
    shutil.copy(source, destination)

# my_event_handler.on_created = on_created
# my_event_handler.on_deleted = on_deleted
# my_event_handler.on_moved = on_moved
my_event_handler.on_modified = on_modified

path = "."
go_recursively = False #True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()

