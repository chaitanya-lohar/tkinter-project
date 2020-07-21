import pyttsx3
import speech_recognition as sr
import pythoncom
#pyaudio is installed using wheels
#Google > unofficial python binaries > ctrl+f(find pyaudio)> click on pyaudio> install according to your system(64bit) and pycharm version(3.6).
# copy and paste the wheel in pycharm > right click on the wheel > open terminal> write command "pip install pyaudio".
engine=pyttsx3.init("sapi5")
voice=engine.getProperty("voices")
engine.setProperty('voice',voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listening():
    receiver=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        receiver.pause_threshold=1
        audio=receiver.listen(source)
        print(audio)
    try:
        print("Recognising")
        query=receiver.recognize_google(audio,language='en-in')
        print(f"User said {query} \n")
    except Exception as e:
        print("Say that again please ")
        return "None"
    return query
# print(var)
# speak(var)