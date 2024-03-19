#PYouTube GUI v1.00 by aiutqmi - Check here for updates! 

import webbrowser
from pytube import YouTube
import tkinter as tk
import os

def download_mp4():
    url = url_entry.get()
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()

    print("Downloading MP4 file...")
    stream.download()
    print("Downloaded Successfully.")

def download_mp3():
    url = url_entry.get()
    video = YouTube(url)
    stream = video.streams.filter(only_audio=True).first()
    outfile = stream.download()
    base, ext = os.path.splitext(outfile)
    newfile = base + '.mp3'
    os.rename(outfile, newfile)

    print("Downloading MP3 file...")
    print("Downloaded Successfully.")

def open_link():
    webbrowser.open("https://aiutqmi.github.io")

window = tk.Tk()
window.title("PYouTube by aiutqmi")
window.geometry("720x480")  
window.configure(bg="#333333")  


title_label = tk.Label(window, text="PYouTube GUI", font=("Helvetica", 18, "bold"), fg="#FF3399", bg="#333333")
title_label.pack(pady=20)


url_label = tk.Label(window, text="Enter a YouTube Video URL:", font=("Helvetica", 12), fg="#FF3399", bg="#333333")
url_label.pack()
url_entry = tk.Entry(window, font=("Helvetica", 12), width=50)
url_entry.pack()


mp4_btn = tk.Button(window, text="MP4", command=download_mp4, width=18, height=2, font=("Helvetica", 12, "bold"), fg="#FFFFFF", bg="#FF3399")
mp4_btn.pack(pady=10)

mp3_btn = tk.Button(window, text="MP3", command=download_mp3, width=18, height=2, font=("Helvetica", 12, "bold"), fg="#FFFFFF", bg="#FF3399")
mp3_btn.pack()

link_label = tk.Label(window, text="Click here to check all my projects!", font=("Helvetica", 10), fg="#FF3399", bg="#333333", cursor="hand2")
link_label.pack(side="bottom", pady=10)
link_label.bind("<Button-1>", lambda e: open_link())

developed_by_label = tk.Label(window, text="v1.00\nDeveloped by aiutqmi", font=("Helvetica", 10, "italic"), fg="#FF3399", bg="#333333")
developed_by_label.pack(side="bottom", pady=10)

window.mainloop()