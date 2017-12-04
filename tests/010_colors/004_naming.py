# -*- coding: utf-8 -*-
import os

import pytest

from sveetoy_cli.colors.naming import ColorNames


@pytest.mark.parametrize("color,attempted", [
    (
        "#000000",
        ("black", "#000000"),
    ),
    (
        "#ff0000",
        ("red1", "#ff0000"),
    ),
    (
        "#8461a1",
        ("plum4", "#8b668b"),
    ),
    (
        "#602f8a",
        ("darkorchid4", "#68228b"),
    ),
    (
        "#b29e6b",
        ("darkkhaki", "#bdb76b"),
    ),
    (
        "#505050",
        ("gray31", "#4f4f4f"),
    ),
    (
        "#40b59b",
        ("mediumseagreen", "#3cb371"),
    ),
    (
        "#00688b",
        ("deepskyblue4", "#00688b"),
    ),
    (
        "#f7f5f2",
        ("whitesmoke", "#f5f5f5"),
    ),
])
def test_nearest_color_name(color, attempted):
    """
    Testing nearest color name finder is accurate
    """
    namer = ColorNames()

    assert namer.nearest_color_name(color) == attempted


@pytest.mark.parametrize("colors,attempted", [
    (
        ["#000000", "#ff0000"],
        {
            "#000000": ("black", "#000000"),
            "#ff0000": ("red1", "#ff0000"),
        }
    ),
    (
        ["#8461a1", "#602f8a", "#505050"],
        {
            "#8461a1": ("plum4", "#8b668b"),
            "#602f8a": ("darkorchid4", "#68228b"),
            "#505050": ("gray31", "#4f4f4f"),
        }
    ),
])
def test_batch_names(colors, attempted):
    """
    Testing nearest color name finder is accurate
    """
    namer = ColorNames()

    assert namer.batch_names(colors) == attempted
