from speaker import speak
from listener import take_command
import datetime
import wikipedia
import pyjokes
import pywhatkit
import subprocess
import sys
from PyDictionary import PyDictionary

try:
    def note():
        speak("Making the note, what should I include in it?")
        text = take_command()
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)

        subprocess.Popen(["notepad.exe", file_name])

    def mainBody():
        dictionary=PyDictionary()
        speak("What is your bidding?")
        command = take_command()
        print(command)

        if "hello" in command:
            speak("Hello, I am INFINITY, I live to ease your life my great master")

        elif "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')# I gets the 12 hour format, p gives am or pm
            speak("The current time is "+ time)

        if "play" in command:
            song = command.replace("play","")
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif "joke" in command:
            speak(pyjokes.get_joke())

        elif "note" in command:
            note()

        elif "play" in command:
            song = command.replace("play","")
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif "define" in command:
            Word = command.replace("define","")
            speak(dictionary.meaning(Word))

        elif "end" in command or "done" in command or "abort" in command or "bye" in command:
            sys.exit()

    while True:
        mainBody()

except:
    speak("An unexpected error occured")