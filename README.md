# YouTube Playlist Downloader using `yt-dlp`

This Python script downloads videos from a YouTube playlist and saves them in a local directory. The videos are downloaded with the best available video and audio quality and stored in a numbered format (e.g., `1. Video Title.mp4`, `2. Video Title.mp4`, etc.). The folder name is dynamically created using the playlist title.

## Features

- Downloads all videos from a YouTube playlist.
- Saves videos in a directory named after the playlist.
- Downloads videos in the best available format (best video + best audio).
- Shows download progress using `tqdm` for each video.

## Prerequisites

Make sure you have the following installed:

1. **Python 3.12** (or a compatible version)
2. **yt-dlp** (for downloading YouTube videos)
3. **tqdm** (for showing progress bars)

### Install the required packages

You can install the required packages using `pip`:

```bash
pip install yt-dlp tqdm
