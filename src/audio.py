from pydub import AudioSegment

import speech_recognition as sr
import os

def audio_conv(src,dest=os.path.join(os.path.expanduser('~'), 'Downloads')):
    AudioSegment.from_file(src).set_channels(1).export(os.path.join(dest,f"{os.path.basename(src.split('.')[0])}.wav"),format="wav")
    print("\nVideo Conversion completed!\n")
    return os.path.join(dest,f"{os.path.basename(src.split('.')[0])}.wav")


def transcribe(file_path):
    print("Transcribing Audio...\n\n")
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as src:
        audio = r.record(src)

    # Whisper
    return r.recognize_whisper(audio)