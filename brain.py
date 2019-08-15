import speech_recognition as sr
import os
import win32com
import win32com.client as wincl
import time
import pyjokes

recognition = sr.Recognizer()
default_mic = sr.Microphone()
speaker = win32com.client.Dispatch("SAPI.SpVoice")
voice_control = True


def activate(phrase='online', active=None):
    try:
        with default_mic as activate_source:
            recognition.adjust_for_ambient_noise(activate_source)
            activate_audio = recognition.listen(activate_source)
            try:
                activate_output = recognition.recognize_google(activate_audio)
            except:Exception
            if activate_output == phrase:
                print('Listening')
                speaker.Speak("Im listening")
                speaker.Speak("please say, shutdown computer, restart computer, name, tell me a joke")
                return False
            else:
                print('Not Listening')
                return False
    except:Exception


def control():
    while activate:
        with default_mic as source:
            recognition.adjust_for_ambient_noise(source)
            audio = recognition.listen(source)
            try:
                output = recognition.recognize_google(audio)
            except: Exception
        if output == 'shutdown computer':
            speaker.Speak("Shutting down computer")
            time.sleep(5)
            os.system('shutdown /s /t 1')
        elif output == 'restart computer':
            speaker.Speak("Restarting computer")
            time.sleep(5)
            os.system('shutdown /r /t 1')
        elif output == 'name':
            name()
        elif output == 'tell me a joke':
            joke()
        else:
            print(output)


def name():
    speaker.Speak("What is your name")
    with default_mic as source:
        audio = recognition.listen(source)
    try:
        name = recognition.recognize_google(audio)
        speaker.Speak(f"Hello {name}")
    except:Exception


def joke():
    jokes = (pyjokes.get_joke())
    speaker.Speak(jokes)
