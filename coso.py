import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import openai

openai.api_key = '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'

talk("IamJarvis")

engine = pyttsx3.init()

recognizer = sr.Recognizer()

history = []  # List to store the history of questions and answers

def gpt(prompt):
    print("\n\n\n")
    print(history)
    prompt = "answer this in 10 words " + prompt
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
    )

    return response.choices[0].text.strip()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        voice = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(voice).lower()
        if "jarvis" in command:
            command = command.replace("jarvis", "")
            talk(command)
    except sr.UnknownValueError:
        pass

    return command

def run_jarvis():
    command = take_command()
    response = gpt(command)
    print(response)
    talk(response)
    history.append((command, response))

def upw():
    while True:
        try:
            talk("What do you want?")
            run_jarvis()
        except Exception as e:
            print("An error occurred:", str(e))

upw()
