from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed")

save = "C:/Users/Andrew/Download"

print(video.title)

videoDownload = video.streams.get_highest_resolution()

videoDownload.download(save)