import os
import time
import datetime
import sys
import shutil
def main(path=sys.path[0], days=2, size=4096):
    paths = [path+"\\"+"Archive", path+"\\"+"Small",path+"\\"]
    if os.path.isdir(path):
        flagAchive = False
        flagSmall = False
        if not os.path.isdir(paths[0]):
            flagAchive = True
        if not os.path.isdir(paths[1]):
            flagSmall = True
        files = os.listdir(path)
        data = datetime.datetime.today()
        for i in files:
            if os.path.isfile(paths[2]+i) and data-datetime.datetime.fromtimestamp(os.path.getmtime(paths[2]+i))>=datetime.timedelta(days=days):
                if flagAchive:
                    os.mkdir(paths[0])
                    flagAchive=False
                shutil.copy(paths[2]+i, paths[0]+"\\"+i)
            if os.path.isfile(paths[2]+i) and os.path.getsize(paths[2]+i)<=size:
                if flagSmall:
                    os.mkdir(paths[1])
                    flagSmall=False
                shutil.copy(paths[2]+i, paths[1]+"\\"+i)
    else:
        print("Директории по заданному пути не существует", path)
if __name__ =="__main__":
    if len(sys.argv)==7 and sys.argv[1] == "--source" and sys.argv[3] == "--days" and sys.argv[5] == "--size":
        main(sys.argv[2], int(sys.argv[4]), int(sys.argv[6]))
    else:
        print("Error. Example:\n reorganize --source \"C:\\TestDir\" --days 2 --size 4096")
