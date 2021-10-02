import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listen = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_cmd():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listen.listen(source)
            cmd = listen.recognize_google(voice)
            command = cmd.lower()
            if 'alexa' in cmd:
                cmd = cmd.replace('dunza', '')
                # talk(command)
            return cmd
    except:
        pass

def run_dunza():
    cmd = take_cmd()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play ', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in cmd:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in cmd:
        person = cmd.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me a joke' in cmd:
        joke = pyjokes.get_joke() 
        print(joke)
        talk(joke)
    elif 'thank you' or 'good bye' in cmd:
        exit()
    else:
        error_msg = "Sorry didn't catched that... Please repeat!"
        print(error_msg)
        talk(error_msg)

while True:
    run_dunza()