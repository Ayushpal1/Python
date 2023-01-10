from pytube import YouTube
import sys

#music Class
class Audio:

    def displayQuality():
        streams = audio.streams.filter(only_audio=True)
        for i in streams:
            print(i)
    
    PATH = "D:/Songs/playlist"
    def __init__(self,link):
        self.link = link
        self.audio = YouTube(self.link)
        print(self.audio.title)
        streams = self.audio.streams.filter(only_audio=True)
        for i in streams:
            print(i)
        #self.displayQuality()
        print("Enter the itag of the Qualtiy : ")
        q = int(input())
        try:
            self.audio.streams.get_by_itag(q).download(PATH)
            print("done")
        except Exception as e:
            print(e)
            print("download failed")

#video Class
class Video:

    PATH = "D:/Songs/playlist"
    def __init__(self, link):
        self.link = link
        self.video = YouTube(self.link)
        print(self.video.title)
        streams = self.video.streams.filter(mime_type="video/mp4")
        for i in streams:
            print(i)
        # self.displayQuality()
        print("Enter the itag of the Qualtiy : ")
        q = int(input())
        try:
            self.video.streams.get_by_itag(q).download("D:/Songs/playlist")
            print("done")
        except Exception as e:
            print(e)
            print("download failed")





#take input from the user
PATH = "D:/Songs/playlist"

link = input("Enter the link : ")
#print(" you chose ",sys.argv[1])
#video = YouTube(sys.argv[1])

#S = "https://www.youtube.com/watch?v=Ai47BcMrsXw"
print(" you chose ",link)
video = YouTube(link)


print(video.title)
#print(video.video_id)
#print(video.age_restricted)


#video.streams.all()
stream = video.streams.all()
for i in stream:
    print(i)

print("Choose the itag from above : ")
code = int(input())
video.streams.get_by_itag(code).download(PATH)

print("File downloaded at ",PATH)