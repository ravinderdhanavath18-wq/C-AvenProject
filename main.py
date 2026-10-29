import re
import os
import time
from config import DEFAULT_LANGUAGE, WAKE_WORD
from voice import AvenVoice
from assistant import AvenAssistant
from app_controller import AppController

class Aven:
    def __init__(self):
        self.language = DEFAULT_LANGUAGE
        self.voice = AvenVoice(language=self.language)
        self.ai = AvenAssistant()
        self.app_controller = AppController()

    def detect_language(self, text):
        if not text:
            return self.language
        if re.search(r"[\u0900-\u097F]", text):
            return "hi-IN"
        return "en-IN"

    def clean_command(self, text):
        if not text:
            return ""
        text = text.lower()
        text = text.replace("aven", "", 1).strip()
        return text

    def handle_command(self, command):
        text = command.lower().strip()

        if "open" in text or "launch" in text:
            # Example: "open chrome"
            pattern = r"(?:open|launch)\s+(.*)"
            match = re.search(pattern, text)
            if match:
                app = match.group(1).strip()
                return self.app_controller.open_app(app)
            return "Which app do you want me to open?"

        if "close" in text:
            pattern = r"close\s+(.*)"
            match = re.search(pattern, text)
            if match:
                app = match.group(1).strip()
                return self.app_controller.close_app(app)
            return "Which app do you want me to close?"

        if "search" in text:
            pattern = r"search\s+(.*)"
            match = re.search(pattern, text)
            if match:
                query = match.group(1).strip()
                return self.app_controller.search_web(query)
            return "What would you like me to search for?"

        if "write" in text and "notepad" in text:
            pattern = r"write\s+(.*)"
            match = re.search(pattern, text)
            if match:
                content = match.group(1).strip()
                return self.app_controller.open_notepad_and_write(content)
            return "What text do you want me to write in Notepad?"

        if "hello" in text or "hi" in text:
            return self.ai.ask(text)

        if "help" in text:
            return (
                "I can open apps, search the web, answer questions, and control approved desktop apps. "
                "Examples: Open Chrome, Search python tutorials, Close Notepad"
            )

        return self.ai.ask(text)

    def run(self):
        self.voice.speak("Hello, I am Aven. I am ready to help.")
        while True:
            command = self.voice.listen_once()
            if not command:
                self.voice.speak("I did not hear you clearly. Please say again.")
                continue

            # language detection
            lang = self.detect_language(command)
            self.voice.set_language(lang)

            # remove wake word if present
            cleaned = self.clean_command(command)
            if not cleaned:
                self.voice.speak("Please say your command again.")
                continue

            response = self.handle_command(cleaned)
            self.voice.speak(response)

if __name__ == "__main__":
    aven = Aven()
    aven.run()
