from requests.exceptions import MissingSchema
from pytube.exceptions import RegexMatchError
from pydub.exceptions import CouldntDecodeError
import os
from text_content_generator import youtube
from text_content_generator import audio
from text_content_generator import webpage
from text_content_generator import pdf

def generate_content():
    transcript = ""
    while (True):
        i = int(input(
            f"Generating Content\n\n1. YouTube Video URLs\n2. Local Audio/Video Files\n3. Upload PDF Files\n4. Web Article URL\n0. Quit\n\nSelect an option: "))

        if i == 1:
            try:
                url = input("Please enter the video URL : ").strip()
                transcript += youtube.youtube_script(url) + "\n\n"

            except RegexMatchError as rex:
                print("\nPlease enter a valid URL!\n")

            except:
                print("\nSubtitles are disabled for this video!\n")

                conf = input("Would you like to download and transcribe instead?\n (y/n) : ")[0].lower()
                if conf == 'y':
                    vid_path = youtube.yt_download(url)
                    audio_path = audio.audio_conv(vid_path)
                    transcript += audio.transcribe(audio_path) + "\n\n"
                    os.remove(vid_path)
                    os.remove(audio_path)

                elif conf == 'n':
                    print("\n")

        elif i == 2:
            path = input("Please enter file Path : ").strip()
            '''
    
                add code logic to check if the file entered 
                    is correct video or audio format
    
            '''

            try:
                transcript += audio.transcribe(audio.audio_conv(path)) + "\n"
            except CouldntDecodeError:
                print("\nThe file provided could not be decoded.\nPlease make sure to insert only .mp4 and .mp3 files.\n")
            except FileNotFoundError:
                print("\nNo such file directory exists!!\n")

        elif i == 3:
            try:
                file = input("PDF File Path : ").strip()
                transcript += pdf.pdf_read(file) + "\n\n"
            except FileNotFoundError:
                print("\nNo such file directory exists!!\n")


        elif i == 4:
            try:
                address = input("Website URL : ").strip()
                print("\nGetting Website Content...\n")
                transcript += webpage.read_pages(address) + "\n\n"
            except MissingSchema:
                print("\nInvalid Address provided!\n")

        elif i == 0:
            print("\n---QUITING!---\n")
            break

        else:
            print("\nPlease enter a VALID OPTION!\n")
    return transcript

print(generate_content())