import speech_recognition as sr  # this module is used for speech recognitiom
import pyttsx3   # this module has lots of voices in it
import pywhatkit
import datetime
import wikipedia
import pyjokes
import 

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)     

def talk(text):
    engine.say(text)
    engine.runAndWait()


engine.say("I am your jinniee ")
engine.say("what can I do for you pretty lady!!")
engine.runAndWait()
def alexa_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)

        
    except :
         pass
    return command

def run_alexa():
    command=alexa_command()
    if 'play' in command:
        song=command.replace("play","")
        talk('playing music'+song)
        print("playing")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%H:%M:%S")
        talk('Current time is'+time)
        print("Time is",time)
    elif 'date' in command:
        date=datetime.datetime.now().strftime("%d/%m/%Y")
        talk('The date is'+date)
        print("date is"+date)       
    elif 'superstar' in command:
        person=command.replace('superstar',"")
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
run_alexa()
