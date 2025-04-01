import speech_recognition as sr
import pyaudio 
import wave
import os
import sys
from vosk import Model, KaldiRecognizer
import json
import time
from pynput import keyboard



def check_model() -> bool:
    if not os.path.exists("model"):
        print("Vosk model not found. \n "
        "Download it and unpackage it into model folder. \n"
        "https://alphacephei.com/vosk/models")
        os.mkdir("model")
        return False
    return True

def get_text_from_microphone(time = 10, threshold = 2000) -> str:
    if not check_model():
        return 0 
    rec = sr.Recognizer()
    rec.energy_threshold = threshold
    with sr.Microphone() as source:
        print("Recording in progress...")
        audio = rec.listen(source, time)
    try:
        text = rec.recognize_vosk(audio)
        text_json = json.loads(text)
        clean_text = text_json["text"]
        return clean_text
    except sr.UnknownValueError:
        print("Vosk could not understand audio.")
        return 0
    except sr.RequestError as e:
        print(f"Vosk error: {e}")
        return 0
    
def on_press(key):
    if key == keyboard.KeyCode(char = "v"):
        call_assistant()
    if key == keyboard.KeyCode(char = "e"):
        exit()

def call_assistant() -> None:
    text = get_text_from_microphone().split()
    # call func that chekcs keywords
    print(text)