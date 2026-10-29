# Aven Desktop AI Assistant

Aven is a desktop AI assistant that listens to voice commands in English and Hindi, opens approved apps, searches the web, answers questions, and can write text into Notepad.

## Features
- Voice input and response
- English/Hindi command support
- App launching with allowlist
- Web search
- AI Q&A using OpenAI API
- Permission-based app access

## Setup
1. Create a virtual environment:
   python -m venv .venv
   .venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Create a .env file:
   copy .env.example .env

4. Add your OpenAI API key:
   OPENAI_API_KEY=your_key_here

5. Update allowed app paths in config.py

6. Run:
   python main.py

## Example commands
- Open Chrome
- Launch Notepad
- Search for Python tutorials
- Close Calculator
- Hello Aven
- Hindi me jawab do

## Notes
- App list is permission-based. Only apps in config.py can be opened.
- You may need to adjust paths for your machines.
