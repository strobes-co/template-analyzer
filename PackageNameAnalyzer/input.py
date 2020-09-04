# Arguments to be taken by the analyzer will be defined here

from argparse import ArgumentParser, Namespace
from typing import List, Tuple


def parse_args() -> Tuple[Namespace, List[str]]:
    """ Function that parses arguments from command line

    Returns:
        Tuple[Namespace, List[str]]: Known arguments will be passed
        passed in Namespace object while unknown will be passed in list
    """    
    parser = ArgumentParser()

    parser.add_argument(
        "-log",
        dest="loglevel",
        default="DEBUG",
        help="Log Level(DEBUG, INFO , WARNING , ERROR or CRITICAL)")

    # Add your arguments here

    args, unknown = parser.parse_known_args()

    return args, unknown