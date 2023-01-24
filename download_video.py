import youtube_dl

def download_video(url, download_path=None):
    try:
        ydl_opts = {
            'outtmpl': download_path + '/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred: ", e)

# Example usage
url = "https://youtu.be/u2NAuswnTKs"
download_path = "Downloads\pydown"
download_video(url, download_path)


