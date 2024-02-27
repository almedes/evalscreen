#! /usr/bin/python

import sys

from PIL import Image


def is_target_color_present(file):
    target_color = (255, 119, 0)  # Set the target color as a hardcoded value
    img = Image.open(file)
    colors = img.getcolors(256 * 1024)  # put a higher value if there are many colors in your image
    max_occurrence, most_present = 0, 0

    try:
        for c in colors:
            if c[0] > max_occurrence:
                max_occurrence, most_present = c
            occurrence, color = c
            print(f"Color: {color}, Occurrence: {occurrence}")

        # Check if the target color is present
        if most_present == target_color:
            print(f"The target color {target_color} is present in the image.")
            return True
        else:
            print(f"The target color {target_color} is not present in the image.")
            return False

    except TypeError:
        # Too many colors in the image
        print("Too many colors in the image.")
        return False


if is_target_color_present('screen.png'):
    print('Found color in image - seems to be alive ... Wont restart')
    sys.exit(1)
