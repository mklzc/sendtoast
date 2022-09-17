"""
Note:
Use Command "nohup" to run in the background like:
nohup python -u toast.py > toast.log 2>&1 &
use Command "jobs" to check whether it is running successfully.
If you like, you can change the message to any with a higher invisibility.
"""
import requests
import platform
import os
import time
if platform.system() != "Linux":
    print("Program can only run in linux system.")
    exit(0)
last = 2
url = "http://192.168.1.1:10086/query"
def ChangeLog(data):
    print("{} changed status to {} in {}".format(data["ip"], data["isComing"], data["time"]))
def Check(Last, Now, Who):
    if Last == 1 and Now == 0:
        os.system('notify-send "No one is around"')
        return True
    if Last == 0 and Now == 1:
        message = Who + " is coming"
        os.system('notify-send ' + '"' + message + '"')
        return True
    return False
while True:
    time.sleep(0.1)
    data = requests.get(url).json()
    if Check(last, data["isComing"], data["who"]) == True:
        ChangeLog(data)
    last = data["isComing"]