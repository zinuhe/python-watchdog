# https://pythonhosted.org/watchdog/
# http://thepythoncorner.com/dev/how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/

# You can use pip to install watchdog quickly and easily:
# $ pip install watchdog
# Python3 -m pip install watchdog


# The following example program will monitor the current directory recursively for file system changes 
# and copy a specified file changed to another folder

# Python3 changeCopy.py

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):
    print(f"-- {event.src_path} has been created")

def on_deleted(event):
    print(f"-- {event.src_path} was deleted")

def on_modified(event):
    print(f"-- {event.src_path} has been modified")

def on_moved(event):
    print(f"-- {event.src_path} was moved to {event.dest_path}")


my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved


path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)


my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()

