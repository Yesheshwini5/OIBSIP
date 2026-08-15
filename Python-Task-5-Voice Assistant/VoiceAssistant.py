import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse


# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech and print it."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to the user's voice and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for background noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Sorry, the speech recognition service is unavailable.")
            return ""


def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")


def tell_date():
    """Tell the current date."""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}.")


def web_search(topic):
    """Search the web for the requested topic."""
    if topic:
        encoded_topic = urllib.parse.quote(topic)
        url = f"https://www.google.com/search?q={encoded_topic}"

        speak(f"Searching the web for {topic}.")
        webbrowser.open(url)
    else:
        speak("Please tell me what you want me to search for.")


def process_command(command):
    """Process the user's command."""

    if not command:
        return True

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        tell_time()

    # Date
    elif "date" in command or "today" in command:
        tell_date()

    # Web search
    elif "search for" in command:
        topic = command.split("search for", 1)[1].strip()
        web_search(topic)

    elif "search" in command:
        topic = command.split("search", 1)[1].strip()
        web_search(topic)

    # Exit
    elif "exit" in command or "quit" in command or "goodbye" in command:
        speak("Goodbye! Have a great day.")
        return False

    # Unknown command
    else:
        speak(
            "I'm not sure how to help with that. "
            "You can say hello, ask for the time, "
            "ask for the date, or ask me to search the web."
        )

    return True


def main():
    """Main voice assistant program."""

    speak("Voice assistant started.")
    speak("How can I help you?")

    running = True

    while running:
        command = listen()
        running = process_command(command)


if __name__ == "__main__":
    main()