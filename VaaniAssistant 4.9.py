import speech_recognition as sr
import pyttsx3
from datetime import datetime
import sys

import pocketsphinx  

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("VaaniAssistant 4.9:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("Waiting timed out, please speak a little faster.")
            return ""
    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Speech service is not available right now.")
        return ""

def process_command(command):
    # Greetings and time
    if any(word in command for word in ["vanakkam", "hello", "hi", "good morning", "good evening", "good night"]):
        speak("Vanakkam! How can I help you?")
    elif any(word in command for word in ["how are you", "how ru", "how r u"]):
        speak("I am fine, thanks for asking!")
    elif any(word in command for word in ["thank you", "thanks"]):
        speak("You’re welcome!")
    elif any(word in command for word in ["bye", "exit", "quit", "poitu varen"]):
        speak("Goodbye! Have a nice day.")
        sys.exit()

    # Time related
    elif any(word in command for word in ["neram", "time", "what time"]):
        now = datetime.now()
        speak(f"The time is {now.strftime('%I:%M %p')}.")

    # Light controls
    elif any(word in command for word in ["light on", "vellicham on", "vilakku on", "light_ah_on_pannunga"]):
        speak("Turning on the light.")
    elif any(word in command for word in ["light off", "vellicham off", "vilakku off", "light_ah_off_pannunga"]):
        speak("Turning off the light.")

    # Fan controls
    elif any(word in command for word in ["fan on", "pankka on", "fan_ah_on_pannu"]):
        speak("Turning on the fan.")
    elif any(word in command for word in ["fan off", "pankka off", "fan_ah_off_pannu"]):
        speak("Turning off the fan.")

    # TV controls
    elif any(word in command for word in ["tv on", "tv_on_aagattum"]):
        speak("Turning on the TV.")
    elif any(word in command for word in ["tv off", "tv_off_pannunga"]):
        speak("Turning off the TV.")

    # AC controls
    elif any(word in command for word in ["ac on", "ac on pannunga"]):
        speak("Turning on the air conditioner.")
    elif any(word in command for word in ["ac off", "ac off pannunga"]):
        speak("Turning off the air conditioner.")

    # Door controls
    elif any(word in command for word in ["door open", "vāsal thirappu", "door open pannunga"]):
        speak("Opening the door.")
    elif any(word in command for word in ["door close", "vāsal moodu", "door close pannu"]):
        speak("Closing the door.")

    # Curtain controls
    elif any(word in command for word in ["curtain open"]):
        speak("Opening the curtain.")
    elif any(word in command for word in ["curtain close"]):
        speak("Closing the curtain.")

    # Music controls
    elif any(word in command for word in ["music on", "play music", "song", "music play", "isai oodu", "isai start pannu"]):
        speak("Playing music now.")
    elif any(word in command for word in ["stop music", "pause music", "music off", "music stop", "isai niruththu", "isai stop pannu"]):
        speak("Stopping the music.")

    # Volume controls
    elif any(word in command for word in ["increase volume", "volume konjam jasthi pannu"]):
        speak("Increasing the volume.")
    elif any(word in command for word in ["decrease volume", "volume konjam adinga"]):
        speak("Decreasing the volume.")

    # Alarm
    elif any(word in command for word in ["alarm set", "thooku eludhal"]):
        speak("Alarm has been set.")
    elif any(word in command for word in ["alarm stop", "thooku niruththal"]):
        speak("Alarm has been stopped.")

    # Speech mode
    elif any(word in command for word in ["speech mode start", "pattimandram start"]):
        speak("Speech mode started.")
    elif any(word in command for word in ["speech mode stop", "pattimandram stop"]):
        speak("Speech mode stopped.")

    # Weather
    elif any(word in command for word in ["weather", "climate"]):
        speak("I am unable to fetch weather right now.")

    # Fallback
    else:
        speak("Sorry, I did not understand that. Please try again.")

if __name__ == "__main__":
    with sr.Microphone() as source:
        print("Calibrating ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
    speak("VaaniAssistant 4.9 is ready.")

    while True:
        user_command = listen()
        if user_command:
            process_command(user_command)
