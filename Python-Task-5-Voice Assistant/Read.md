# 🎙️ Voice Assistant – Python Internship Project

## 📌 Project Overview

This project is a **Python-based Voice Assistant** that listens to spoken commands, understands basic requests, and responds using text-to-speech.

The project is developed as part of a **Python Internship** to demonstrate practical knowledge of Python, voice recognition, automation, web browsing, and API integration.

The Beginner version focuses on core voice-assistant functionality, while the Advanced version adds natural language understanding, email, reminders, weather information, and customizable commands.

---

## 🎯 Objective

The main objective of this project is to build a voice-controlled application that can:

* Capture commands through a microphone.
* Convert speech into text.
* Process the user's command.
* Perform the requested action.
* Respond using synthesized speech.
* Handle errors when speech cannot be understood.

---

## 🛠️ Technologies Used

### Beginner Tier

* **Python**
* **SpeechRecognition**
* **PyAudio**
* **pyttsx3**
* **datetime**
* **webbrowser**

### Advanced Tier

* **Python**
* **SpeechRecognition**
* **pyttsx3**
* **NLTK / Transformers**
* **OpenWeatherMap API**
* **smtplib**
* **datetime / time**
* **JSON / configuration files**

---

## ✨ Features

### Beginner Features

* [ ] Capture voice input using `speech_recognition`.
* [ ] Respond to **"Hello"** with a predefined greeting.
* [ ] Tell the current time.
* [ ] Tell the current date.
* [ ] Search the web using a spoken topic.
* [ ] Open the browser automatically.
* [ ] Ask the user to repeat when speech is not understood.
* [ ] Provide text-to-speech feedback for responses.

### Advanced Features

* [ ] Understand natural-language commands.
* [ ] Send an email using voice commands.
* [ ] Set timed reminders.
* [ ] Give an audible reminder alert.
* [ ] Fetch live weather information.
* [ ] Read weather information aloud.
* [ ] Answer general knowledge questions.
* [ ] Allow custom commands.
* [ ] Store custom commands in a configuration file.
* [ ] Document privacy and data processing considerations.

---

## 📂 Project Structure

```text
Voice-Assistant/
│
├── main.py
├── README.md
├── requirements.txt
├── config.json
└── .gitignore
```

### File Description

| File               | Purpose                                  |
| ------------------ | ---------------------------------------- |
| `main.py`          | Main voice-assistant program             |
| `README.md`        | Project documentation                    |
| `requirements.txt` | Python dependencies                      |
| `config.json`      | Custom commands and configuration        |
| `.gitignore`       | Files that should not be uploaded to Git |

---

## ⚙️ Installation

### 1. Install Python

Download and install Python from the official Python website:

https://www.python.org/downloads/

During installation on Windows, make sure to enable:

```text
Add Python to PATH
```

---

### 2. Open Command Prompt

Open **Command Prompt** or the terminal inside VS Code.

Check Python installation:

```bash
python --version
```

You should see a Python version such as:

```text
Python 3.x.x
```

---

### 3. Install Required Libraries

For the beginner version, install:

```bash
pip install SpeechRecognition pyttsx3 PyAudio
```

If `PyAudio` causes installation problems on Windows, install a compatible PyAudio package/build for your Python version or use a supported audio-input alternative.

---

## ▶️ How to Run the Project

Navigate to the project folder:

```bash
cd Voice-Assistant
```

Run the program:

```bash
python main.py
```

The assistant will start listening through the microphone.

---

# 🗣️ Example Commands

The assistant can respond to commands such as:

```text
Hello
```

```text
What is the time?
```

```text
Tell me today's date
```

```text
Search Python tutorials
```

Example interaction:

```text
Assistant: Hello! How can I help you?

User: What is the time?

Assistant: The current time is 09:30 PM.
```

Another example:

```text
User: Search Python voice assistant tutorial

Assistant: Searching for Python voice assistant tutorial.

[Browser opens with the search results]
```

