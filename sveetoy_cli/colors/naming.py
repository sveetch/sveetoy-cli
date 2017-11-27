# -*- coding: utf-8 -*-
"""
* When a color name is used more than one time, increment names with "_[+1]" for all other identic names;
"""
import json, os, re

from pathlib import Path

from colour import Color

from sveetoy_cli.colors.registry import ColorRegistry

class ColorNames(ColorRegistry):
    def name_it(self, hexa):
        """
        Return a color name for given hexadecimal code
        """
        clr = Color(hexa)
        return "nope"
