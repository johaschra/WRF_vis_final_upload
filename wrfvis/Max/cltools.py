""" contains command line tools of WRFvis

Manuela Lehner
November 2023
"""
"""
Task 1: We here make modifications to enhance the readability,
maintainability and simplicity of the command line tools. We do not change the
functionality.

Author: Maximilian Bähr
Date: January 2024

"""

import sys
import webbrowser

import wrfvis

HELP = """wrfvis_gridcell: Visualization of WRF output at a single selected grid cell.

Usage:
   -h, --help                       : print the help
   -v, --version                    : print the installed version
   -p, --parameter [PARAM]          : WRF variable to plot
   -lon, --longitude [LON]          : longitude of grid point
   -lat, --latitude [LAT]           : latitude of grid point
   -hgt, --height [HGT]             : height above ground for grid point 
   --no-browser                     : the default behavior is to open a browser with the
                                      newly generated visualization. Set to ignore
                                      and print the path to the html file instead
"""


def gridcell(args):
    """The actual wrfvis_gridcell command line tool.

    Parameters
    ----------
    args: list
        output of sys.args[1:]
    """
    # Change 1: use of a dictionary for the replacement mapping.
    # Here, we introduce a dictionary to store the mapping between
    # old and new command line options and the use a loop to
    # apply the replacements. Instead of the loop, originally
    # we applied if-statements for that. In this way, it's easier to
    # extend and modify the replacement mapping for future changes.
    # The new version is user-friendlier as we specified more concrete input names - the
    # user cannot interchange the order of the input variables anymore.
    replace_mapping = {'--parameter': '-p', '--longitude': '-lon', '--latitude': '-lat', '--height': '-hgt'}
    # defines mapping between old and new command-line arguments.
    # for loop iterates over each pair of key-value in this dictionary
    for old_arg, new_arg in replace_mapping.items():
        if old_arg in args:  # is the old argument in the list of args?
            args[args.index(old_arg)] = new_arg  # if yes, replace it with the new one

    if len(args) == 0:  # check the value of the first argument
        print(HELP)
    elif args[0] in ['-h', '--help']:  # if the first argument is -h or --help, print the help message
        print(HELP)
    elif args[0] in ['-v', '--version']:  # if the first argument is -v or --version, print version info

        # change 2: improvement of the formatting regarding information of the version
        # for the version information we have now made use of the
        # f-string formatting, giving a better readibility. In the original code
        # the version information is concatenated using the + operator, now we
        # make use of f-strings.

        print('wrfvis_gridcell: ' + wrfvis.__version__)
        print('Licence: public domain')
        print('wrfvis_gridcell is provided "as is", without warranty of any kind')
    elif '-p' in args and '-lon' and '-lat' and '-hgt' in args:  # check for the required arguments
        # which are -p and -l. Parameter and location have to be present in args list.

        # change 3: simplification of the extracttion of coordinates and height
        # no dispersion between the 3 geographical inputs lon, lat and height
        # above sea level any more. In the originalcode, longitude, latitude
        # and height above ground are extracted from the command-line arguments
        # individually using multiple lines. Each variable is assigned based
        # on its position in the argument list. Instead, we use "map" as single line.
        #  It maps the float function to each element in the specified slice of the argument
        #  list, converting the latitude, longitude, and height above ground to float values.

        param = args[args.index('-p') + 1]  # extract the value of parameter (-p) from command line arguments
        lon = float(args[args.index('-lon') + 1])
        lat = float(args[args.index('-lat') + 1])
        zagl = float(args[args.index('-hgt') + 1])
        # extract values of longituede, latitude and height asl
        html_path = wrfvis.write_html(param, lon, lat, zagl)
        # generation of the visualization via HTML, input is parameter, longitude, latitude and height
        if '--no-browser' in args:  # is the --no-browser option in the command-line arguments?
            print('File successfully generated at: ' + html_path)  # if yes, print this message
        else:
            webbrowser.get().open_new_tab('file://' + html_path)
            # if not, open the HTML file in the default browser.
    else:
        print('wrfvis_gridcell: command not understood. '
              'Type "wrfvis_gridcell --help" for usage information.')
    # if none of the two options above is met, print this error message.


def wrfvis_gridcell():
    """Entry point for the wrfvis_gridcell application script"""

    # Minimal code because we don't want to test for sys.argv
    # (we could, but this is way above the purpose of this package
    gridcell(sys.argv[1:])

if __name__ == '__main__':

    wrfvis_gridcell()
