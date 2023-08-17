from cv2 import resize, imread
from math import ceil
import sys
import os
import matplotlib.pyplot as plt
import numpy as np

TERMINAL_ASCII_MAP = " .:*#"

#used to minimise distortion with most non mono-spaced fonts
MESSAGES_ASCII_MAP = " `~<Q"


class image_to_ascii:

    def __init__(self):
        #default values
        self._image_character_length = 80 #arbitrary
        self._scale_height = 1
        self._grey_scale_ascii_map = TERMINAL_ASCII_MAP
        self._start_char = ""

    def scale_height(self, scale: float):
        """
        Takes float between 0 and 1 and scales the height of the output in
        characters by that amount. Useful as character height may distort
        the height of the image so may take some tinkering. If falsy variable
        is passed, defaults to 1.
        """

        if scale < 0 or scale > 1:
            raise ValueError("scale must between 1 and 0")
        elif type(scale) != float or not bool(scale):
            scale = 1 #default to 1

        self._scale_height = scale

    def row_beginner(self, beginner: str):
        """
        designates a string that will go at the start of each line, default
        value is nothing. Pass falsy variable to reset to default
        """

        if not beginner:
            self._start_char = ""

        self._start_char = beginner

    def image_width(self, width:int):
        """
        takes an integer length and will set the width of the output to that
        width in characters
        """
        self._image_character_length = width

    def ascii_map(self, char_set:str):
        """
        takes a string argument that sets the map of the greyscale to ascii
        to that string of characters. Character set should be in order of
        lightest (least space eg: . ) to darkest (most space eg: @)
        """
        if not isinstance(char_set, str):
            raise TypeError("grey scale ascii mapping needs to be a string, not "+ str(type(char_set)))

        if len(char_set) < 3:
            print("WARNING: it is reccomended to use a ascii mapping of atleast 3 characters")

        self._grey_scale_ascii_map = char_set


    def image_to_ascii(self, image_path:str, invert: bool = False,
        text_file_path: str|None = None)->str:
        """
        takes image_path, invert, text_file_path and returns the string
        containing an ascii version of the image. If text_file_path is
        provided, writes this string to the file also
        """
        ascii_mapping = self._grey_scale_ascii_map
        if invert:
            ascii_mapping = ascii_mapping[::-1] #inverts colors

        #get image from file path
        img = imread(image_path, 0)
        if type(img) == type(None):
            return

        im_width, im_height = img.shape
        im_width -= len(self._start_char)

        height_width_ratio = im_height/im_width
        height_width_ratio *= self._scale_height


        img = resize( #resize img
            img,
            [
                self._image_character_length,
                int(height_width_ratio * self._image_character_length)
            ]
        )

        result = "" #initialise final string
        for row in img:
            char_row = ""

            if self._start_char:
                char_row += self._start_char

            for pix in row:
                pix_ascii = ascii_mapping[
                    ceil((pix/255)*len(ascii_mapping))-1
                ]
                char_row += pix_ascii

            char_row += "\n"
            result += char_row
        if text_file_path:
            with open(text_file_path, 'w') as f:
                f.writelines(result)

        return result


if __name__ == "__main__":
    converter = image_to_ascii()
    converter.scale_height(0.2)
    result = converter.image_to_ascii(
        "chris.jpeg", invert=True
    )

    print(result)