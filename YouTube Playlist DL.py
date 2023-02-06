from pytube import YouTube, exceptions, Playlist


playlist = Playlist('insert Youtube playlist URL')
print(f'Downloading: {playlist.title}')

output = 'your output path'
for url in playlist.video_urls:
    print(url)
    try:
        video = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    except execeptions.VideoUnavailable:
        print('Error Downloading Video')
        pass # Error loading single video
    else:
        video.streams.filter(type='video', progressive=True, file_extension='mp4').first().download(output)
     
print('Download complete!')   
     
     
