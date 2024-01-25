# A visualization package for WRF model output

**wrfvis** offers command line tools to display WRF model output in your browser.

It was written for the University of Innsbruck's
[scientific programming](https://manuelalehner.github.io/scientific_programming)
course as a package template for the semester project and is based on the 
example packages [scispack](https://github.com/fmaussion/scispack) and
[climvis](https://github.com/fmaussion/climvis) written by
[Fabien Maussion](https://fabienmaussion.info).

## HowTo

Make sure you have all dependencies installed. These are:
- numpy
- pandas
- xarray
- netcdf4
- matplotlib
- pytest
- cartopy

Download the package and install it in development mode. From the root directory,
do:

    $ pip install -e .

If you are on a university computer, you should use:

    $ pip install --user -e .

## Command line interface

``setup.py`` defines an "entry point" for a script to be used as a
command line program. Currently, the only command installed is ``wrfvis_gridcell``.

After installation, just type

    $ wrfvis_gridcell --help
or
    $ wrfvis_map -h
or
    $ wrfvis_cross -h

to see what the tool can do.
## Usage

You have 2 option to run the code, depending on the variable that you select. A list of output variable is [here](https://www2.mmm.ucar.edu/wrf/users/wrf_users_guide/build/html/output_variables.html)
 
For 3d variable (T: "perturbation potential temperature theta-t0") type:

    $ wrfvis_gridcell -p T -l 11 45 200
    

For 2d variable (MU: "perturbation dry air mass in column") type

    $ wrfvis_gridcell -p MU -l 11 45

## Added functionalities

1. Display spacial distributions of a parameter on a map (wrvis_map)
   
Author: **Johanna Schramm**

Command line input:

    $ wrfvis_map -h for help

    
Example usage:

    $ wrfvis_map -p T2 -t 5 (Displays Temp at 2 M on 18 Aug 2028 at 17 UTC)
    $ wrfvis_map -p T -t 5 -hgt 5 (Displays Temp at Level 5 on 18 Aug 2028 at 17 UTC)



2. Plot of a crosssection either over all latitudes by a choosing a longitude value in degrees or over all longitudes choosing a latitude.
Its is optional to select a certain height for the crosssection

Author: **Lena Zelger**

Command line input: 

    $ wrfvis_cross -h for help


Example usage:

    $ wrfvis_cross -p T -t 5 -hgt 10000 -lon 10 


(Displays perturbation Temperature on 18 Aug 2028 
at 17 UTC over all latitudinal cells at a 
longitude of 10 degrees at a height of 10000 meter converted and displayed as a gridcell number)

    $ wrfvis_cross -p T -t 5 -hgt 10000 -lat 10 (option over longitude)
    $ wrfvis_cross -p T -t 5  -lon 10 (option without selecting height, gives the crosssection over all height cells)



3.Create an html file to plot a single Skew T-logP plot with wind profile, hodographs and Skew T-logP indices.

Author: **Christian Brida**

Command line input: 

    $ wrfvis_skewt -h for help


To plot a single diagram, with wind profile, hodograph and indices, you can run: 

    $ wrfvis_skewt -l 11 45 -t 2018-08-18T12:00 for single diagram, wind profile, hodograph and parameters
    $ wrfvis_skewt -l 11 45 -t 2018-08-18T12:00 12 for compare 2 different timestamps and the average Skew T-logP
    

########## new versions for the command-line tools in file "Max" ###########
1. "cftools.py": Modifications of the command-line tools
2. "cftools2.py": Dealing with error handling and the structure of command-line processing. 
3. "test_cltools.py": Adding to tests  1) test of extraction of coordinates and height
         			       2) test for handling invalid comments


##### Gianni #########
Variable explorer




## Testing

I recommend to use [pytest](https://docs.pytest.org) for testing. To test
the package, run

    $ pytest .

in the package root directory.


## License

With the exception of the ``setup.py`` file, which was adapted from the
[sampleproject](https://github.com/pypa/sampleproject) package, all the
code in this repository is dedicated to the public domain.




    
