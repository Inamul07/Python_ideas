import pytube from YouTube
video = YouTube("#link")
video.streams.get_highest_resolution().download()
