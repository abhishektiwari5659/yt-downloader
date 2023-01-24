
# YouTube Video Downloader

This is a simple script that uses the youtube_dl library to download a video from YouTube and convert it to an mp3 file.






## Features

- Downloads YouTube videos and converts them to mp3 format.

- Allows you to specify a download path to save the downloaded video (optional).

- Uses the 'bestaudio/best' format and 'FFmpegExtractAudio' post-processor to extract the audio from the video and convert it to an mp3 file.

- Can be easily modified to download videos in different formats or quality by adjusting the options in the ydl_opts variable.

- Prints a message indicating if the video was downloaded successfully or if an error occurred.

- Easy to use and understand the code.

- Can be integrated with other projects.

- Can handle the exception.

- Can work in any platform that supports python and ffmpeg.

## Usage/Examples
Install the required libraries by running pip install youtube_dl in your command prompt.

Replace the url variable with the YouTube video URL that you want to download.

Replace the download_path variable with the path where you want to save the downloaded video (optional).

Run the script by executing python download_video.py in your command prompt.

The script will download the video and convert it to an mp3 file with a 192 kbps bitrate and save it in the specified download path. The file name will be the title of the video


Example:

url = "https://yourvideolink/

download_path = "Downloads\pydown"

download_video(url, download_path)

This will download the video at the given url and save it in the "Downloads\pydown" location with the title of the video as the file name

## Notes

The script uses the 'bestaudio/best' format and 'FFmpegExtractAudio' post-processor to extract the audio from the video and convert it to an mp3 file.

If you want to download the video in a different format or quality, you can adjust the options in the ydl_opts variable accordingly.

If you want to handle the exception, you can add code for handling the exception and remove the print statement in catch block.

Make sure that you have ffmpeg installed in your computer if you want to convert the video to mp3.
## Conclusion
This script is a simple example of how to use the youtube_dl library to download videos from YouTube and convert them to other formats. You can use this script as a starting point for your own projects or modify it to suit your needs.
## Author

- HeheAbhi(https://github.com/abhishektiwari5659)

