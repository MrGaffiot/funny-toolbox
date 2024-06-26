import click, os
from . import imageSeparator as separator
from . import ytdownloader as downloader
from . import renamer 
from . import vidmaker
from . import fsender
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
    cprint("separate: separates parts of images that are not connected into multimple images", size=size)
    cprint("ytdownload: downloads vids from YouTube using URL",size=size)
    cprint("rename: renames all files in a folder",size=size)
    cprint("makevid: merges an audio file with image to make video",size=size)
    cprint("fsender: puts up a small website to either download or upload files, check out official repo for more info", size=size)
    
    command = input("> ")

    if command == "separate":
        separate()
    elif command == "ytdownload":
        download()
    elif command == "rename":
        rename()
    elif command == "makevid":
        makevid()
    elif command == "fsender":
        sender()
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

@click.command()
@click.option("--p", prompt="Path to the folder with the files to rename", help="Path to the folder with the files to rename.")
def rename(p):
    renamer.rename_files_in_directory(p)

@click.command()
@click.option("--ipath", prompt="Path to the image you want to use", help="Path to the used image.")
@click.option("--apath", prompt="Path to the audio file you want to use", help="Path to the audio file that'll be used")
def makevid(ipath, apath):
    vidmaker.merge_image_and_audio(image_path=ipath, audio_path=apath)

@click.command()
@click.option("--m", prompt="Do you want to send or recive files (s/r)", help="Mode, recive or send")
@click.option("--p", prompt="Path to the file (enter some random letters if reciving)", help="Path to the file to be sent", required=False)
@click.option("--port", prompt="The port you want to use", help="The port being used to display the website.")
def sender(m, p, port):
    if m.lower() == "r":
        fsender.runReciver(portNum=port)
        cprint(Fore.YELLOW + "ATTENTION! This bit is a bit complicated, but it's whatever your IP/URL is and /upload")
    elif m.lower() == "s":
        fsender.runUploader(filePath=p, portNum=port)
        cprint(Fore.YELLOW + "ATTENTION! This bit is a bit complicated, but it's whatever your IP/URL is and /download")
    else:
        print(Fore.RED + "Invalid option!" + Fore.RESET)

if __name__=="__main__":
    start()
