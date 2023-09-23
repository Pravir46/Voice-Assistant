# Project Voice Assistant
import json
#from msilib.schema import SelfReg
import operator
import sys
import time
from typing_extensions import Self  # SUPREET
from urllib import request
import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import random
import re  # regular expression for matching
import os  # creating and removing directory
import cv2
import pywhatkit as kit  # FOR USING WHATSAPP
import smtplib  # For using mail
import subprocess as sp
import pyautogui  # keyboard
import requests  # HTTP
from bs4 import BeautifulSoup
import PyPDF2
import webbrowser as web
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from gui import Ui_jarvisui


from urllib.request import urlopen

#date and time


def date():
    """
    Just return date as string
    :return: date if success, False if fail
    """
    try:
        date = datetime.datetime.now().strftime("%b %d %Y")
    except Exception as e:
        print(e)
        date = False
    return date


def time():
    """
    Just return time as string
    :return: time if success, False if fail
    """
    try:
        time = datetime.datetime.now().strftime("%H:%M:%S")
    except Exception as e:
        print(e)
        time = False
    return time

# wikipedia


def tell_me_about(topic):
    try:
        # info = str(ny.content[:500].encode('utf-8'))
        # res = re.sub('[^a-zA-Z.\d\s]', '', info)[1:]
        res = wikipedia.summary(topic, sentences=3)

        return res
    except Exception as e:
        print(e)
        return False


def speak(audio):  # here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("good morning  ")
        speak("good morning  ")
    elif hour >= 12 and hour < 18:
        print("good afternoon ")
        speak("good afternoon ")
    else:
        print("good evening,  ")
        speak("good evening, ")
    c_date = date()
    print(f"TOday is {c_date}")
    speak(f"TOday is {c_date}")

    c_time = time()
    print(f"Currently it is {c_time}")
    speak(f"Currently it is {c_time}")

    speak("I am Friday. Online and ready")
# now convert audio to text


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        speak("I am ready to take command")
        audio = r.listen(source)
    try:
        print("Recognising.")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except Exception:  # For Error handling

        print("Network connection error")
        return "none"
    return text

# to send mail


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # for checking domain name
    # client wants to upgrade from an insecure connection to a secure one using TLS or SSL.
    server.starttls()
    server.login('pravirkumar46@gmail.com', 'zamullqgrbnijsgc')
    server.sendmail('pravirkumar46@gmail.com', to, content)
    server.close()


# location


def my_location():
    op = "https://www.google.com/maps/place/C.+V.+Raman+Global+University/@20.2192705,85.7336041,17z/data=!3m1!4b1!4m5!3m4!1s0x3a19a8fa59ac3c81:0xc81fc475faa77274!8m2!3d20.2192655!4d85.7357928"
    web.open(op)
    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']
    country = geo_d['country']

    speak(f"you are in {state,country} . ")
    print(f"you are in {state,country} . ")


def googleMaps(Place):
    Url_Place = "https://www.google.com/maps/place/"+str(Place)
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(Place, addressdetails=True)
    target_latlon = location.latitude, location.longitude
    location = location.raw['address']
    target = {'city': location.get('city', ''),
              'state': location.get('state', ''),
              'country': location.get('country', '')}

    current_location = geocoder.ip('me')
    current_latlon = current_location.latlng
    distance = str(great_circle(current_latlon, target_latlon))
    distance = str(distance.split(' ', 1)[0])
    distance = round(float(distance), 2)
    web.open(url=Url_Place)
    speak(target)
    speak(f"{Place} is {distance} Kilometer away from your location")
# Text To Speech


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)


