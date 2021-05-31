"""Define useful constants and functions."""

import os
import json
import pkg_resources

__version_info__ = ("1", "0", "11")
__version__ = ".".join(__version_info__)
__author__ = "Dimitri Kokkonis"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LANG_FILE = pkg_resources.resource_filename(__name__, "data/languages.json")
LANG_DATA = json.loads(pkg_resources.resource_string(__name__, "data/languages.json"))


def info(message, ending="\n"):
    """Print a colored info message."""
    print(f"\033[33m{message}\033[0m", end=ending)


def warn(message, ending="\n"):
    """Print a colored warning message."""
    print(f"\033[91m/!\\ {message}\033[0m", end=ending)


def fail(message, ending="\n"):
    """Print a colored error message."""
    print(f"\033[31m{message}\033[0m", end=ending)


def esc_regex(string):
    """Escape non-literal regex characters in a string."""
    return (
        string.replace("[", "\\[")
        .replace("]", "\\]")
        .replace("\\", "\\\\")
        .replace("^", "\\^")
        .replace("$", "\\$")
        .replace(".", "\\.")
        .replace("|", "\\|")
        .replace("?", "\\?")
        .replace("*", "\\*")
        .replace("+", "\\+")
        .replace("(", "\\(")
        .replace(")", "\\)")
    )
