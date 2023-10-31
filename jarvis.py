import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser 
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING!")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON!")
    else:
        speak("GOOD EVENING!")
    
    speak("I am Jarvis ,please tell me how may i help you")


def takeCommand():
    #it takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")

        elif 'search in youtube' in query:

            query = query.replace("jarvis","")
            query = query.replace("search in youtube","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("OK,This is what i found for your search!")

        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak('Opening stackoverflow')
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\tuts\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%Hours:%Minutes:%Seconds")
            speak(f"Sir,the time is{strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\vvfgc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)




