from pytube import YouTube
from colorama import Fore
def download_youtube_video(url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Print some details about the video
        print(f'Title: {yt.title}')
        print(f'Author: {yt.author}')
        print(f'Views: {yt.views}')
        print(f'Duration: {yt.length} seconds')

        # Download the video
        print('Downloading...')
        stream.download(output_path=output_path)
        print('Download completed!')

    except Exception as e:
        print(Fore.RED + f'An error occurred: {e}, report to walper either on github (on the official repo) or on discord (walper)' + Fore.RESET)

# Example usage
if __name__ == '__main__':
    video_url = input("The URL for your video: ")
    download_youtube_video(video_url)
