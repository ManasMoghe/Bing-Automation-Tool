import subprocess
import pyautogui
import time
import datetime
import os
import sys
import pygetwindow as gw
import random

def is_edge_window_open():
    windows = gw.getAllWindows()
    for win in windows:
        if "Edge" in win.title and win.visible:
            return True
    return False

now = datetime.datetime.now()
today = now.date().isoformat()

start_time = now.replace(hour=6, minute=0, second=0, microsecond=0)
end_time = now.replace(hour=23, minute=59, second=59, microsecond=0)

if not (start_time <= now <= end_time):
    print("Outside allowed time window (6 AM - 11:59 PM). Exiting.")
    sys.exit()

last_run_file = os.path.join(os.path.dirname(__file__), "last_run.txt")
if os.path.exists(last_run_file):
    with open(last_run_file, "r") as f:
        last_run_date = f.read().strip()
    if last_run_date == today:
        print("Already ran today. Exiting.")
        sys.exit()

with open(last_run_file, "w") as f:
    f.write(today)

queries_file = os.path.join(os.path.dirname(__file__), "search_queries.txt")

if not os.path.exists(queries_file):
    print("search_queries.txt not found. Exiting.")
    sys.exit()

with open(queries_file, "r", encoding="utf-8") as f:
    all_queries = [line.strip() for line in f if line.strip()]
search_queries = random.sample(all_queries, min(10, len(all_queries)))

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
profile_dir = ["Profile 2", "Profile 3"]
url1 = "https://rewards.bing.com/?form=edgepredeem"

for profile in profile_dir:
    subprocess.Popen([edge, f"--profile-directory={profile}"])
    time.sleep(5)

    for query in search_queries:
        if not is_edge_window_open():
            print("Edge window is closed. Exiting script.")
            sys.exit()

        pyautogui.click(x=753, y=51)
        time.sleep(1)
        try:
            pyautogui.write(query, interval=0.1)
        except pyautogui.FailSafeException:
            print("Mouse moved to corner. Script stopped for safety.")
            sys.exit()

        pyautogui.press('enter')
        time.sleep(5)

    subprocess.Popen([edge, url1])
