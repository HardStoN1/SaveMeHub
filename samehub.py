import sys
import os

PATH = sys.argv[1] # Gets the file path
_dic = {}

print(str(PATH))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def work_on_file(fileName, filePath):
    try:
        os.chdir(PATH)
        os.system("git add " + fileName)
        os.system("git commit -m " + "\"" + "secondary commit" + "\"")
        os.system("git push origin master")
    except Exception as e:
        print("Oops! -> " + str(e))

if sys.argv[2] != None:
    PATH += " " + sys.argv[2]

for fName in os.listdir(PATH):
    raw = PATH + "\\" + fName
    print(str(raw))
    _dic[fName] = raw

for key in _dic:
    fN = key
    fP = _dic[key]

    work_on_file(fN, fP)

print(f"{bcolors.OKGREEN}It saul goodman! All files has been saved and commited to your GitHub Reop!")



