# -*- coding: utf-8 -*-
import os

import pytest

from sveetoy_cli.colors.registry import ColorRegistry


def test_loading():
    registry = ColorRegistry()

    assert sorted(registry.name_maps.keys()) == sorted([
        "color-hex",
        "imagemagick",
        "w3schools"
    ])
