import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import openai
import os
import google.generativeai as genai
import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def ai(prompt):
    genai.configure(api_key="AIzaSyAyo7t85w-AVHqy9JUFRLolBvhonb356DU")
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = prompt
    response = model.generate_content(prompt)
    print(response.text)
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()} .txt", "w") as f:
        f.write(response.text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio , language ='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis "

if __name__ == "__main__":
    print("PyCharm")
    say("Hello, I am Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [
            ["youtube", "https://www.youtube.com/"],
            ["google", "https://www.google.com/"],
            ["wikipedia", "https://www.wikipedia.com/"],
            ["github", "https://www.github.com/"],
            ["stackoverflow", "https://stackoverflow.com/"],
            ["reddit", "https://www.reddit.com/"],
            ["amazon", "https://www.amazon.in/"],
            ["facebook", "https://www.facebook.com/"],
            ["twitter", "https://www.twitter.com/"],
            ["linkedin", "https://www.linkedin.com/"],
            ["instagram", "https://www.instagram.com/"],
            ["flipkart", "https://www.flipkart.com/"],
            ["netflix", "https://www.netflix.com/"],
            ["quora", "https://www.quora.com/"],
            ["spotify", "https://www.spotify.com/"]
        ]

        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])



        if "open music".lower() in query.lower():
            musicPath = r"C:\Users\ROHIT\Downloads\Post_Malone_-_Sunflower.mp3"
            os.startfile(musicPath)

        if "using Artificial Intelligence".lower() in query.lower():
            ai(prompt=query)



        elif "the time".lower() in query.lower():
            strfTime = datetime.datetime.now().strftime("%I:%M:%S")
            say(f"The time is {strfTime}")
        elif "open blender".lower() in query.lower():
            blenderPath = r"C:\Users\ROHIT\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Blender\Blender 4.5.lnk"
            os.startfile(blenderPath)
            say(f"opening blender sir..")
        elif "open camera".lower() in query.lower():
            os.system("start microsoft.windows.camera:")

        #say(text)
