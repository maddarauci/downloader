#download pytube with pip install pytube
import pytube

#made it a function so that you can call it from any script and just pass in
#the url in ""
url = input("enter url: ")
def downloadVideo(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    print(video.title)
    video.download()
    
downloadVideo(url)
print("download completed!!")
