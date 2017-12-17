# -*- coding: utf-8 -*-
"""
* When a color name is used more than one time, increment names with "_[+1]" for all other identic names;
"""
import json, os, re

from pathlib import Path

from colour import Color

from sveetoy_cli.colors import toColourRGB, toCssRGB
from sveetoy_cli.colors.registry import ColorRegistry


class ColorNames(ColorRegistry):
    def nearest_color_name(self, hexa):
        """
        Find nearest color name from color name registry.

        Nearest color is find through a difference from given color and
        available name colors.

        Difference is computed by adding up RGB values and compare it to each
        added up RGB value from available name colors. In the end of scanning
        name colors, the lesser difference win.

        Args:
            hexa (str): Long hexadecimal color code like ``#000000``, not
                short code like ``#000``.

        Returns:
            tuple: A tuple of nearest color name and its original hexadecimal
                code than can differ from given ``hexa`` argument.
        """
        min_diff = None
        searched_color = Color(hexa)
        searched_red, searched_green, searched_blue = toCssRGB(searched_color.rgb)

        for available_hexa, available_name in self.hexa_map:
            r, g, b = toCssRGB(Color(available_hexa).rgb)

            # Compute RGB values difference between colors
            diff = (abs(searched_red - r) * 256) + \
                    (abs(searched_green - g) * 256) + \
                    (abs(searched_blue- b) * 256)

            if min_diff is None or diff < min_diff:
                min_diff = diff
                color_name = available_name
                original_hex = available_hexa

        return (color_name, original_hex)

    def batch_names(self, colors):
        """
        Find nearest color names for every given hexadecimal codes.

        Args:
            colors (list): List of long hexadecimal color code.

        Returns:
            dict: A dictionnary of given colors with their nearest color name.
        """
        batchs = {}

        for code in colors:
            batchs[code] = self.nearest_color_name(code)

        return batchs
