import os
import yt_dlp
from tqdm import tqdm

def download_youtube_playlist(playlist_url, download_dir='Download'):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Options for yt-dlp to use a format that works
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Fallback to best available if the best is not available
        'outtmpl': os.path.join(download_dir, '%(playlist_index)s. %(title)s.%(ext)s'),
        'noplaylist': False,  # Enable playlist downloading
        'progress_hooks': [progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the playlist
        ydl.download([playlist_url])

def progress_hook(d):
    if d['status'] == 'downloading':
        pbar.update(1)
    elif d['status'] == 'finished':
        pbar.close()
        print(f"Download complete: {d['filename']}")

# Example usage
playlist_url = 'https://youtube.com/playlist?list=PLwmVgOWoXWb_2nZ1FvrHVRinQfaHhaCo3&si=cEPqhah8-xg7YADt'
with tqdm(total=100) as pbar:  # Initialize progress bar with dummy total
    download_youtube_playlist(playlist_url)
