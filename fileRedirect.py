from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

downloads="C:\\Users\\danme\\Downloads"
pic=(".png",".jpg",".jpeg",".raw",".svg",".gif",".tiff",".JPG")
text=(".txt",".docx",".rtf",".doc")
video=(".mp4",".mov")
audio=(".mp3",".flac",".wav")
pdf=(".pdf",".eps")


class Handler(FileSystemEventHandler):
    def on_created(self,event):
        for fileName in os.listdir(downloads):
            index=fileName.rfind('.')
            ext=fileName[index:].lower()
            # print(ext)
            if ext in pic:
                os.rename(downloads+"\\"+fileName,downloads+"\\Pictures\\"+fileName)
            elif ext in pdf:
                os.rename(downloads+"\\"+fileName,downloads+"\\PDF\\"+fileName)
            elif ext in text:
                os.rename(downloads+"\\"+fileName,downloads+"\\Text\\"+fileName)
            elif ext in video:
                os.rename(downloads+"\\"+fileName,downloads+"\\Video\\"+fileName)
            elif ext in audio:
                os.rename(downloads+"\\"+fileName,downloads+"\\Audio\\"+fileName)


eventHandler= Handler()
observer = Observer()
observer.schedule(eventHandler,downloads,recursive=False)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
