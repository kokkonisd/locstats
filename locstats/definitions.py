## 
## @package locstats
## @author Dimitri Kokkonis ([\@kokkonisd](https://github.com/kokkonisd))
## 
## This file contains useful definitions, such as the BASE_DIR path, and also 
## some helper functions.
##

import os
import json

VERSION = "1.0.10"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LANG_FILE = os.path.join(BASE_DIR, "languages.json")
with open(LANG_FILE, "r") as ext:
    LANG_DATA = json.loads(ext.read())


def info(message, ending = '\n'):
    """Prints a colored info message."""
    print(f"\033[33m{message}\033[0m", end = ending)


def warn(message, ending = '\n'):
    """Prints a colored warning message."""
    print(f"\033[91m/!\\ {message}\033[0m", end = ending)


def fail(message, ending = '\n'):
    """Prints a colored error message."""
    print(f"\033[31m{message}\033[0m", end = ending)


def esc_regex(string):
    """Escapes non-literal regex characters in a string."""
    return string.replace('[', '\\[')\
                 .replace(']', '\\]')\
                 .replace('\\', '\\\\')\
                 .replace('^', '\\^')\
                 .replace('$', '\\$')\
                 .replace('.', '\\.')\
                 .replace('|', '\\|')\
                 .replace('?', '\\?')\
                 .replace('*', '\\*')\
                 .replace('+', '\\+')\
                 .replace('(', '\\(')\
                 .replace(')', '\\)')