# for main function
def Taskexecution():

    wish()

    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("searching details....Wait")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strtime}")

 # to send the email

        elif 'send a mail' in query or 'mail ' in query:
            try:
                # speak("please tell me, reciever email id")
                # to = takeCommand().lower
                speak("what should i say?")
                content = takeCommand().lower()

                to = "narayangope57@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent ")
            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to sent this mail ")

 # opening apps

        elif 'open microsoft word' in query or 'ms word' in query:
            speak("opening microsoft word")
            sp.Popen(
                "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

        elif 'open microsoft powerpoint' in query or "ms powerpoint" in query:
            speak("opening microsoft powerpoint")
            sp.Popen(
                "C:\\Program Files\\Microsoft Office\root\\Office16\\POWERPNT.EXE")

        elif ' open microsoft excel' in query or 'EXCEL' in query:
            speak("opening microsoft excel")
            sp.Popen(
                "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

        elif 'open command prompt' in query or 'command prompt' in query:
            os.system("start cmd")
            speak("opening command prompt")


# TO CLOSE THE OPENED APP

        elif 'close command prompt' in query or 'close command' in query:
            speak("okay closing command prompt")
            os.system("taskkill /f /im cmd.exe ")

        elif 'close microsoft word' in query or 'close ms word' in query:
            speak("okay closing MICROSOFT WORD")
            os.system("taskkill /f /im WINWORD.EXE ")

        elif 'close microsoft POWER POINT' in query or 'close powerpoint' in query:
            speak("okay closing MICROSOFT POWER POINT")
            os.system("taskkill /f /im POWERPNT.EXE ")

        elif 'close microsoft excel' in query or 'close excel' in query:
            speak("okay closing MICROSOFT EXCEL")
            os.system("taskkill /f /im EXCEL.EXE ")

        elif 'close google' in query:
            speak("okay closing google")
            os.system("taskkill /f /im msedge.exe ")

        elif 'close instagram' in query:
            speak("okay closing instagram")

            os.system("taskkill /f /im chrome.exe ")

        elif 'close youtube' in query:
            speak("okay closing youtube")
            os.system("taskkill /f /im chrome.exe ")

        elif 'close facebook' in query:
            speak("okay closing facebook")
            os.system("taskkill /f /im chrome.exe ")

# OPENING WEBSITES
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

 # to search in google

        elif 'open google' in query:
            speak("what should i search on google")
            cm = takeCommand().lower()

            webbrowser.open(f"{cm}")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")

 # switching window

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
# PLAYING MUSIC AND VIDEO

        elif 'play music on youtube' in query or "play music from youtube" in query:
            kit.playonyt("jaadugar")
            speak("playing jaadugar")

        elif 'music from pc' in query or "music" in query or "play a song" in query:
            speak("ok i am playing music")
            music_dir = 'C:\\Users\\pravi\\Desktop\\Casestudy\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'video from pc' in query or "video" in query or "open a video" in query:
            speak("ok i am playing videos")
            video_dir = 'C:\\Users\\pravi\\Desktop\\jarvis\\video'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'tell me news' in query or 'news' in query:

            try:
                jsonObj = urlopen(
                    'http://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=2bdecf15d7194109af5c0990442c0fae')

                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    if (i == 3):
                        break
            except Exception as e:

                print(str(e))
# FIND YOUR LOCATION
        elif 'where am i' in query:
            my_location()
# FIND ANYWHERE AND DISTANCE FROM YOUR LOCATION
        elif "where is" in query:
            name = query.split('where is ', 1)[1]
            googleMaps(name)
# to tell about something
        elif re.search('tell me about' or "who is", query):
            topic = query.split(' ')[-1]
            if topic:
                wiki_res = tell_me_about(topic)
                print(wiki_res)
                speak(wiki_res)
            else:
                speak(
                    "Sorry sir. I couldn't load your query from my database. Please try again")


# taking screenshot
        elif 'take screenshot' in query or 'take a screenshot' in query or 'screenshot' in query:
            speak("please tell me the name of the screenshot file")
            name = takeCommand().lower()
            speak("please, hold the screen for few seconds, i am taking screenshot")
            # time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak(
                "i am done sir, the screenshot is saved in our main folder.now I am ready for next command")

# to read pdf
        elif 'read a pdf' in query or "read" in query:
            book = open('Harry Potter and The Sorcerer’s Stone.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            speak(f"Total numbers of pages in this book{pages}")
            speak("please enter the page number i have to read")
            pg = int(input("Please enter the page number:"))
            page = pdfReader.getPage(pg)
            text = page.extractText()
            speak(text)

# to calculate numerical value

        elif "do some calculation" in query or "can you calculate" in query:
            r = sr. Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate, example: 3 plus 3")
                print("listening.....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r. recognize_google(audio)
            print(my_string)

            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    'divided': operator.__truediv__, }[op]

            def eval_binary_expr(op1, oper, op2):  # 5 plus 8
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")

            print(eval_binary_expr(*(my_string.split())))
            speak(eval_binary_expr(*(my_string.split())))
            speak(
                "i am done sir, the calculation is done.now I am ready for next command")


# to weather forecast *********************************************************************************************************

        elif "what is the weather in" in query or "weather in" in query:
            place = query.split(' ')[-1]

            user_api = '34699a951b05e5cc4472544b2cc74a01'
            #location = input("Enter the city name: ")

            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
                place+"&appid="+user_api
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            # create variables to store and display data
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            #date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            print("Current temperature is: {:.2f} deg C".format(temp_city))
            speak("Current temperature is: {:.2f} deg C".format(temp_city))
            print("Current weather desc  :", weather_desc)
            speak(f"Current weather desc  :{weather_desc}")
            print("Current Humidity      :", hmdt, '%')
            speak(f"Current Humidity      :{hmdt}, '%'")
            print("Current wind speed    :", wind_spd, 'kmph')
            speak(f"Current wind speed    :{ wind_spd}, 'kmph'")

        elif 'good bye' in query:
            speak("good bye")
            exit()

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!',
                      'I am nice and full of energy', 'i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information satya and team Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Friday an A I based computer program created by satya but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
   # print(about)
            speak(about)
        elif "hello" in query or "hello sir" in query:
            hel = "Hello  Sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Friday"
            print(na_me)
            speak(na_me)
        elif "how are you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")
        elif query == 'none':
            continue
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'good bye' in query or 'quit' in query:
            ex_exit = 'I feeling very sweet after meeting with you ,please let me know whenever you want something.Thank you'
            speak(ex_exit)
            break

     # TO SHUT DOWN OR RESTART OR SLEEP THE SYSTEM
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
        elif 'restart the system' in query:
            speak("restarting")
            os.system("shutdown /r /t 5")

        elif 'sleep the system' in query:
            speak("sleeping")
            os.system("rundll32.exe powrprof.dill,SetSuspendState 0,1,0")
        else:
            temp = query.replace(' ', '+')
            g_url = "https://www.google.com/search?q="
            res_g = 'sorry! i cant understand '
            speak("sorry sir! I can't understand")
            print(res_g)


if __name__ == "__main__":
    while True:
        Taskexecution()
        permission = takeCommand()
        if "wake up" in permission:
            Taskexecution()
        elif "goodbye" in permission:
            sys.exit()

            # webbrowser.open(g_url+temp)
