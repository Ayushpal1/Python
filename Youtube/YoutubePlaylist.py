import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = 'D:/Songs/playlist'

playlist = Playlist('https://youtube.com/playlist?list=PLCFQY6TpJRfBpiG4ANaV8F__AQUhdbps8')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

# physically downloading the audio track
for video in playlist.videos:
    print(video.title)
    print(video.age_restricted)
    if video.age_restricted == True:
        continue
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)