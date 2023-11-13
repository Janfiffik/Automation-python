from pytube import YouTube
import schedule
import time

# List of videos for downloading audio only.
audiobooks_to_download = [
                          "https://www.youtube.com/watch?v=Eqjxlhed1x8",
                          "https://www.youtube.com/watch?v=moX6LtCjZvs",
                          "https://www.youtube.com/watch?v=2kZXaf8HaOc"
                          ]

START_DOWNLOAD = "13:28"


def download_audio(audio_list):
    link = audio_list[0]
    yt = YouTube(link)
    audio = yt.streams.get_audio_only()
    audio.download()
    audio_list.pop(0)


schedule.every().day.at(START_DOWNLOAD).do(lambda: download_audio(audiobooks_to_download))

while True:
    schedule.run_pending()
    time.sleep(1)
