import pyttsx3
import pythoncom
# import pywin32
import speech_recognition as sr

engine = pyttsx3.init('sapi5')  # API , we will initiate this api
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("")

def takecommand():
    ram = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening........")
        ram.pause_threshold=1
        audio=ram.listen(source)
    try:
        print("recognizing......")
        query= ram.recognize_google(audio, language="en-in")
        print(f"user said:{query}\n")
        speak(query)


    except Exception as e:
        print("say that again please:")
        return("None")
    return query

takecommand()




