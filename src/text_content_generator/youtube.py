import os

from pytube import YouTube
from pytube import Search

from youtube_transcript_api import YouTubeTranscriptApi

def yt_download(url,dest=os.path.join(os.path.expanduser('~'), 'Downloads')):
    yt = YouTube(url)
    print(f"\nDownloading {yt.title} ...")
#     print(f"Thumbnail {yt.thumbnail_url}")
    path = yt.streams.get_highest_resolution().download(output_path=dest)
    print("\nDone!")
    return path

def search_yt(query,num=10):
    return [{'title':x.title,'url':x.watch_url} for x in Search(query).results[:num]]

def search_and_download(query,num=5,output_path=os.path.join(os.path.expanduser('~'), 'Downloads')):
    videos = search_yt(query)[:num]
    for x in range(len(videos)):
        print(f"{x} : {videos[x]['title']}")
    user = [int(u) for u in input("Enter Selection : ").strip().split(",")[:num]]
    for i in user:
        yt = YouTube(videos[i]['url'])
        stream = yt.streams.get_highest_resolution()
        print("Downloading:", yt.title)
        # make it selectable by the user
        stream.download(output_path=output_path)
        print("Download complete!")


def youtube_script(url):
    try:
        yt = YouTube(url)
        srt = "".join([text["text"] + '\n' for text in YouTubeTranscriptApi.get_transcript(yt.video_id,languages=['en'])])
    except:
        yt = YouTube(url)
        srt = "".join([text["text"] + '\n' for text in YouTubeTranscriptApi.get_transcript(yt.video_id)])
    return srt
