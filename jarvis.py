import speech_recognition
import datetime
import webbrowser
from win32com.client import Dispatch
import wikipedia

def greet():
    print(datetime.datetime.now().date())
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak("good morning")

    elif hour >= 12 and hour <= 18:
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak("good afternoon")

    elif hour >= 18 and hour <= 24:
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak("good evening")

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak("What can I do for you")


try:

    def takecommand():
        s = speech_recognition.Recognizer()

        print("Listening...")

        with speech_recognition.Microphone() as m:
            audio = s.listen(m)
            query = s.recognize_google(audio, language='eng-in')
            print('Recognizing...\n')
            print(query)
            return query


    if __name__ == "__main__":
        greet()
        running = True
        while running:
            query = takecommand().lower()

            if 'open youtube' in query:
                webbrowser.open('www.youtube.com')

            elif 'wikipedia' in query:
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak = Dispatch("SAPI.SpVoice")
                speak.Speak("According to Wikipedia" + str(result))

            elif 'play music' in query:
                webbrowser.open('www.spotify.com')

            elif 'repeat' in query:
                query = query.replace("repeat", "You said ")
                speak = Dispatch('SAPI.SpVoice')
                speak.Speak(query)

            elif 'open google' in query:
                webbrowser.open("www.google.com")

            elif 'date' in query:
                speak = Dispatch("SAPI.SpVoice")
                speak.Speak(datetime.datetime.now().date())

            elif 'time' in query:
                speak = Dispatch("SAPI.SpVoice")
                speak.Speak(datetime.datetime.now().time())

            elif 'open python' in query:
                webbrowser.open("C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37\\Lib\idlelib\\idle.pyw")# your python targat

            elif 'stop' in query:
                running = False

except Exception:
    a = "You spoke nothing for a long time"
    print(a)
