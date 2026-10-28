import yt_dlp

video_url = "https://www.youtube.com/shorts/lAn_EMae_Uo"

options = {
    "format": "bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s",
    "ffmpeg_location": r"C:\ffmpeg\bin",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([video_url])
print("Download complete!")
