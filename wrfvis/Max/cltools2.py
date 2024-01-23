
"""
Task 2: another version for cltools. Here, we deal with
error handling and the structure of command-line processing.
The new code is better prepared for potential errors and issues.
"""
import argparse
import sys
import webbrowser
import wrfvis

HELP = """wrfvis_gridcell: Visualization of WRF output at a single selected grid cell.

Usage:
   -h, --help                       : print the help
   -v, --version                    : print the installed version
   -p, --parameter [PARAM]          : WRF variable to plot
   -l, --location [LON] [LAT] [HGT] : location and height above ground of the grid 
                                      cell for which to plot the data
   --no-browser                     : the default behavior is to open a browser with the
                                      newly generated visualization. Set to ignore
                                      and print the path to the html file instead
"""


def gridcell(args):
    """The actual wrfvis_gridcell command line tool.

    Parameters
    ----------
    args: argparse.Namespace
        Parsed command line arguments.
    """
    if not args.parameter or not args.location:
        print("Error: Both parameter and location are required.")
        print(HELP)
        return

    try:
        param = args.parameter
        lon, lat, zagl = map(float, args.location)
        html_path = wrfvis.write_html(param, lon, lat, zagl)

        if args.no_browser:
            print('File successfully generated at: ' + html_path)
        else:
            webbrowser.get().open_new_tab('file://' + html_path)
    except ValueError as e:
        print(f"Error: {e}. Please provide valid numerical values for location.")
        print(HELP)


# change: we define the function "parse_arguments" which analyzes and
# validates arguments using argparse (looked up in python docs). This
# simplifies the processing of command-line-arguments.

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Visualization of WRF output at a single selected grid cell.")
    # sets the description the user will get when asking for help
    parser.add_argument('-p', '--parameter', help='WRF variable to plot')
    # adds a command-line argument, -p or --parameter. The argument expects a value, so here
    # a WRF varaiable able to plot.
    parser.add_argument('-l', '--location', nargs=3, type=float,
                        help='location and height above ground of the grid cell for which to plot the data')
    # This line adds another argument, -l or --location, which expects three values (latitude, longitude, and height above ground) as a list.
    # It specifies that these values should be converted to float type
    parser.add_argument('--no-browser', action='store_true',
                        help='do not open a browser with the newly generated visualization')
    # Here we have a boolean argument "--no-browser" to the parser. When we
    # have this flag, it is set to "true" and we will skip opening a browser
    # for the visualization.

    return parser.parse_args()
    # This line parses the command-line arguments using the configured parser and returns an
    # Namespace object containing the parsed values.


def wrfvis_gridcell():
    """Entry point for the wrfvis_gridcell application script"""
    # we use a try except block we learned about in the lecture
    # it handles possible exceptions during the execution of the script
    try:  # code within this block is attempted
        args = parse_arguments()
        gridcell(args)
    except Exception as e:  # if we get an exception during executing the try block
        # we store it here and the exception is stored in the variable e
        print(f"An unexpected error occurred: {e}")
        # this message is printed when an error occured


# checks, whether the script is run as the main program, e.g not
# imported as a module. We had that explicitly in the lecture, too.
# If it is the main program, wrfvis_gridcell function is called
if __name__ == "__main__":
    wrfvis_gridcell()  # if the script is the main programm in fact,
    # it calls the wrfvis_gridcell function and starts the execution of the script.
