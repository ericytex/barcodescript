from datetime import date
import datetime
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # A file has been modified
        pass

# Set up the file system event handler
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='myrepo', recursive=True)
observer.start()


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Add the modified file to the staging area
        subprocess.Popen(["git", "add", event.src_path], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, cwd="myrepo", universal_newlines=True, close_fds=True)

        # Create a commit with a unique timestamp as the commit message
        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        subprocess.Popen(["git", "commit", "--message", f"Changes at {timestamp}"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, cwd="myrepo", universal_newlines=True, close_fds=True)
