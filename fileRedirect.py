from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

user="C:\\Users\\danme\\"
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
            ext=fileName[index:].lower()
            df=downloads+fileName
            if ext in pic:
                rename_test(df,user+"Pictures\\Downloaded\\"+fileName)
            elif ext in pdf:
                rename_test(df,downloads+"PDF\\"+fileName)
            elif ext in text:
                rename_test(df,downloads+"Text\\"+fileName)
            elif ext in video:
                rename_test(df,downloads+"Video\\"+fileName)
            elif ext in audio:
                rename_test(df,downloads+"Audio\\"+fileName)
            elif ext in pdf:
                rename_test(df,downloads+"PDF\\"+fileName)
            elif ext in ppt:
                rename_test(df,downloads+"PowerPoint\\"+fileName)
            elif ext in excel:
                rename_test(df,downloads+"Excel\\"+fileName)
            elif ext in zips:
                rename_test(df,downloads+"Zip\\"+fileName)
            elif ext in code:
                rename_test(df,downloads+"code\\"+fileName)
                        
            


def rename_test(oldName,newName):
    try:
        os.rename(oldName,newName)
    except FileExistsError:
        index=newName.rfind('.')
        ext=newName[index:].lower()
        rename_test(oldName,newName[:index]+" Copy"+ext)

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
