import pywhatkit as wht
import speech_recognition as sr
import pyttsx3
import datetime

# Get current time

dt = datetime.datetime.now()
hr = dt.hour
min = dt.minute
print(f"{hr}:{min}")

#intzi txt to speech as engine and change the voice into female

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',200)

#talk & write
def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def recognize_speech():
    x = sr.Recognizer()
    with sr.Microphone() as source:     # using microphone as source
        print('Listening...')
        voice = x.listen(source,timeout=5,phrase_time_limit=10)  # using x and listen the source and store it in the variable
        command = x.recognize_google(voice)  # recognize by google and store it as command
        command = command.lower()
        return command

def sry():
    speak("Sorry master, I don't understand")

#use cases
def operations(command):

    if any(word in command for word in ['hello', 'hi', 'hi']):
        speak("hello master , How can i help you today ?")

    elif any(word in command for word in ['play', 'song', 'movie']):
        for word in ['play', 'song', 'movie']:
            command = command.replace(word, '')
        speak("Playing " + command)
        wht.playonyt(command)

    elif 'time' in command:
        speak(f"Time is {hr}:{min}")

    elif any(word in command for word in ['what', 'when', 'who', 'how']):
        speak("Searching " + command)
        wht.search(command)

    elif 'screenshot' in command:
        speak("Taking a screenshot")
        wht.take_screenshot("Screenshot",2,True)

    elif 'message' in command:
        speak("What is the number master")
        num = recognize_speech()
        country_code = "+91 "
        num = country_code + num
        print(num)
        speak("What is the message master")
        msg = recognize_speech()
        print(msg)
        speak("Sending message")
        wht.sendwhatmsg_instantly(num,msg,10)

    else:
        sry()

def start():
        #wellcoming us
        if hr < 12:      # morning
            speak("Good morning master , How can i help you today ?")
        elif 11 < hr < 16:       #afternoon
            speak("Good afternoon master , How can i help you today ?")
        elif hr > 15:        #evening
            speak("Good evening master , How can i help you today ?")

        # create a variable for recognizers
        #x = sr.Recognizer()
        while True:
            try:
                command = recognize_speech()
                print(command)
                if any(word in command for word in ['bye','exit','off','goodbye']):
                    speak("Goodbye , Master...!")
                    break
                else:
                    operations(command)

            except:
                speak("Sorry master , i can't hear you")

start()