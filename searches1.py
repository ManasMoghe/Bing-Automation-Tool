import subprocess
import pyautogui
import time
import datetime
import os

last_run_file = "last_run.txt"
today = datetime.date.today().isoformat()

if os.path.exists(last_run_file):
    with open(last_run_file, "r") as f:
        last_run_date = f.read().strip()
    if last_run_date == today:
        print("Already ran today. Exiting.")
        exit()

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

