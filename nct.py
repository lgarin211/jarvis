import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import openai

openai.api_key = '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'

print("Jarvis")
MASTER = "Augustinus"

engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()

def gpt(prompt, history):
    prompt = "answer this in 10 words " + prompt
    history += f"(You:{prompt})\n"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=history,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
    )
    history += f"(Jarvis:{response.choices[0].text.strip()})\n"
    return response.choices[0].text.strip(), history

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour

    if hour < 12:
        talk(f"Hello Good Morning {MASTER}")
    elif hour < 18:
        talk(f"Hello Good Afternoon {MASTER}")
    else:
        talk(f"Hello Good Evening {MASTER}")

def take_command():
    with sr.Microphone() as source:
        print("Listening")
        voice = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(voice).lower()
        if "jarvis" in command:
            command = command.replace("jarvis", "")
            talk(command)
    except:
        pass

    return command

def run_jarvis(history):
    command = take_command()
    response = ""
    if 'play' in command:
        song = command.replace("play", "")
        talk(f"Playing {song}")
        print(f"Playing {song}")
        pywhatkit.playonyt(song)
        response = f"Playing {song}"

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk(f"The time now is {time}")
        response = f"The time now is {time}"

    elif "wikipedia" in command:
        src = command.replace("wikipedia", "")
        info = wikipedia.summary(src, sentences=1)
        talk("Searching Wikipedia")
        print(info)
        talk(info)
        response = info
    else:
        response, history = gpt(command, history)
        print(response)
        response = response.replace("Jarvis:", "")
        talk(response)

    return history

def upw():
    history = 'Chat history:\n'

    while True:
        try:
            print("\n\n\n" + history)
            talk("What do you want?")
            history = run_jarvis(history)
        except Exception as e:
            print("An error occurred:", str(e))

upw()
