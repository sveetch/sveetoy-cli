# -*- coding: utf-8 -*-
import logging

from pathlib import Path

import click

from sveetoy_cli.colors.finder import ColorFinder
from sveetoy_cli.colors.naming import ColorNames


@click.command('colors', short_help='Search for colors to name them.')
@click.argument('source', type=click.Path(exists=True), required=True)
@click.pass_context
def colors_command(context, source):
    """
    Search for colors in given files and return named colors.
    """
    logger = logging.getLogger("sveetoy")

    logger.info("Searching files for colors")

    finder = ColorFinder()
    colors = finder.search(Path(source))

    namer = ColorNames()
    namer.batch_names(colors)