---

# 🧠 How the Voice Assistant Works

The application follows these basic steps:

```text
Microphone
     ↓
Speech Recognition
     ↓
Convert Speech → Text
     ↓
Process Command
     ↓
Perform Action
     ↓
Generate Response
     ↓
Text-to-Speech
     ↓
Speaker
```

### Step 1 – Listen

The microphone captures the user's voice.

### Step 2 – Recognize

The `speech_recognition` library converts spoken audio into text.

### Step 3 – Process

Python checks the recognized command and determines what action should be performed.

### Step 4 – Execute

The program performs the requested task, such as checking the time or opening a web search.

### Step 5 – Respond

`pyttsx3` converts the response text into spoken audio.

---

# 🔊 Text-to-Speech

The project uses the `pyttsx3` library to provide audible responses.

Example:

```python
import pyttsx3

engine = pyttsx3.init()

engine.say("Hello! How can I help you?")
engine.runAndWait()
```

This allows the assistant to communicate with the user without requiring a screen-based response.

---

# 🎤 Speech Recognition

The `SpeechRecognition` library is used to capture audio from the microphone and recognize spoken commands.

Example:

```python
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)
except sr.UnknownValueError:
    print("Sorry, I could not understand you.")
except sr.RequestError:
    print("Speech recognition service is unavailable.")
```

---

# 🕒 Date and Time

Python's `datetime` module can be used to obtain the current date and time.

Example:

```python
from datetime import datetime

current_time = datetime.now().strftime("%I:%M %p")
current_date = datetime.now().strftime("%d %B %Y")
```

The assistant can then speak the result to the user.

---

# 🌐 Web Search

The built-in `webbrowser` module can open a browser search.

Example:

```python
import webbrowser

query = "Python programming tutorial"
webbrowser.open(
    "https://www.google.com/search?q=" + query.replace(" ", "+")
)
```

The voice assistant can obtain the search query directly from the user's spoken command.

---

# 🛡️ Error Handling

The application should handle situations where the microphone input cannot be understood.

Example:

```python
try:
    command = recognizer.recognize_google(audio)
except sr.UnknownValueError:
    speak("Sorry, I couldn't understand that. Please repeat.")
except sr.RequestError:
    speak("The speech recognition service is currently unavailable.")
```

This prevents the application from crashing and provides a better user experience.

---

# 🚀 Advanced Features

## 1. Natural Language Understanding

The advanced version can process more flexible sentences instead of relying only on exact keywords.

For example, users may say:

```text
Could you please tell me what time it is?
```

instead of:

```text
What is the time?
```

Natural language processing can be implemented using libraries such as:

* `nltk`
* `transformers`

---

## 2. Email Automation

The assistant can send emails based on spoken commands using Python's `smtplib`.

Example workflow:

```text
User speaks
     ↓
Assistant identifies email intent
     ↓
Collect recipient and message
     ↓
Connect to email server
     ↓
Send email
```

A test or dummy email account should be used during development.

Sensitive credentials should **never** be hard-coded into the source code.

---

## 3. Timed Reminders

The assistant can allow users to create reminders.

Example:

```text
User: Remind me after 10 seconds.
```

The program waits for the requested duration and then produces an audible notification.

---

## 4. Weather Updates

The advanced version can retrieve weather information using an API such as **OpenWeatherMap**.

Example:

```text
User: What is the weather in Hyderabad?

Assistant: Fetching weather information...
Assistant: The current temperature is ...
```

An API key is required for the weather service.

The API key should be stored securely and should not be uploaded to GitHub.

---

## 5. General Knowledge Questions

The assistant can answer general questions using:

* A local knowledge base.
* A question-answering API.
* A suitable NLP/AI model.

Example:

```text
User: Who invented the telephone?

Assistant: ...
```

---

## 6. Custom Commands

Users can define additional commands using a configuration file such as:

