import yt_dlp as youtube_dl

def download_video(url):
    ydl_opts = {
        'format': 'best',  # Download the best quality available
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the title of the video
        'noplaylist': True,  # Only download a single video, not a playlist
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Por favor, ingresa la URL del video: ")
    download_video(url)
