# Testing command line interfaces is hard. But we'll try
# At least we separated our actual program from the I/O part so that we
# can test that
import wrfvis
from wrfvis.cltools import gridcell, MAP, CROSS, check_wind

import pytest


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


def test_help_MAP(capsys):
    ''' test the help Part from the comandline tool MAP
    Author: Johanna Schramm
    '''

    # Check that with empty arguments we return the help
    MAP([])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out
    print(captured.out)

    MAP(['-h'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out

    MAP(['--help'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out


# test go to directory wrfvis_test and then type pytest
def test_help_CROSS(capsys):
    ''' test the help Part from the comandline tool CROSS
    Author: Lena Zelger
    '''

    # Check that with empty arguments we return the help
    CROSS([])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out
    print(captured.out)

    CROSS(['-h'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out

    CROSS(['--help'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out


def test_version(capsys):

    gridcell(['-v'])
    captured = capsys.readouterr()
    assert wrfvis.__version__ in captured.out


def test_check_wind(capsys):

    # Test with valid input, no exception should be raised
    assert check_wind('T', 'crosssection') is None
    assert check_wind('T', 'map') is None


def test_check_wind_invalid_input_u():
    # Test with invalid 'u' input, expect ValueError
    with pytest.raises(ValueError, match="It is not possible to make a blabla_plot plot for Wind components"):
        check_wind('u', 'blabla_plot')


def test_print_html(capsys):

    gridcell(['-p', 'T', '-l', '12.1', '47.3', '300', '--no-browser'])
    captured = capsys.readouterr()
    assert 'File successfully generated at:' in captured.out

    MAP(['-p', 'T2', '-t', '2', '--no-browser'])
    captured = capsys.readouterr()
    assert 'File successfully generated at:' in captured.out


def test_time_in_range(capsys):

    MAP(['-p', 'T2', '-t', '0', '--no-browser'])
    captured = capsys.readouterr()
    assert 'File successfully generated at:' in captured.out

    with pytest.raises(ValueError):
        MAP(['-p', 'T2', '-t', '36', '--no-browser'])

    with pytest.raises(ValueError):
        MAP(['-p', 'T2', '-t', '-1', '--no-browser'])


def test_error(capsys):

    gridcell(['-p', '12.1'])
    captured = capsys.readouterr()
    assert 'command not understood' in captured.out

    MAP(['xyz'])
    captured = capsys.readouterr()
    assert 'wrfvis_map: command not understood. ' in captured.out
