import subprocess
import pyautogui
import time
import datetime
import os
import sys

now = datetime.datetime.now()
today = now.date().isoformat()

start_time = now.replace(hour=6, minute=0, second=0, microsecond=0)
end_time = now.replace(hour=23, minute=59, second=59, microsecond=0)

if not (start_time <= now <= end_time):
    print("Outside allowed time window (6 AM - 11:59 PM). Exiting.")
    sys.exit()

if os.path.exists(last_run_file):
    with open(last_run_file, "r") as f:
        last_run_date = f.read().strip()
    if last_run_date == today:
        print("Already ran today. Exiting.")
        sys.exit()

with open(last_run_file, "w") as f:
    f.write(today)

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
profile_dir = ["Profile 2","Profile 3"]
url1 = f"https://rewards.bing.com/?form=edgepredeem"

search_queries = ["weather today", "news headlines", "coding tutorials","youtube","drgon ball","naruto","kamehameha","instinct","brain","bmw"]

for i in profile_dir:
    subprocess.Popen([edge,f"--profile-directory={i}"])
    
    time.sleep(5)
    
    for i in search_queries:
        pyautogui.click(x=753, y=51)
        
        time.sleep(1)
        
        pyautogui.write(i, interval=0.1)
        pyautogui.press('enter')
        
        time.sleep(5)
    
    subprocess.Popen([edge,url1])

