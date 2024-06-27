import cv2
import numpy as np
import os
from colorama import Fore, Style

def separate_connected_components(image_path, output_dir=None):
    try:
        if output_dir is None:
            output_dir = "/"
        elif not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Read the input image
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if image is None:
            raise ValueError(Fore.RED + f"Image at path {image_path} could not be read." + Style.RESET_ALL)

        # Check if the image has an alpha channel
        if image.shape[2] == 4:
            b, g, r, a = cv2.split(image)
            image_rgb = cv2.merge((b, g, r))
            gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Threshold the image to get a binary image
        _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

        # Find connected components
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)

        print(f"Number of connected components: {num_labels - 1}")  # subtract 1 to not count the background

        # Iterate through each component and save it as a separate image
        for i in range(1, num_labels):  # Start from 1 to skip the background
            component_mask = (labels == i).astype(np.uint8) * 255
            component_image = cv2.bitwise_and(image, image, mask=component_mask)

            # Bounding box of the component
            x, y, w, h = stats[i, cv2.CC_STAT_LEFT], stats[i, cv2.CC_STAT_TOP], stats[i, cv2.CC_STAT_WIDTH], stats[i, cv2.CC_STAT_HEIGHT]
            component_image_cropped = component_image[y:y+h, x:x+w]

            # Create an RGBA image with a transparent background
            if component_image_cropped.shape[2] == 4:
                b, g, r, a = cv2.split(component_image_cropped)
            else:
                b, g, r = cv2.split(component_image_cropped)
                a = np.where(component_mask[y:y+h, x:x+w] > 0, 255, 0).astype(np.uint8)
            
            component_image_rgba = cv2.merge((b, g, r, a))

            # Save the component image
            component_output_path = os.path.join(output_dir, f"component_{i}.png")
            cv2.imwrite(component_output_path, component_image_rgba)
            print(f"Saved component {i} to {component_output_path}")
    except Exception as e:
        print(Fore.RED + "Something very weird and unexpected happened, go report this error to the repo of this project (https://github.com/MrGaffiot/funny-toolbox)")
        print(e + Style.RESET_ALL)
