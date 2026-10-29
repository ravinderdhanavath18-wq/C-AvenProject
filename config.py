import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en-IN")
WAKE_WORD = os.getenv("WAKE_WORD", "aven")

# Approved apps only. Add more as needed.
ALLOWED_APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "google chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": r"C:\Windows\System32\notepad.exe",
    "calculator": r"C:\Windows\System32\calc.exe",
    "command prompt": r"C:\Windows\System32\cmd.exe",
    "terminal": r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
    "file explorer": r"C:\Windows\explorer.exe",
    "explorer": r"C:\Windows\explorer.exe",
    "vs code": r"C:\Program Files\Microsoft VS Code\Code.exe",
    "vscode": r"C:\Program Files\Microsoft VS Code\Code.exe",
    "spotify": r"C:\Users\Public\Desktop\Spotify.lnk",  # update if needed
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
}

# Allowed actions
SAFE_COMMANDS = {
    "open",
    "launch",
    "close",
    "search",
    "write",
    "tell",
    "what",
    "who",
    "where",
    "hello",
    "hi",
    "help",
}
