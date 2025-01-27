# SPEAK FUNCTIONALITY

# to make JARVIS speak
import pyttsx3 

# to recognize speech from microphone
import speech_recognition as sr

# importing random for songs
import random

# web browser for songs, this is inbuilt 
import webbrowser

# date and time module
import datetime

# notification for mobile phone
from plyer import notification

# to open any apps
import pyautogui

#to open wikipedia
import wikipedia

#to send whatsapp message
import pywhatkit as pwk

import user_config

import smtplib,ssl

import openai_request as ai

# import image_generation

import mtranslate

# initializing this library
engine = pyttsx3.init()

# getting voices property from this library
voices = engine.getProperty('voices')       

# setting the property of voice
engine.setProperty('voice', voices[0].id)

# setting the rate/speed of voice
engine.setProperty("rate", 170) 


# function to make JARVIS speak any command
def speak(audio):
    audio= mtranslate.translate(audio,to_language="hi", from_language="en-in")
    engine.say(audio)
    engine.runAndWait()


# function to recognize voice commands
def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            content = r.recognize_google(audio, language='en-in')
           
            content = mtranslate.translate(content,to_language='en-in')
            print("You said: " + content)
        except Exception as e:
            print("Please try again...!")

    return content


# main process to handle commands
def main_process():
    jarvis_chat=[]
    while True:
        request = command().lower()

        if "hello" in request:
            speak("Welcome, how can I help you today")
        
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1, 3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=K4DyBUG242c&list=RDQMTgh66LaGkb4&start_radio=1")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=3nQNiWdeH2Q&list=RDQMTgh66LaGkb4&index=3")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=TW9d8vYrVFQ&list=RDQMTgh66LaGkb4&index=7")
        
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
        
        elif "say date" in request:
            now_date = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is " + str(now_date))
        
        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task != "":
                speak("Adding task " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")
        
        elif "speak task" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read().strip()
                if tasks:
                    speak("Work we have to do today is: " + tasks)
                else:
                    speak("There are no tasks in the to-do list.")
            except FileNotFoundError:
                speak("The to-do list file is not found.")
        
        elif "list" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read().strip()
                if tasks:
                    notification.notify(
                        title="Today's Work",
                        message=tasks,
                        timeout=10  # Notification duration in seconds
                    )
                    speak("Showing today's work in a notification.")
                else:
                    speak("There are no tasks in the to-do list.")
            except FileNotFoundError:
                speak("The to-do list file is not found.")
        elif "open youtube" in request:
          webbrowser.open("www.youtube.com")
        
        elif "open" in request:
            query = request.replace("open", "").strip()
            if query:
                speak(f"Opening {query}")
                pyautogui.press("super")  # Press Windows key
                pyautogui.sleep(1)  # Give time for the Start Menu to open
                pyautogui.typewrite(query)
                pyautogui.sleep(2)  # Allow time for search results
                pyautogui.press("enter")  # Select and open the application
            else:
                speak("Please specify what you want to open.")

        elif "wikipedia" in request:
          request=request.replace("jarvis ","")
          request=request.replace("search wikipedia ","")
          result=wikipedia.summary(request, sentences=2)
          speak(result)
        elif "search google" in request:
          request=request.replace("jarvis ","")
          request=request.replace("search google ","")
          webbrowser.open("https://www.google.com/search?q="+request)
        elif "send whatsapp" in request:
          pwk.sendwhatmsg("number", "Hi", 12, 26,30)
        elif "send mail" in request:
            pwk.send_mail("richuuka009@gmail.com", user_config.gmail_pass, "hello" ,"Hello,How are you?","rishikach009@gmail.com") 
            speak("Email sent")
#         elif "send mail" in request:
#             s=smtplib.SMTP('smtp.gmail.com','587')
#             s.starttls()
#             s.login("richuuka009@gmail.com","hehe0090")
#             message= """
# This is the message
# Thank you.
# """          
#             s.sendmail("richuuka009@gmail.com","rishikachaudharyyyy@gmail.com",message)
#             s.quit()
#             speak("Email sent")

        # elif "generate image" in request:
        #     request=request.replace("jarvis","")
        #     image_generation.generate_image(request)

        elif "ask ai" in request:
            
            request=request.replace("jarvis","")

            request=request.replace("ask ai","")

            print(request)

            response=ai.send_request(request)
            print(response)
            speak(response)
        elif "clear chat" in request:
            jarvis_chat=[]
            speak("Chat cleared")
        else:
            
            request=request.replace("jarvis","")

            

            
            jarvis_chat.append({"role": "user","content": request})
         

            response=ai.send_request2(jarvis_chat)

            jarvis_chat.append({"role":"assistant", "content":response})

           
            speak(response)


            
            
          
        

# Run the main process
main_process()
