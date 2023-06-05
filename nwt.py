import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import openai
openai.api_key = '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'

print("Jarvis")
MASTER = "Augustinus"

engine = pyttsx3.init("sapi5")
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

mendengarkan = sr.Recognizer()

def gpt(prompt,hipos):
    prompt="answert this in 10 word "+prompt
    hipos+=hipos+"("+MASTER+":"+prompt+")\n"
    response = openai.Completion.create(
        engine='text-davinci-003',  # Ganti dengan model yang Anda inginkan
        prompt=hipos,
        max_tokens=50,  # Ganti sesuai kebutuhan
        temperature=0.7,  # Ganti sesuai kebutuhan
        n=1,
        stop=None,
    )
    hipos+="(Jarvis:"+response.choices[0].text.strip()+")\n"
    return response.choices[0].text.strip()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        talk("Hello Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        talk("Hello Good Afternoon" + MASTER)
    else:
        talk("Hello Good Evening" + MASTER)

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice = mendengarkan.listen(source)
            command = mendengarkan.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                print(command)
                command = command.replace("jarvis", "")
                talk(command)
                
    except:
        pass

    return command

def run_jarvis(dos):
    
    command = take_command()
    if 'play' in command:
        song = command.replace("play", "")
        talk("Playing"+ song)
        print("Playing"+ song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("The time now is "+ time)
    elif "wikipedia" in command:
        src = command.replace("wikipedia", "")
        info = wikipedia.summary(src, sentences=1)
        talk("Searching Wikipedia")
        print(info)
        talk(info)
    elif "jarvis":
        print(command)
        res=gpt(command,dos)
        print(res)
        talk(res)
    else:
        talk("Not any instruction")
        print(command)

# ret=gpt("How to make apel pie")
# print(ret)
# talk(ret)

wishMe()
def upw():
    history='history chat: \n'
    while True:
        try:
            print("\n\n\n"+history)
            talk("What do you want?")
            run_jarvis(history)
        except Exception as e:
            print("An error occurred:", str(e))
upw()