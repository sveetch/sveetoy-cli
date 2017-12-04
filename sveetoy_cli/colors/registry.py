# -*- coding: utf-8 -*-
import io, json

from pathlib import Path

from collections import OrderedDict


class ColorRegistry:
    """
    Open, read and store color names maps
    """
    def __init__(self):
        datas_dirpath = Path(__file__).parent / "datas"

        self.map_path = datas_dirpath / "names.json"

        with io.open(str(self.map_path), 'r') as fp:
            names = dict(json.load(fp))

        self.name_map = names
        # Reverse keys/values so map is indexed on hexa
        self.hexa_map = dict(zip(self.name_map.values(), self.name_map.keys()))
