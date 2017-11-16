#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Try to find all used colors through all given scss/css files

Require:

    pip install colorutils

TODO: * Parse all existing *.scss/*.css files from given directory (instead of SCSS_FILES)
      * When a color name is used more than one time, increment names with "_[+1]" for all other identic names;
      * Procedure to replace hexadecimal, rgb, and rgba colors with their variable name (using their finded name);
"""
import json, os, re

import colorutils

SCSS_FILES = [
    'scss/app.scss',
]

class ColorNames:
    """
    Gist: https://gist.github.com/jdiscar/9144764

    Original Author  Ernesto P. Adorio, Ph.D
    Original Source: http://my-other-life-as-programmer.blogspot.com/2012/02/python-finding-nearest-matching-color.html
    Modifed By: JDiscar

    This class maps an RGB value to the nearest color name it can find. Code is modified to include
    ImageMagick names and WebColor names.

    1. Modify the minimization criterion to use least sum of squares of the differences.
    2. Provide error checking for input R, G, B values to be within the interval [0, 255].
    3. Provide different ways to specify the input RGB values, aside from the (R, G, B) values as done in the program above.
    """

    ColorHexCom = dict(json.load(open("color-hex_color-names.json", 'r')))

    WebColorMap = dict(json.load(open("w3schools_color-names.json", 'r')))

    ImageMagickColorMap = dict(json.load(open("imagemagick_color-names.json", 'r')))

    @staticmethod
    def rgbFromStr(s):
        # s starts with a #.
        r, g, b = int(s[1:3],16), int(s[3:5], 16),int(s[5:7], 16)
        return r, g, b

    @staticmethod
    def findNearestWebColorName((R,G,B)):
        return ColorNames.findNearestColorName((R,G,B),ColorNames.WebColorMap)

    @staticmethod
    def findNearestImageMagickColorName((R,G,B)):
        return ColorNames.findNearestColorName((R,G,B),ColorNames.ImageMagickColorMap)

    @staticmethod
    def findNearestColorHexComColorName((R,G,B)):
        return ColorNames.findNearestColorName((R,G,B),ColorNames.ColorHexCom)

    @staticmethod
    def findNearestColorName((R,G,B),Map):
        mindiff = None
        for d in Map:
            r, g, b = ColorNames.rgbFromStr(Map[d])
            diff = abs(R -r)*256 + abs(G-g)* 256 + abs(B- b)* 256
            if mindiff is None or diff < mindiff:
                mindiff = diff
                mincolorname = d
        return mincolorname




if __name__ == "__main__":
    # Open scss files to find colors
    collected_color = {}
    for filepath in SCSS_FILES:
        print "* Opening filepath:", filepath
        with open(filepath, 'rb') as fileobj:
            content = fileobj.read()

            hex_values = re.findall(r'#(?:[a-fA-F0-9]{1,6})\b', content)
            print "Hex codes:", hex_values
            for item in hex_values:
                clr = colorutils.Color(hex=item)
                collected_color[clr.hex] = clr
            print

            rgb_values = re.findall(r'rgb[a]{0,1}\(([^\n\r()]+)\)', content)
            print "Rgb(a) values:", rgb_values
            for item in rgb_values:
                rgb_colors = [v.strip() for v in item.split(',')]
                # Remove alpha channel if any
                if len(rgb_colors)>3:
                    rgb_colors = rgb_colors[0:3]
                rgb_colors = [int(v) for v in rgb_colors]
                clr = colorutils.Color(rgb=tuple(rgb_colors))
                collected_color[clr.hex] = clr
            print

    """
    Print out all finded colors, named from the given map, using "nearest" finding
    to find a name when the color does not exist in the map
    """
    print len(collected_color)
    #print json.dumps(collected_color, indent=4)
    for hex_name, color in collected_color.items():
        print hex_name, ":", ColorNames.findNearestColorHexComColorName(color.rgb), ColorNames.findNearestImageMagickColorName(color.rgb)
    #print
