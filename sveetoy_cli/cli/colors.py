# -*- coding: utf-8 -*-
import click
import logging


@click.command('colors', short_help='Search for colors to name them.')
@click.argument('sources', type=click.Path(exists=True), nargs=-1)
@click.pass_context
def colors_command(context, sources):
    """
    Search for colors in given files and return named colors.
    """
    logger = logging.getLogger("sveetoy")

    if not sources:
        logger.critical("At least one argument is required for a Sass source file")
        raise click.Abort()
    print(sources)

    logger.info("Searching files for colors")