"""Get the Lines Of Code count."""

import os
import re
from typing import List, Dict, Tuple, Any

from .definitions import esc_regex, warn


def get_source_files(
    source_dir: str, source_file_extensions: List[str], silent: bool = False
) -> List[str]:
    """Return a list of source files given a root directory and a file extension.

    :param source_dir: the source directory (containing the source files)
    :param source_file_extensions: the extensions of the source files to look for
    :param silent: if True, run in silent mode
    :return: the list of source files found
    """
    source_files: List[str] = []

    if not os.path.exists(source_dir):
        if not silent:
            warn(f"Source directory `{source_dir}` doesn't exist. Skipping.")
        return source_files

    if not os.path.isdir(source_dir):
        if not silent:
            warn(f"`{source_dir}` is not a directory. Skipping.")
        return source_files

    for dirpath, _dirnames, filenames in os.walk(source_dir):
        for file in filenames:
            name, extension = os.path.splitext(os.path.join(dirpath, file))
            if extension in source_file_extensions:
                source_files += [os.path.join(dirpath, file)]

    return source_files


def get_loc(
    source_file: str,
    strict: bool,
    comments: Dict[str, Any],
    silent: bool = False,
) -> Tuple[int, int]:
    """Return the LOC count and the comment-line count given a file.

    Optionally strip out comments and blank lines.

    :param source_file: the path to the source file
    :param strict: if True, do not count comments and empty lines
    :param comments: the single-line and multi-line comments for the language of the
        file
    :param silent: if True, run in silent mode
    :return: the LOC count and the comment-line count in tuple form: (loc, comments)
    """
    # Read the raw source code
    with open(source_file, "r") as source:
        try:
            lines = source.read()
        except UnicodeDecodeError:
            if not silent:
                warn(f"Could not read file `{source_file}` (it's not UTF-8). Skipping.")
            return (0, 0)

    comm_lines = []
    lines_of_code = []

    # Handle multi-line comments
    for start, stop in comments["multi_line"]:
        comm_multi_regex = (
            f"((^|\n)[ \t]*{esc_regex(start)}"
            f"((?!{esc_regex(stop)})[\\s\\S])*"
            f"{esc_regex(stop)}[ \t]*)\n"
        )

        # If in strict mode, remove all multi line comments
        if strict:
            lines = re.sub(comm_multi_regex, "\\2", lines)
        else:
            # Collect all multi line comments
            #
            # Because of the leading and trailing \n characters in the regex, sometimes
            # an empty line will be prepended or appended, increasing the comment line
            # count. In order to avoid that, we strip the matched multi-line comment
            # before splitting it into lines.
            multi_comm_lines = [
                line
                for match in re.findall(comm_multi_regex, lines)
                for line in match[0].strip().split("\n")
            ]

            comm_lines += multi_comm_lines
            # Strip multi-line comments to stop them from interfering with single-line ones
            lines = re.sub(comm_multi_regex, "\\2", lines)
            # Replace stripped multi-line comments with empty lines, line count should still be the same
            lines += "\n" * len(multi_comm_lines)

    # Handle single-line comments
    for comment in comments["single_line"]:
        # Simulate ^ and $ characters, as for some reason the re.MULTILINE flag doesn't work (and thus ^ and $ only
        # match at the beginning and at the end of the string, not at every line)
        comm_single_regex = f"((^|\n)[ \t]*{esc_regex(comment)}.+[ \t]*)"

        # If in strict mode, remove all single line comments
        if strict:
            lines = re.sub(comm_single_regex, "", lines)
        else:
            # Collect all single line comments
            comm_lines += [match[0] for match in re.findall(comm_single_regex, lines)]

    if strict:
        # Strip empty lines (comments have been replaced by empty lines at this point,
        # so they will be stripped as well)
        lines_of_code = [line for line in lines.split("\n") if line]
    else:
        lines_of_code = lines.split("\n")

    return len(lines_of_code), len(comm_lines)
