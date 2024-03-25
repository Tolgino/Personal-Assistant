import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from googletrans import Translator

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
alex = voices[0].id
samantha = voices[33].id
victoria = voices[41].id
yelda = voices[43].id
engine.setProperty('voice', yelda)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="tr-TR")
            command = command.lower()
            if 'yelda' in command:
                command = command.replace('yelda', '')
                print(command)
            else:
                print(command)
    except:
        pass
    return command


def runEnglish():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Time is ' + time)
    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 1)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'name' in command:
        talk('my name is slim shady')
    else:
        talk('Please say it again')

def runTurkish():
    command = take_command()
    if 'çal' in command:
        song = command.replace('çal', '')
        talk(song + 'çalınıyor')
        pywhatkit.playonyt(song)
    elif 'saat' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Saat ' + time)
    elif 'ne demek' in command:
        thing = command.replace('ne demek', '')
        info = wikipedia.summary(thing, 1)
        talk(info)
    elif 'kim' in command:
        person = command.replace('kim', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'şaka' in command:
        joke()
    else:
        talk('Lütfen tekrar söyleyin')

def joke():
    joke = pyjokes.get_joke()
    translator = Translator()
    saka = translator.translate(joke, dest='tr')
    talk(saka.text)

#live news, calculator, near places, movies, weather-wolframaplha python ekle


while True:
    #runTurkish()
    #joke()