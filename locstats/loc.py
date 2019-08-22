## 
## @package locstats
## @author Dimitri Kokkonis ([\@kokkonisd](https://github.com/kokkonisd))
## 
## This file contains useful functions to get the number of LOC from a given
## directory set.
##

import os
import re

from .definitions import esc_regex, warn


def get_source_files(src_dir, src_extensions, silent):
    """Returns a list of source files given a root directory and a file
    extension."""
    source_files = []

    if not os.path.exists(src_dir):
        if not silent:
            warn(f"Source directory `{src_dir}` doesn't exist. Skipping.")
        return source_files

    if os.path.isfile(src_dir):
        if not silent:
            warn(f"`{src_dir}` is a file, not a directory. Skipping.")
        return source_files


    for (dirpath, dirnames, filenames) in os.walk(src_dir):
        for file in filenames:
            name, extension = os.path.splitext(os.path.join(dirpath, file))
            if extension in src_extensions:
                source_files += [os.path.join(dirpath, file)]

    return source_files


def get_loc(file, strict, comments, silent):
    """Returns the LOC count given a file. Optionally strips out comments and
    blank lines"""
    with open(file, "r") as source:
        try:
            lines = source.read()
        except:
            if not silent:
                warn(f"Could not read file `{file}` (probably because it's "\
                     "not UTF-8). Skipping.")
            return 0
    
    if strict:
        for comment in comments["single_line"]:
            # Simulate ^ and $ characters, as for some reason the re.MULTILINE
            # flag doesn't work (and thus ^ and $ only match at the beginning
            # and at the end of the string, not at every line)
            lines = re.sub(f"([\n]?)[ \t]*{esc_regex(comment)}.+[ \t]*([\n]?)",
                           "\\1\\2",
                           lines)

        for start, stop in comments["multi_line"]:
            lines = re.sub(f"{esc_regex(start)}"\
                               f"((?!{esc_regex(stop)})[\\s\\S])*"\
                               f"{esc_regex(stop)}",
                           "",
                           lines)

        lines = list(filter(lambda x: len(x) > 0, lines.split('\n')))
    else:
        lines = lines.split('\n')

    return len(lines)
