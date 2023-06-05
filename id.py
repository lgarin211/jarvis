import os
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import openai

openai.api_key = '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'

engine = pyttsx3.init()

recognizer = sr.Recognizer()

history = ['History']

def gpt(prompt):
    print("\n\n\n")
    # clear windows
    os.system("clear")
    print(history)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7,
        n=1,
        stop=None,
    )

    return response.choices[0].text.strip()

def talk(text):
    engine.say(text)
    sw=str(datetime.datetime.now().timestamp())
    print(sw)
    engine.save_to_file(text, '/DOM/output'+sw+'.mp3')
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Mendengarkan...")
        recognizer.adjust_for_ambient_noise(source)
        voice = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(voice, language="id-ID").lower()
        if "jarvis" in command:
            command = command.replace("jarvis", "")
            talk(command)
    except sr.UnknownValueError:
        pass

    return command

def run_jarvis():
    command = take_command()
    response = gpt("Answert this on 10 word "+command)
    print(response)
    talk(response)
    history.append(list(map(str, (command, response))))

def upw():
    talk("Hai Saya Jarvis, Senang membantumu ")
    while True:
        try:
            talk("Any Question?")
            run_jarvis()
        except Exception as e:
            print("Terjadi kesalahan:", str(e))

os.system("pip install speech_recognition")
upw()
