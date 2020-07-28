# https://www.devdungeon.com/content/text-speech-python-pyttsx3
import pyttsx3

""" engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop() """

engine = pyttsx3.init()

# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_ZIRA_11.0"

# Use female English voice
engine.setProperty('voice', en_voice_id)
engine.say('Hello with my new voice')



engine.runAndWait()