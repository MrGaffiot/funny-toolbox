from PIL import Image, ImageDraw, ImageFont

def add_black_border_with_text(image_path, text):
    # Open an image file
    with Image.open(image_path) as img:
        # Calculate the size for the new image with a black border
        border_size = 50  # You can change this value to make the border larger or smaller
        new_width = img.width + 2 * border_size
        new_height = img.height + 2 * border_size
        
        # Create a new image with black background
        new_img = Image.new("RGB", (new_width, new_height), "black")
        
        # Paste the original image onto the new image, centered
        new_img.paste(img, (border_size, border_size))
        
        # Create a drawing context
        draw = ImageDraw.Draw(new_img)
        
        font = ImageFont.load_default()
        
        # Get the size of the text to be drawn
        text_width, text_height = draw.textsize(text, font=font)
        
        # Calculate the position at the bottom center
        text_x = (new_img.width - text_width) // 2
        text_y = new_img.height - border_size - text_height
        
        # Draw the text
        draw.text((text_x, text_y), text, fill="white", font=font)
        
        # Draw white lines at the edges of the black border
        line_width = 2  # You can change the thickness of the lines
        draw.line([(0, 0), (new_width - 1, 0)], fill="white", width=line_width)  # Top line
        draw.line([(0, 0), (0, new_height - 1)], fill="white", width=line_width)  # Left line
        draw.line([(0, new_height - 1), (new_width - 1, new_height - 1)], fill="white", width=line_width)  # Bottom line
        draw.line([(new_width - 1, 0), (new_width - 1, new_height - 1)], fill="white", width=line_width)  # Right line
        
        # Save the resulting image
        new_img.save("output.png")
