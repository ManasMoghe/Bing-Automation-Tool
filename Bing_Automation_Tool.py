import tkinter as tk
from tkinter import scrolledtext
import threading
from automation import run_script
from utilities import log_to_console

running = False

def threaded_run(console, force=False):
    global running
    if running:
        log_to_console(console, "Script already running.")
        return
    running = True
    btn_run.config(state=tk.DISABLED)
    btn_force.config(state=tk.DISABLED)

    def wrapper():
        run_script(console, force=force)
        btn_run.config(state=tk.NORMAL)
        btn_force.config(state=tk.NORMAL)
        global running
        running = False

    threading.Thread(target=wrapper).start()


# === GUI ===
root = tk.Tk()
root.title("Bing Automation Tool")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn_run = tk.Button(frame, text="Run", width=15, command=lambda: threaded_run(console, force=False))
btn_run.grid(row=0, column=0, padx=5)

btn_force = tk.Button(frame, text="Force Run", width=15, command=lambda: threaded_run(console, force=True))
btn_force.grid(row=0, column=1, padx=5)

btn_exit = tk.Button(frame, text="Exit", width=15, command=root.quit)
btn_exit.grid(row=0, column=2, padx=5)

console = scrolledtext.ScrolledText(root, height=20, width=60, state='normal')
console.pack(padx=10, pady=10)

log_to_console(console, "Ready. Click 'Run' or 'Force Run'.")

root.mainloop()
