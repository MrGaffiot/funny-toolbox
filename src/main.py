import click
import scriptFiles.imageSeparator as separator
import os

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

def start():
    size = os.get_terminal_size().columns
    for line in ascii_art_lines:
        print(line.center(size, " "))

@click.command()
@click.option("--i", prompt="Path to the input image: ", help="The path for the image to process.")
@click.option("--o", prompt="Path to folder for output: ", help="The path for the output image.")
def separate(i, o):
    separator.separate_connected_components(image_path=i, output_dir=o)

if __name__=="__main__":
    start()

