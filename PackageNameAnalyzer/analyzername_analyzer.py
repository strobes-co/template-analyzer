#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import traceback
from argparse import Namespace
from typing import NoReturn, List
from PackageNameAnalyzer.input import parse_args
from PackageNameAnalyzer.logging import get_logger


logger = None

# Note: Typing & docstring use is must for better documentation and
#       readability of code, Use understandable names for variables
#       which reflects the kind of data saved in that variable


def scan(arguments: Namespace, unknown: List[str]) -> NoReturn:
    """ Runs the dependency scan on the dependency meta file
    Args:
        arguments (Namespace): Arguments object parsed by argparse
        unknown (List[str]): Unidentified args by argparse
    Returns:
        NoReturn
    """
    try:
        logger.info("Analyzer Scan Started!")
        # Write your code here
        logger.info("Analyzer Scan Completed!")
    except Exception as err:
        logger.error(str(err))
        logger.debug(traceback.format_exc())


def main():
    global logger
    arguments, unknown = parse_args()
    os.environ["LOG_LEVEL"] = arguments.loglevel
    logger = get_logger()
    scan(arguments, unknown)


if __name__ == "__main__":
    main()
