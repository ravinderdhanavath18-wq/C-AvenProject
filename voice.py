import pyttsx3
import speech_recognition as sr
import threading
import time

class AvenVoice:
    def __init__(self, language="en-IN"):
        self.language = language
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 170)

    def set_language(self, language):
        self.language = language

    def speak(self, text):
        if not text:
            return
        print(f"Aven: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_once(self):
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)
            text = self.recognizer.recognize_google(audio, language=self.language)
            print(f"You: {text}")
            return text
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""
        except Exception:
            return ""

    def listen_for_wake_word(self, wake_word="aven"):
        while True:
            try:
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=6)
                text = self.recognizer.recognize_google(audio, language=self.language)
                text = text.lower().strip()
                print("Wake check:", text)
                if wake_word in text:
                    return text
            except Exception:
                continue
