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
                checkFileExists(fileName,fileName,downloads+"\\Pictures\\")
            elif ext in pdf:
                checkFileExists(fileName,fileName,downloads+"\\PDF\\")
            elif ext in text:
                checkFileExists(fileName,fileName,downloads+"\\Text\\")
            elif ext in video:
                checkFileExists(fileName,fileName,downloads+"\\Video\\")
            elif ext in audio:
                checkFileExists(fileName,fileName,downloads+"\\Audio\\")
            elif ext in ppt:
                checkFileExists(fileName,fileName,downloads+"\\PowerPoint\\")
            elif ext in excel:
                checkFileExists(fileName,fileName,downloads+"\\Excel\\")
            elif ext in zips:
                checkFileExists(fileName,fileName,downloads+"\\Zip\\")
    

def checkFileExists(original,fileName,folder):
    if fileName in os.listdir(folder):
        checkFileExists(original,"Copy Of "+fileName,folder)
    else:
        os.rename(downloads+"\\"+original,folder+fileName)




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
