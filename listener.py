import pyaudio
import speech_recognition as sr

r=sr.Recognizer()
r.energy_threshold=4000

def take_command():
   print("Listening...")
   with sr.Microphone() as source:
      audio=r.listen(source)

   try:
      return(r.recognize_google(audio))
   except:
      print('Speech not understood')
