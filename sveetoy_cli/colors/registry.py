# -*- coding: utf-8 -*-
import io, json

from pathlib import Path

class ColorRegistry:
    """
    Open, read and store color names maps
    """
    def __init__(self):
        datas_dirpath = Path(__file__).parent / "datas"

        self.map_paths = [
            datas_dirpath / "color-hex.json",
            datas_dirpath / "imagemagick.json",
            datas_dirpath / "w3schools.json"
        ]

        self.name_maps = {}
        for item in self.map_paths:
            with io.open(str(item), 'r') as fp:
                self.name_maps[item.stem] = dict(json.load(fp))