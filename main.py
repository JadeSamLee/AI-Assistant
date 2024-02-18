import os
import time
import pyaudio
import playsound 
from gtts import gTTS 
import openai
import speech_recognition as sr

api_key=""

lang='en'

openai.api_key=api_key

while True:
    def get_audio():
        ar=sr.Recognizer()
        with sr.Microphone() as source:
            audio=ar.listen(source)
            voiced=""

            try:
                voiced=ar.recognize_google(audio)
                print(voiced)

                if "John" in voiced:
                    completion=openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":voiced}])
                    text=completion.choices[0].message.content
                    speech=gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    speech.save("response_audio.mp3")
                    playsound.playsound("response_audio.mp3")

            except Exception:
                print("Exception detected")

        return voiced
    
    get_audio()


