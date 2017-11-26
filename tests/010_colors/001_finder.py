# -*- coding: utf-8 -*-
import os

import pytest

from sveetoy_cli.colors.finder import ColorFinder

from pathlib import Path


@pytest.mark.parametrize("extensions,attempted", [
    (
        None,
        [
            'sample-3.scss',
            'sample-2.scss',
            'sample-1.scss',
            'sub_1/subfile.scss',
            'sample-4.sass',
            'sample-5.css',
            'sub_1/sub_1-1/subsubfile.css',
        ]
    ),
    (
        ['scss'],
        [
            'sample-3.scss',
            'sample-2.scss',
            'sample-1.scss',
            'sub_1/subfile.scss',
        ]
    ),
    (
        ['sass'],
        [
            'sample-4.sass',
        ]
    ),
    (
        ['css'],
        [
            'sample-5.css',
            'sub_1/sub_1-1/subsubfile.css',
        ]
    ),
    (
        ['txt'],
        [
            'dummy.txt',
        ]
    ),
    (
        ['nope'],
        []
    ),
])
def test_get_files(settings, extensions, attempted):
    """Search for colors in file"""
    basedir = settings.colors_path

    finder = ColorFinder(extensions=extensions)
    found = finder.get_files(basedir)

    relative_found = [str(item.relative_to(basedir)) for item in found]

    assert sorted(relative_found) == sorted(attempted)


@pytest.mark.parametrize("source,attempts", [
    (
        "nothing",
        []
    ),
    (
        ("// Not a color\n"
         "#maze"),
        []
    ),
    (
        ("// Invalid hexa\n"
         "color: ffffff;"),
        []
    ),
    (
        "#000",
        ["#000"]
    ),
    (
        "#FFF000",
        ["#fff000"]
    ),
    (
        "#fff000",
        ["#fff000"]
    ),
    (
        ("// Single comment\n"
         ".red{color: #ff0000}"),
        ["#ff0000"]
    ),
    (
        ("// Commented color\n"
         "// #ff0000"),
        ["#ff0000"]
    ),
    (
        ("color: rgba(#ff0000, 0.4);"),
        ["#ff0000"]
    ),
    (
        ("// Single comment\n"
         ".red{color: #ff0000}\n"
         ".blue{color: #0000ff;}"),
        ["#ff0000", "#0000ff"]
    ),
    (
        ("$var: #f0f0f0 #dedede #ff0000;"),
        ["#f0f0f0", "#dedede", "#ff0000"]
    ),
])
def test_find_hexacode(source, attempts):
    """Hexadecimal codes finding"""
    finder = ColorFinder()
    found = finder.find_hexacode(source)

    assert sorted(found) == sorted(attempts)


# rgb[a] is currently not supported
#@pytest.mark.parametrize("source,attempts", [
    #(
        #"nothing",
        #[]
    #),
    #(
        #("color: rgba(255, 0, 0);"),
        #["255, 0, 0"]
    #),
    #(
        #("color: rgba(#255, 0, 0);"),
        #["#255, 0, 0"]
    #),
    #(
        #("color: rgba(#255, 0);"),
        #["#255"]
    #),
    #(
        #("color: rgba(#ff0000, 0.4);"),
        #["#ff0000"]
    #),
    #(
        #("color: rgb(255, 0, 0);"
         #"color: rgb(0, 255, 0);"),
        #["0, 255, 0", "255, 0, 0"]
    #),
#])
#def test_find_rgb(source, attempts):
    #"""rgb[a] finding"""
    #finder = ColorFinder()
    #found = finder.find_rgb(source)

    #assert sorted(found) == sorted(attempts)


@pytest.mark.parametrize("filepath,attempts", [
    (
        "sample-1.scss",
        ['#4c4c92', '#6676a2', '#ff8702']
    ),
    (
        "sample-2.scss",
        []
    ),
    (
        "sample-3.scss",
        ['#253a79', '#1a2955', '#fafafa', '#ff8702']
    ),
    (
        "sample-4.sass",
        ['#00ff00']
    ),
    (
        "sample-5.css",
        ['#222']
    ),
])
def test_read_file(settings, filepath, attempts):
    """Open and read file"""
    basedir = settings.colors_path

    path = basedir / Path(filepath)

    finder = ColorFinder()
    found = finder.read_file(path)

    assert sorted(found) == sorted(attempts)


@pytest.mark.parametrize("dirpath,extensions,attempts", [
    (
        ".",
        None,
        ['#222', '#b29e6b', '#253a79', '#fafafa', '#1a2955', '#6676a2',
         '#00ff00', '#8461a1', '#ff8702', '#4c4c92']
    ),
    (
        "empty",
        None,
        []
    ),
    (
        "sub_1",
        None,
        ['#b29e6b', '#8461a1']
    ),
    (
        ".",
        ['css', 'sass'],
        ['#222', '#8461a1', '#00ff00']
    ),
])
def test_search(settings, dirpath, extensions, attempts):
    """Hexadecimal codes finding"""
    basedir = settings.colors_path

    path = basedir / Path(dirpath)

    finder = ColorFinder(extensions=extensions)
    found = finder.search(path)

    print(found)
    assert sorted(found) == sorted(attempts)
