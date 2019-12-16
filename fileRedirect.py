from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

downloads="C:\\Users\\danme\\Downloads\\"
pic=(".png",".jpg",".jpeg",".raw",".svg",".gif",".tiff",".JPG")
text=(".txt",".docx",".rtf",".doc")
video=(".mp4",".mov")
audio=(".mp3",".flac",".wav")
pdf=(".pdf",".eps")
ppt=(".ppt",".pptx")
excel=(".xls",".xlsm",".xlsx")
zips=(".zip",".tar",".rar",".gz")
code=(".py",".java",".c",",.circ",".jar",".class")


class Handler(FileSystemEventHandler):
    def on_created(self,event):
        for fileName in os.listdir(downloads):
            index=fileName.rfind('.')
            ext=fileName[index:]
            if ext in pic:
                rename_test(downloads+fileName,downloads+"Pictures\\"+fileName)
            elif ext in pdf:
                rename_test(downloads+fileName,downloads+"PDF\\"+fileName)
            elif ext in text:
                rename_test(downloads+fileName,downloads+"Text\\"+fileName)
            elif ext in video:
                rename_test(downloads+fileName,downloads+"Video\\"+fileName)
            elif ext in audio:
                rename_test(downloads+fileName,downloads+"Audio\\"+fileName)
            elif ext in ppt:
                rename_test(downloads+fileName,downloads+"PowerPoint\\"+fileName)
            elif ext in excel:
                rename_test(fileName,fileName,downloads+"Excel\\"+fileName)
            elif ext in zips:
                rename_test(fileName,fileName,downloads+"Zip\\"+fileName)
            elif ext in code:
                rename_test(fileName,fileName,downloads+"code\\"+fileName)
    

def rename_test(oldName,newName):
    try:
        os.rename(oldName,newName)
    except FileExistsError:
        rename_test(oldName,newName+" Copy")


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