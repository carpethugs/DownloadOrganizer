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
ppt=(".ppt",".pptx")
excel=(".xls",".xlsm",".xlsx")
zips=(".zip",".tar",".rar",".gz")


class Handler(FileSystemEventHandler):
    def on_created(self,event):
        for fileName in os.listdir(downloads):
            index=fileName.rfind('.')
            ext=fileName[index:]
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
            elif ext in ppt:
                os.rename(downloads+"\\"+fileName,downloads+"\\PowerPoint\\"+fileName)
            elif ext in excel:
                os.rename(downloads+"\\"+fileName,downloads+"\\Excel\\"+fileName)
            elif ext in zips:
                os.rename(downloads+"\\"+fileName,downloads+"\\Zip\\"+fileName)



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
