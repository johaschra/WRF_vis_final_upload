import os
import numpy as np

from wrfvis import core, cfg
import pytest


def test_get_ts():

    df, hgt = core.get_wrf_timeseries('T', 11, 45, 300)

    assert df.attrs['variable_name'] == 'T'
    assert df.attrs['variable_units'] == 'K'
    assert df.attrs['grid_point_elevation_time0'] < 400
    assert df.attrs['grid_point_elevation_time0'] > 10
    np.testing.assert_allclose(df.XLAT, df.attrs['lat_grid_point'])
    np.testing.assert_allclose(df.XLONG, df.attrs['lon_grid_point'])

    # dimensions of hgt
    assert hgt.dims == ('south_north', 'west_east')


def test_get_time_index():
    '''Tests the get_time_index
    Author: Johanna Schramm'''
    assert core.get_time_index('2018-08-18T12:00') == 0
    assert core.get_time_index('2018-08-18T13:00') == 1
    assert core.get_time_index('2018-08-19T23:00') == 35

    with pytest.raises(ValueError):
        core.get_time_index('2018-08-19T24:00')

    with pytest.raises(ValueError):
        core.get_time_index('2017-08-19T24:00')


def test_get_wrf_for_map():
    '''Author: Johanna Schramm'''

    df, is_3D = core.get_wrf_for_map('T2', 5)

    assert df.attrs['variable_name'] == 'T2'
    assert df.attrs['variable_units'] == 'K'
    assert df.attrs['variable_descr'] == 'TEMP at 2 M'
    assert is_3D == False

    df, is_3D = core.get_wrf_for_map('T', 5, 5)

    assert df.attrs['variable_name'] == 'T'
    assert df.attrs['variable_units'] == 'K'
    assert is_3D == True


def test_write_html_map(tmpdir, capsys):
    '''Author:Johanna Schramm'''
    outpath = core.write_html_map('T2', 2, None)
    assert os.path.exists(outpath)
    captured = capsys.readouterr()
    assert 'Extracting values at specified time' in captured.out


def test_mkdir(tmpdir):

    dir = str(tmpdir.join('html_dir'))
    core.mkdir(dir)
    assert os.path.isdir(dir)
