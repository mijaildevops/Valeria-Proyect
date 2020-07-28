import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        #text = r.recognize_google(audio, language = "en-US") # Ingles
        text = r.recognize_google(audio, language = "es-ES") # Spanish
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

engine = pyttsx3.init()
engine.say(str(text))
engine.runAndWait()