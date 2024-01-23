# Testing command line interfaces is hard. But we'll try
# At least we separated our actual program from the I/O part so that we
# can test that
import wrfvis
from wrfvis.cltools import gridcell


def test_help(capsys):

    # Check that with empty arguments we return the help
    gridcell([])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out
    print(captured.out)

    gridcell(['-h'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out

    gridcell(['--help'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out


def test_version(capsys):

    gridcell(['-v'])
    captured = capsys.readouterr()
    assert wrfvis.__version__ in captured.out


def test_print_html(capsys):
    # adapted to our input versionp
    gridcell(['-p', 'T', '-lon', '12.1', '-lat', '47.3', '-hgt', '300', '--no-browser'])
    captured = capsys.readouterr()
    assert 'File successfully generated at:' in captured.out


def test_error(capsys):

    gridcell(['-p', '12.1'])
    captured = capsys.readouterr()
    assert 'command not understood' in captured.out


"""
Author: Maximilian Bähr
Date: January 2024

Subtask 1: Test of extraction of coordinates and height
"""
# This test checks whether the gridcell function extracts
# coordinates and height as it should.
# Provide a valid parameter, location, and height
# as example coordinates and height asl of Innsbruck
def test_coordinate_and_height_extraction(capsys):
    gridcell(['-p', 'T', '-lon', '11.4', '-lat', '47.3', '-hgt', '574'])

    # Capture the output
    captured = capsys.readouterr()
    # Add assertions based on the expected output
    assert 'Extracting timeseries at nearest grid cell' in captured.out
    assert 'Plotting data' in captured.out


"""
Subtask 2: Test for handling invalid comments
"""
# This test simulates running the script with an invalid command ('invalid_command')
# and checks if the correct error message is printed.
def test_invalid_command(capsys):
    args = ['invalid_command']

    # Call the gridcell function and capture printed output
    gridcell(args)

    # Check if the correct error message is printed
    captured = capsys.readouterr()
    assert 'wrfvis_gridcell: command not understood.' in captured.out
    assert 'Type "wrfvis_gridcell --help" for usage information.' in captured.out

