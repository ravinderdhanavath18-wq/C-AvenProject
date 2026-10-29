import os
import subprocess
import webbrowser
import time
from config import ALLOWED_APPS

class AppController:
    def __init__(self):
        self.allowed_apps = ALLOWED_APPS

    def is_allowed(self, app_name):
        return app_name.lower().strip() in [k.lower() for k in self.allowed_apps.keys()]

    def open_app(self, app_name):
        app_key = None
        for key in self.allowed_apps.keys():
            if key.lower() == app_name.lower():
                app_key = key
                break

        if not app_key:
            for key in self.allowed_apps.keys():
                if app_name.lower() in key.lower():
                    app_key = key
                    break

        if app_key is None:
            return f"I cannot open '{app_name}' because it is not in your approved app list."

        path = self.allowed_apps.get(app_key)
        if not os.path.exists(path):
            return f"The path for '{app_key}' does not exist. Please update the app path in config.py."

        try:
            subprocess.Popen(path)
            return f"Opening {app_key}."
        except Exception as exc:
            return f"I could not open {app_key}: {exc}"

    def close_app(self, app_name):
        try:
            import psutil
            for proc in psutil.process_iter(["name", "exe"]):
                name = (proc.info.get("name") or "").lower()
                exe = (proc.info.get("exe") or "").lower()
                target = app_name.lower()

                if target in name or target in exe:
                    proc.kill()
                    return f"Closed {app_name}."
            return f"I could not find an open app named '{app_name}'."
        except Exception:
            return f"I am unable to close '{app_name}' on this system."

    def search_web(self, query):
        url = "https://www.google.com/search?q=" + query.replace(" ", "+")
        webbrowser.open(url)
        return f"Searching the web for: {query}"

    def open_notepad_and_write(self, text):
        try:
            notepad = subprocess.Popen(["notepad.exe"])
            time.sleep(1)
            # Use clipboard because direct text injection is harder
            import pyperclip
            pyperclip.copy(text)
            # Simulate Ctrl+V
            import pyautogui
            pyautogui.hotkey("ctrl", "v")
            return "Opened Notepad and wrote the text."
        except Exception as exc:
            return f"Could not write into Notepad: {exc}"
