#! /usr/bin/python

import sys

from PIL import Image


def is_target_color_present(file):
    target_color = (255, 119, 0)  # Set the target color as a hardcoded value
    img = Image.open(file)
    colors = img.getcolors(256 * 1024)  # put a higher value if there are many colors in your image
    max_occurrence, most_present = 0, 0

    try:
        sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)[:10]

        for rank, (occurrence, color) in enumerate(sorted_colors, start=1):
            print(f"Rank {rank}: Color: {color}, Occurrence: {occurrence}")

        for c in colors:
            if c[0] > max_occurrence:
                max_occurrence, most_present = c

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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evalimage.py <image_filename>")
        sys.exit(1)

    image_filename = sys.argv[1]

    if is_target_color_present(image_filename):
        print('Found color in the image - seems to be alive... Won\'t restart.')
        sys.exit(1)
