import click
from . import imageSeparator as separator
from . import ytinstaller as downloader
import os
from colorama import Fore

line1 = "      ___           ___           ___           ___           ___       ___     "
line2 = "     /\  \         /\  \         /\  \         /\  \         /\__\     /\  \    "
line3 = "    /::\  \        \:\  \       /::\  \       /::\  \       /:/  /    /::\  \   "
line4 = "   /:/\:\  \        \:\  \     /:/\:\  \     /:/\:\  \     /:/  /    /:/\ \  \  "
line5 = "  /::\~\:\  \       /::\  \   /:/  \:\  \   /:/  \:\  \   /:/  /    _\:\~\ \  \ "
line6 = " /:/\:\ \:\__\     /:/\:\__\ /:/__/ \:\__\ /:/__/ \:\__\ /:/__/    /\ \:\ \ \__\\"
line7 = " \/__\:\ \/__/    /:/  \/__/ \:\  \ /:/  / \:\  \ /:/  / \:\  \    \:\ \:\ \/__/"
line8 = "      \:\__\     /:/  /       \:\  /:/  /   \:\  /:/  /   \:\  \    \:\ \:\__\  "
line9 = "       \/__/     \/__/         \:\/:/  /     \:\/:/  /     \:\  \    \:\/:/  /  "
line10 = "                                \::/  /       \::/  /       \:\__\    \::/  /   "
line11 = "                                 \/__/         \/__/         \/__/     \/__/    "
ascii_art_lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11]

def cprint(text: str, size=os.get_terminal_size().columns):
    print(text.center(size, " "))

def start():
    size = os.get_terminal_size().columns
    for line in ascii_art_lines:
        print(line.center(size, " "))
    cprint("Welcome to ftools (short for funny tools)! This is just a small project by me (walper),", size=size)
    cprint("So don't expect anything crazy.", size=size)
    cprint("List of features:", size=size)
    cprint("separate: separates parts of images that are not connected into multimple images")
    cprint("ytdownload: downloads vids from YouTube using URL")
    
    command = input("> ")

    if command == "separate":
        separate()
    elif command == "ytdownload":
        download()
    else:
        print(Fore.RED + "Unknown command!" + Fore.RESET)
    
@click.command()
@click.option("--i", prompt="Path to the input image", help="The path for the image to process.")
@click.option("--o", prompt="Path to folder for output", help="The path for the output image.")
def separate(i, o):
    separator.separate_connected_components(image_path=i, output_dir=o)

@click.command()
@click.option("--url", prompt="URL for the video you want to download", help="The URL for the video to be downloaded.")
def download(url):
    downloader.download_youtube_video(url=url)

if __name__=="__main__":
    start()
