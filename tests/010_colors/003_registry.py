# -*- coding: utf-8 -*-
import os

import pytest

from sveetoy_cli.colors.registry import ColorRegistry


def test_loading():
    """
    Testing names map has been correctly loaded
    """
    registry = ColorRegistry()

    assert ('black' in registry.name_map) == True
    assert ('white' in registry.name_map) == True
    assert ('#000000' in registry.hexa_map) == True
    assert ('#ffffff' in registry.hexa_map) == True

    assert ('foo' in registry.name_map) == False
    assert ('#foo' in registry.hexa_map) == False
