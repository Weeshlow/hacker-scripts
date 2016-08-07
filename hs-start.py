# Author: Areeb Beigh
# Created: 10th April 2016

"""
Starts all the programs in config.ini [hs-start]
"""

import argparse
import os
import sys

from src import help
from src.errors import *
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
white_space = initializer.white_space
config_file = initializer.config_file
config_reader = ConfigReader(config_file)
# List of programs/files to be opened (will be filled later)
files = config_reader.read_config("hs-start")


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help',
                        '-help',
                        action='store_true')

    args = parser.parse_args()

    if args.help:
        cmd = sys.argv[0].partition(".")[0]
        help.display_help(cmd)
        return

    execute()


def execute():
    # At least one program / file must be specified in the config
    if len(files) > 0:
        for file in files:
            if os.path.isfile(file):
                print("{0} Opening {1}".format(white_space, file))
                os.startfile(file)
            else:
                print("{0} Skipping {1} since it does not exist".format(
                    white_space, file))
    else:
        raise ConfigError("No programs / files specified in the configuration file")


if __name__ == "__main__":
    main()