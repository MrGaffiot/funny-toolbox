from moviepy.editor import *

def merge_image_and_audio(image_path, audio_path, output_path):
    # Load the image
    image_clip = ImageClip(image_path)

    # Load the audio
    audio_clip = AudioFileClip(audio_path)

    # Set the duration of the image clip to match the audio duration
    image_clip = image_clip.set_duration(audio_clip.duration)

    # Set the audio of the image clip
    video_clip = image_clip.set_audio(audio_clip)

    # Write the result to a file
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
