# IMPORTING LIBRARIES
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import json
import requests
import sys
import pywhatkit
import pyjokes
import pyautogui

# VOICE ENGINE
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[11].id)
# engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty('voice', 'english-us')


def speak(text):
    engine.say(text)
    engine.runAndWait()


print(" LOADING YOUR AI - MONKEY ")
speak(" LOADING YOUR AI - MONKEY ")

# GREETING
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak(" Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak(" Hello,Good Afternoon")
    else:
        speak(" Hello, Good Evening")


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Days = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thrusday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    if day in Days.keys():
        day_of_week = Days[day]
        speak("The day is " + day_of_week)


def tellTime():
    today = time.localtime()
    today_TIME = time.strftime('%H:%M:%S', today)
    speak('Time is '+today_TIME)

# Take command function


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source, timeout=8, phrase_time_limit=8)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("pardon me ,please say that again")
            return 'None'
        return statement


# wishMe()


if __name__ == '__main__':
    wishMe()
    tellDay()
    tellTime()

    speak(" I am activated")
    speak(" Tell me how can i help you ")

    # COMMAND LOOP
    while (True):
        print("_")
        query = takeCommand().lower()

        if query == 0:
            continue

        # COMMANDS
        bye = ["goodbye", "bye", "tata", "sleepnow"]
        if query in bye:
            speak(" I am shutting down, have a good time, Good bye")
            sys.exit()

        if 'open google' in query:
            speak('Opening google')
            #chrome_path = '/use/bin/google-chrome %s'
            webbrowser.open_new_tab('https://www.google.com')
        elif 'search in google' in query:
            word = query.replace("search in google", "")
            webbrowser.open_new_tab(
                'https://www.google.com/search?q='+word)

        if 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open_new_tab("https://www.youtube.com")
        elif 'search in youtube' in query:
            word = query.replace("search in youtube", "")
            webbrowser.open_new_tab(
                'https://www.youtube.com/results?search_query='+word)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing '+song)
            pywhatkit.playonyt(song)

        elif 'how are you monkey' in query:
            speak("i am fine , thankyou")
            speak("how are you sir")

        fine_reply = ["good", "fine", "i am good", "great", "feeling good"]
        if query in fine_reply:
            speak("good to know sir")

        elif 'who are you' in query:
            speak('I am monkey version 1 point 1 your personal assistant  I am programmed to do minor tasks like opening youtube,google,predict time,search wikipedia')

        elif 'shutdown system now' in query or 'shutdown now' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            cmd = 'shutdown now'
            os.system(cmd)
        elif 'shutdown system' in query:
            cmd = 'shutdown'
            os.system(cmd)
            speak("Your system will shutdown in 60 seconds")
            for sec in range(57, 0, -1):
                speak(sec)

        elif 'restart computer' in query:
            speak(' restarting your computer in 60 seconds')
            for sec in range(60, 0, -1):
                speak(sec)
            cmd = 'reboot'
            os.system(cmd)

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Dheeraj.")

        elif "who am i" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Dheeraj further It's a secret")

        if "tell me a joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            city_name = query.replace('weather', '')
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature_in_KELVIN = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                current_temperature_in_CELSIUS = current_temperature_in_KELVIN - 273.15
                print(" Temperature in celsius unit is " +
                      str(current_temperature_in_CELSIUS) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                speak(" Temperature in celsius unit is " +
                      str(current_temperature_in_CELSIUS) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("searching "+location+' in google maps')
            webbrowser.open(
                "https://www.google.nl/maps/place/" + location + "")

        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")

        elif "switch the window" in query or "switch window" in query:
            speak("Okay sir, Switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        # elif "camera" in query or "take a photo" in query:
        #     ec.capture(0,'camera','img.png')

time.sleep(3)
