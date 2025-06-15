import subprocess
import pyautogui
import time

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
subprocess.Popen(edge_path)

time.sleep(5)

pyautogui.click(x=400, y=50)

time.sleep(0.5)

pyautogui.write("weather today", interval=0.1)

pyautogui.press('enter')
