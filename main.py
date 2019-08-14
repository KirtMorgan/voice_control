import speech_recognition as sr
import os

recognition = sr.Recognizer()
default_mic = sr.Microphone()
voice_control = True


def activate(phrase='hello'):
    try:
        with default_mic as activate_source:
            recognition.adjust_for_ambient_noise(activate_source)
            activate_audio = recognition.listen(activate_source)
            try:
                activate_output = recognition.recognize_google(activate_audio)
            except:
                Exception
            if activate_output == phrase:
                print('Listening')
                return True
            else:
                print('Not Listening')
                return False

    except:
        Exception


while voice_control:
    activate()
    while activate:
        with default_mic as source:
            recognition.adjust_for_ambient_noise(source)
            audio = recognition.listen(source)
            try:
                output = recognition.recognize_google(audio)
            except: Exception
        if output == 'shutdown computer':
            os.system('shutdown /s /t 1')
        elif output == 'restart computer':
            os.system('shutdown /r /t 1')
        else:
            print(output)
