import os
from openai import OpenAI
from config import OPENAI_API_KEY

class AvenAssistant:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

    def ask(self, prompt):
        if not self.client:
            return self.fallback_response(prompt)

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Aven, a friendly desktop AI assistant. "
                            "Answer in English or Hindi depending on the user's request. "
                            "Keep answers concise but helpful."
                        )
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=300,
            )
            return response.choices[0].message.content.strip()
        except Exception:
            return self.fallback_response(prompt)

    def fallback_response(self, prompt):
        lower = prompt.lower()

        if "hello" in lower or "hi" in lower:
            return "Hello! I am Aven. How can I help you today?"
        if "hindi" in lower:
            return "मैं Aven हूँ। मैं आपकी सहायता कर सकता हूँ।"
        if "time" in lower:
            import datetime
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
        return (
            "I am Aven, your desktop assistant. "
            "I can open apps, search the web, answer questions, and assist with commands."
        )
