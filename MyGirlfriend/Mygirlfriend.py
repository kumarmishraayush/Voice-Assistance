
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
#import pywhatkit as pwt

import speech_recognition as sr
from time import timezone


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

print(voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    
    speak("Whats up   ,   how you do in ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("I'm listening Sir don't worry......")
      r.pause_threshold = 1
      audio = r.listen(source)
    
    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir said : {query}\n")
    
    except Exception as e:
        print("Say Again PLease.....")
        return "None"
    
    return query

if __name__ == "__main__":
 wishMe()

  
 #baat sun ke kaam karegi
 while True :
    query = takeCommand().lower()
    if "bad" in query:
     speak("go and study first that is important rather than using this laptop")
     exit()
    elif 'exit' in query :
        speak("ok bye  have a nice day ")
        exit()
    elif 'good' in query:
        speak("welldone thats why have knowledge")
    elif 'wikipedia' in query :

       speak('just searching Sir')
       query = query.replace("wikipedia","")
       results = wikipedia.summary(query,sentences =2)
       speak("according to wikipedia Sir the result is") 
       print(results)
       speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    # elif 'search' in query:
    #     pwt.search(query.lstrip('search'))
    elif 'find favourite videos' in query :
        webbrowser.open('xvideos3.com')
    elif 'open facebook ' in query :
        webbrowser.open("facebook.com")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H hours%M minute%Ssecond")
        speak(f"Sir  the time is {strTime}")
    elif 'open code' in query:
        codePath =   "C:\\Users\\kumar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        os.startfile(codePath)
    elif 'play music' in query:
        music_dir = "D:\\Music"
        songs  = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'close youtube' in query:
        os.system("taskkill / im chrome.exe/f")

    
    
