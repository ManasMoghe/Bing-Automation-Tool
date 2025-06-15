import subprocess, time, random, datetime, pyautogui, os
from paths import EDGE_PATH, PROFILE_DIRS, QUERIES_FILE, LAST_RUN_FILE, REWARDS_URL
from utilities import log_to_console, is_edge_window_open

import os

QUERIES_FILE = os.path.join(os.getcwd(), "search_queries.txt")


def run_script(console=None, force=False):
    try:

        if not EDGE_PATH:
            log_to_console(console, "Microsoft Edge not found. Please install Edge or update EDGE_PATH in paths.py.")
            return
        
        now = datetime.datetime.now()
        today = now.date().isoformat()

        if not force:
            start_time = now.replace(hour=6, minute=0, second=0)
            end_time = now.replace(hour=23, minute=59, second=59)
            if not (start_time <= now <= end_time):
                log_to_console(console, "Outside allowed time window (6 AM - 11:59 PM).")
                return

            if os.path.exists(LAST_RUN_FILE):
                with open(LAST_RUN_FILE, "r") as f:
                    if f.read().strip() == today:
                        log_to_console(console, "Already ran today. Use 'Force Run' if needed.")
                        return

        with open(LAST_RUN_FILE, "w") as f:
            f.write(today)

        if not os.path.exists(QUERIES_FILE):
            log_to_console(console, "search_queries.txt not found.")
            return

        with open(QUERIES_FILE, "r", encoding="utf-8") as f:
            all_queries = [line.strip() for line in f if line.strip()]

        if len(all_queries) < 10:
            log_to_console(console, f"Not enough queries available. Found: {len(all_queries)}")
            return

        used_queries = set()
        total_needed = 10 * len(PROFILE_DIRS)

        if len(all_queries) < total_needed:
            log_to_console(console, f"Not enough queries for all profiles. Needed: {total_needed}, Available: {len(all_queries)}")
            return

        random.shuffle(all_queries)

        for profile in PROFILE_DIRS:
            log_to_console(console, f"Launching Edge with profile: {profile}")
            #subprocess.Popen([EDGE_PATH, f"--profile-directory={profile}"])
            subprocess.Popen([EDGE_PATH])
            time.sleep(5)

            profile_queries = []
            while len(profile_queries) < 10 and all_queries:
                query = all_queries.pop()
                if query not in used_queries:
                    used_queries.add(query)
                    profile_queries.append(query)

            for i,query in enumerate(profile_queries):
                if not is_edge_window_open():
                    log_to_console(console, "Edge window closed. Exiting.")
                    return
            
                pyautogui.hotkey('ctrl', 't')
                time.sleep(1)
                
                try:
                    pyautogui.write(query, interval=0.1)
                except pyautogui.FailSafeException:
                    log_to_console(console, "Fail-safe triggered. Exiting.")
                    return
                pyautogui.press('enter')
                log_to_console(console, f"Searched: {query}")
                time.sleep(3)

            subprocess.Popen([EDGE_PATH, REWARDS_URL])
            log_to_console(console, "Finished profile session.")

        log_to_console(console, "🏁 Script completed.")
    except Exception as e:
        log_to_console(console, f"Unexpected error: {e}")
