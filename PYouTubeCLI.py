from pytube import YouTube

print('PYDL')
url = input("Enter a YouTube Video URL: ")
extension = input("Type 1 to get the MP4 file or 2 to get the MP3 one. ")

if extension == '1':
    video = YouTube(url)
    print("Downloading MP4 file...")
    stream = video.streams.get_highest_resolution()
    stream.download()
    print("Downloaded Successfully.")
elif extension == '2':
    video = YouTube(url)
    print("Downloading MP3 file...")
    stream = video.streams.filter(only_audio=True).first()
    outfile = stream.download()
    base, ext = os.path.splitext(outfile)
    newfile = base + '.mp3'
    os.rename(outfile, newfile)
    print("Downloaded Successfully.")
else:
    print('Invalid Extension.')

break
