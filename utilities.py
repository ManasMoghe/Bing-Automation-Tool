import datetime
import pygetwindow as gw
from paths import LOG_FILE

def log_to_console(console, msg):
    timestamp = datetime.datetime.now().strftime("[%H:%M:%S] ")
    console.insert('end', timestamp + msg + "\n")
    console.see('end')
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(timestamp + msg + "\n")

def is_edge_window_open():
    return any("Edge" in win.title and win.visible for win in gw.getAllWindows())
