from moviepy.editor import VideoFileClip

def extract_audio(video_path: str, output_audio_path: str):
    """
    Extracts audio from a video file and saves it as an audio file.

    Parameters:
    video_path (str): The path to the input video file.
    output_audio_path (str): The path to the output audio file.
    """
    # Load the video file
    video = VideoFileClip(video_path)

    # Extract the audio from the video
    audio = video.audio

    # Write the audio to a file
    audio.write_audiofile(output_audio_path)

    # Close the video file
    video.close()