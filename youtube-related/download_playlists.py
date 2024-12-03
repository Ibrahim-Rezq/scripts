import yt_dlp
import os

# Function to download and rename videos
def download_playlist(playlist_url, download_path):
    # Set options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # You can change this to '360p' if needed
        'outtmpl': os.path.join(download_path, '%03d - %(title)s.%(ext)s'),
        'noplaylist': False,         # Ensure that playlist is downloaded
        'merge_output_format': 'mp4',  # Force output format to mp4
    }

    # Download playlist using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Input your playlist URL and download path here
# playlist_url = input("Enter the YouTube playlist URL: ")
download_path = input("Enter the download directory path: ")

# Download the playlist
download_playlist("https://www.youtube.com/playlist?list=PL2hoGhz2jBSqpWTv6svf4e3HCtPMwqY0g", download_path)
