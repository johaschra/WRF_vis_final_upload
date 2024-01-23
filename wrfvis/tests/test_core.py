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


def test_get_wrf_for_map():

    df, is_3D = core.get_wrf_for_map('T2', 5)

    assert df.attrs['variable_name'] == 'T2'
    assert df.attrs['variable_units'] == 'K'
    assert df.attrs['variable_descr'] == 'TEMP at 2 M'
    assert is_3D == False

    df, is_3D = core.get_wrf_for_map('T', 5, 5)

    assert df.attrs['variable_name'] == 'T'
    assert df.attrs['variable_units'] == 'K'
    assert is_3D == True


def test_get_wrf_for_cross_invalid_input():

    # Test with invalid dimension parameter T2
    with pytest.raises(ValueError, match="cannot create a crosssection if height dimension missing"):
        core.get_wrf_for_cross('T2', '2018-08-18T12:00',
                               lat=None, lon=None, hgt=None)


def test_get_wrf_for_cross_invalid_input():

    # Test with invalid parameter
    with pytest.raises(ValueError, match="test_parameter not found in the WRF output file or invalid variable."):
        core.get_wrf_for_cross('test_parameter', '2018-08-18T12:00',
                               lat=None, lon=None, hgt=None)


# def test_get_wrf_for_cross_get_lat():
#     df, wrf_hgt = core.get_wrf_for_cross('test_parameter', '2018-08-18T12:00',lat='20', lon=None, hgt=None)
#     # Test with invalid parameter
#     assert vararray.attrs['lat'] == '20'
def test_get_wrf_for_map():

    df, wrf_hgt = core.get_wrf_for_map('T2', 5, '20')

    assert df.attrs['lat'] == '20'


def test_mkdir(tmpdir):

    dir = str(tmpdir.join('html_dir'))
    core.mkdir(dir)
    assert os.path.isdir(dir)
