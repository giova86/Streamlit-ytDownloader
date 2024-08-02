# YouTube Playlist to MP3 Downloader

This Streamlit application allows users to download audio tracks from a YouTube playlist in MP3 format. It uses the `yt-dlp` library for downloading and converting the videos to MP3.

## Features

- Download entire YouTube playlists as MP3 files.
- Convert downloaded videos to MP3 with a specified quality.
- Log errors in a file for troubleshooting.
- Simple and user-friendly web interface.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/youtube-playlist-mp3-downloader.git
    cd youtube-playlist-mp3-downloader
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Open the web application in your browser.**
   The Streamlit application will run locally and can be accessed at `http://localhost:8501` by default.

