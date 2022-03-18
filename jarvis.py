from datetime import datetime
from html.entities import codepoint2name
from http import server
import imghdr
from logging import critical
from tkinter.tix import Tree
from unittest import result
from pygame import init
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from requests import get
import sys
import cv2
# import pywhatKit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
        speak("Have a nice day")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
        speak("Hope have a nice day")
    elif hour >= 18 and hour < 19:
        speak("Good Evening Sir!")
        speak("Hope had a nice day")
    else:
        speak("Good night Sir!")
        speak("Have a sleep sir its too late")

    speak("I am jarvis how i can help you Sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say again please...")
        return "None"
    return query


def sendEmail(to, content):
    server.smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Yourmail@gmail.com', 'Password')
    server.sendemail('Yourmail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Sir what should i search in google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'location' in query:
            webbrowser.open('googlemaps.com')
        elif 'play music' in query:
            music_dir = 'D:\\Non critical\\songs\\Favorite Songs2'
            songs = os.listen(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\someone\\OneDrive\\Desktop\\Coding\\Python\\Pyhton project\\someone"
            os.startfile(codePath)
        elif 'email to someone' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "Yourmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry someone i am unable to send email for you")
        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            print(ip)
            speak(f"Your ip address is {ip}")
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        # elif "send whatsapp message" in query:
           #   kit.sendwhatmsg("000000000", "This is jarvis and Lucy", 2, 25)
        elif "shut up" in query:
            speak("Your Welcome someone. Shutting down the system")
            sys.exit()
        speak("Sir do you have any other work")