```json
{
    "open_youtube": "https://www.youtube.com",
    "open_github": "https://github.com"
}
```

The assistant can load these commands and execute them when requested.

---

# 🔐 Privacy Considerations

The application should clearly document what information is processed.

Possible data includes:

* Microphone audio captured while listening.
* Recognized speech converted into text.
* User-entered search queries.
* Weather API requests.
* Email information when the email feature is enabled.

The project should follow these practices:

* Do not store microphone recordings unless required.
* Do not expose API keys or passwords.
* Do not upload `.env` files or credentials to GitHub.
* Use test accounts for email development.
* Explain to users when an external service receives their data.

---

# 📋 Beginner Feature Checklist

* [ ] Python environment installed.
* [ ] `SpeechRecognition` installed.
* [ ] `pyttsx3` installed.
* [ ] Microphone input working.
* [ ] `"Hello"` greeting implemented.
* [ ] Current time implemented.
* [ ] Current date implemented.
* [ ] Web search implemented.
* [ ] Error handling implemented.
* [ ] Text-to-speech responses implemented.

---

# 📋 Advanced Feature Checklist

* [ ] Natural language intent recognition.
* [ ] Voice-controlled email.
* [ ] Timed reminders.
* [ ] Audible reminder alerts.
* [ ] Weather API integration.
* [ ] General knowledge question answering.
* [ ] Custom command support.
* [ ] Configuration file support.
* [ ] Privacy documentation.

---

# 🧪 Testing

The application should be tested using different voice commands.

### Test Case 1 – Greeting

**Input:**

```text
Hello
```

**Expected Output:**

```text
Hello! How can I help you?
```

### Test Case 2 – Time

**Input:**

```text
What is the time?
```

**Expected Output:**

```text
The current time is ...
```

### Test Case 3 – Date

**Input:**

```text
What is today's date?
```

**Expected Output:**

```text
Today's date is ...
```

### Test Case 4 – Web Search

**Input:**

```text
Search Python tutorials
```

**Expected Output:**

The browser opens a search page for the requested topic.

### Test Case 5 – Unrecognized Speech

**Input:**

Unclear or unsupported speech.

**Expected Output:**

```text
Sorry, I couldn't understand that. Please repeat.
```

---

# 📚 Learning Outcomes

By completing this project, the intern gains practical experience with:

* Python programming.
* Functions and modules.
* Exception handling.
* Speech recognition.
* Text-to-speech systems.
* Microphone and audio input.
* Date and time handling.
* Browser automation.
* API integration.
* Natural language processing.
* Email automation.
* Configuration management.
* Basic software security and privacy practices.

---

# 🔗 Learning Resources

The project can be developed using official documentation and tutorials.

### Python

https://www.python.org/

### SpeechRecognition – PyPI

https://pypi.org/project/SpeechRecognition/

### pyttsx3 – PyPI

https://pypi.org/project/pyttsx3/

### OpenWeatherMap

https://openweathermap.org/

### Suggested YouTube Search – Beginner

```text
Python voice assistant tutorial speech_recognition pyttsx3
```

### Suggested YouTube Search – Advanced NLP

```text
Python NLP chatbot intent recognition tutorial
```

### Suggested YouTube Search – Weather API

```text
OpenWeatherMap API Python tutorial
```

---

# 📌 Internship Project Summary

**Project Name:** Voice Assistant
**Programming Language:** Python
**Project Level:** Beginner / Advanced
**Domain:** Voice Recognition and Automation

This project demonstrates how Python can be used to create an interactive voice-controlled assistant. The beginner implementation focuses on speech recognition, text-to-speech, date/time information, greetings, and web search. The advanced implementation extends the system with NLP, email automation, reminders, weather APIs, question answering, and customizable commands.

---

# 👩‍💻 Author

**Name:** P. Yesheshwini

**Project:** Python Internship – Voice Assistant

**Year:** 2026
