import os
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import openai

class App:
    
    def __init__(self):    
        openai.api_key = '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'
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.history = []
        
    def gpt(self, prompt):
        print("\n\n\n")
        print(self.history)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7,
            n=1,
            stop=None,
        )
        
        return self.response.choices[0].text.strip()
    
    def take_command(self):
        with sr.Microphone() as source:
            print("Mendengarkan...")
            self.recognizer.adjust_for_ambient_noise(source)
            voice = self.recognizer.listen(source)
        try:
            self.command = self.recognizer.recognize_google(voice, language="id-ID").lower()
            if "jarvis" in self.command:
                self.command = self.command.replace("jarvis", "")
                self.talk(self.command)
        except sr.UnknownValueError:
            pass

        return self.command
    def talk(self, text):
        self.engine.say(text)
        sw=str(datetime.datetime.now().timestamp())
        print(sw)
        self.engine.save_to_file(text, '/DOM/output'+sw+'.mp3')
        self.engine.runAndWait()
        
    def run_jarvis(self):
        self.command = "Jawab ini dalam 10 kata" + self.take_command()
        self.response = self.gpt(self.command)
        self.history.append(self.command+self.response)
        
    def run(self):
        self.talk("Hai Saya Agus, Senang Membantu!")
        while True:
            try: 
                self.talk("Lagi?")
                self.run_jarvis()
            except Exception as e:
                print(f"Terjadi kebodohan : {str(e)}")

temp = App()
temp.run()

        
        
        
        
    
        