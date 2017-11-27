# -*- coding: utf-8 -*-
import os

import pytest

from sveetoy_cli.colors.naming import ColorNames

@pytest.mark.parametrize("color,attempted", [
    (
        "#000000",
        'black'
    ),
    #(
        #"#ff0000",
        #'red'
    #),
])
def test_name_it(color, attempted):
    namer = ColorNames()

    assert namer.name_it(color) == attempted
