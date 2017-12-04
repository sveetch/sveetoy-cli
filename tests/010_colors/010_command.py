# -*- coding: utf-8 -*-
import os

from pathlib import Path

import pytest

import click
from click.testing import CliRunner

from sveetoy_cli.cli.console_script import cli_frontend


def test_empty(caplog, settings):
    """Invoked without required arguments"""
    runner = CliRunner()

    # Temporary isolated current dir
    with runner.isolated_filesystem():
        test_cwd = os.getcwd()

        # Default verbosity
        result = runner.invoke(cli_frontend, ['colors'])

        assert caplog.record_tuples == []

        assert 'Error: Missing argument "source".' in result.output

        assert result.exit_code == 2


def test_doesnotexists(caplog, settings):
    """Invoked without required arguments"""
    runner = CliRunner()

    # Temporary isolated current dir
    with runner.isolated_filesystem():
        test_cwd = os.getcwd()

        # Default verbosity
        result = runner.invoke(cli_frontend, ['colors'] + ['foo.txt'])

        assert caplog.record_tuples == []

        assert 'Invalid value for "source": Path "foo.txt" does not exist.' in result.output
        assert result.exit_code == 2


def test_source_as_file(caplog, settings):
    """Invoked with a file path as source argument"""
    runner = CliRunner()

    source_path = 'foo.txt'

    # Temporary isolated current dir
    with runner.isolated_filesystem():
        test_cwd = os.getcwd()

        source_file = Path(test_cwd) / source_path
        source_file.write_text('Dummy')

        # Default verbosity
        result = runner.invoke(cli_frontend, ['colors'] + [source_path])

        assert result.exit_code == 0

        assert caplog.record_tuples == [
            (
                'sveetoy',
                20,
                "Searching files for colors"
            ),
        ]


def test_source_as_directory(caplog, settings):
    """Invoked with a directory path as source argument"""
    runner = CliRunner()

    source_path = 'bar'

    # Temporary isolated current dir
    with runner.isolated_filesystem():
        test_cwd = os.getcwd()

        source_dir = Path(test_cwd) / source_path
        source_dir.mkdir(parents=True)

        # Default verbosity
        result = runner.invoke(cli_frontend, ['colors'] + [source_path])

        assert result.exit_code == 0

        assert caplog.record_tuples == [
            (
                'sveetoy',
                20,
                "Searching files for colors"
            ),
        ]
