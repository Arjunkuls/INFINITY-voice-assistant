import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) # male and female voice (0 = male,1 = female)
engine.setProperty("rate", 178)

def speak(speech):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()
