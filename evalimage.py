#! /usr/bin/python

import sys

from PIL import Image


def is_target_color_present(file):
    target_color = (221, 68, 68)  # Set the target color as a hardcoded value
    img = Image.open(file)
    colors = img.getcolors(256 * 1024)  # put a higher value if there are many colors in your image

    try:
        # sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)[:10]

        # for rank, (occurrence, color) in enumerate(sorted_colors, start=1):
        #    print(f"Rank {rank}: Color: {color}, Occurrence: {occurrence}")

        if target_color in [color for occurrence, color in colors]:
            # print(f"The target color {target_color} is present in the image.")
            return True
        else:
            # print(f"The target color {target_color} is not present in the image.")
            return False

    except TypeError:
        # Too many colors in the image
        print("Too many colors in the image.")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        # print("Usage: python evalimage.py <image_filename>")
        sys.exit(1)

    image_filename = sys.argv[1]

    if not is_target_color_present(image_filename):
        print('Target color not found in the image - restarting.')
        sys.exit(1)
    else:
        print('Found target color in the image - seems to be alive... Won\'t restart.')
