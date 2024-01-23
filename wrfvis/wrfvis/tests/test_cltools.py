# Testing command line interfaces is hard. But we'll try
# At least we separated our actual program from the I/O part so that we
# can test that
import wrfvis
from wrfvis.cltools import gridcell, MAP

import pytest


def test_help(capsys):

    # Check that with empty arguments we return the help
    gridcell([])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out

    gridcell(['-h'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out

    gridcell(['--help'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out


def test_help_MAP(capsys):
    ''' test the help Part from the comandline tool MAP
    Author: Johanna Schramm
    '''

    # Check that with empty arguments we return the help
    MAP([])
    captured = capsys.readouterr()
    assert 'Visualization of WRF output of a 2D variable on' in captured.out

    MAP(['-h'])
    captured = capsys.readouterr()
    assert 'Visualization of WRF output of a 2D variable on' in captured.out

    MAP(['--help'])
    captured = capsys.readouterr()
    assert 'Visualization of WRF output of a 2D variable on' in captured.out


def test_version(capsys):

    gridcell(['-v'])
    captured = capsys.readouterr()
    assert wrfvis.__version__ in captured.out


def test_print_html(capsys):

    gridcell(['-p', 'T', '-l', '12.1', '47.3', '300', '--no-browser'])
    captured = capsys.readouterr()
    assert 'File successfully generated at:' in captured.out

    MAP(['-p', 'T2', '-t', '2018-08-18T14:00', '--no-browser'])
    captured = capsys.readouterr()
    assert 'File successfully generated at:' in captured.out


def test_error(capsys):

    gridcell(['-p', '12.1'])
    captured = capsys.readouterr()
    assert 'command not understood' in captured.out

    MAP(['xyz'])
    captured = capsys.readouterr()
    assert 'wrfvis_map: command not understood. ' in captured.out
