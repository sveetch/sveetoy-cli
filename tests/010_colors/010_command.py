# -*- coding: utf-8 -*-
import os

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
        result = runner.invoke(cli_frontend, ['colors']+[])

        assert caplog.record_tuples == [
            (
                'sveetoy',
                50,
                'At least one argument is required for a Sass source file'
            ),
        ]

        assert result.exit_code == 1


def test_doesnotexists(caplog, settings):
    """Invoked without required arguments"""
    runner = CliRunner()

    # Temporary isolated current dir
    with runner.isolated_filesystem():
        test_cwd = os.getcwd()

        # Default verbosity
        result = runner.invoke(cli_frontend, ['colors']+['foo.txt'])

        assert caplog.record_tuples == []

        assert 'Invalid value for "sources": Path "foo.txt" does not exist.' in result.output
        assert result.exit_code == 2


def test_single(caplog, settings):
    """Invoked without required arguments"""
    runner = CliRunner()

    # Temporary isolated current dir
    with runner.isolated_filesystem():
        test_cwd = os.getcwd()

        # Default verbosity
        result = runner.invoke(cli_frontend, ['colors']+['foo.txt'])

        assert result.exit_code == 0

        assert caplog.record_tuples == []
