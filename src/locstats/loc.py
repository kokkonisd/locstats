"""Get the Lines Of Code count."""

import os
import re

from .definitions import esc_regex, warn


def get_source_files(src_dir, src_extensions, silent=False):
    """Return a list of source files given a root directory and a file extension."""
    source_files = []

    if not os.path.exists(src_dir):
        if not silent:
            warn(f"Source directory `{src_dir}` doesn't exist. Skipping.")
        return source_files

    if os.path.isfile(src_dir):
        if not silent:
            warn(f"`{src_dir}` is a file, not a directory. Skipping.")
        return source_files

    for dirpath, _dirnames, filenames in os.walk(src_dir):
        for file in filenames:
            name, extension = os.path.splitext(os.path.join(dirpath, file))
            if extension in src_extensions:
                source_files += [os.path.join(dirpath, file)]

    return source_files


def get_loc(filename, strict, comments, silent=False):
    """Return the LOC count and the comment-line count given a file.

    Optionally strip out comments and blank lines.
    """
    with open(filename, "r") as source:
        try:
            lines = source.read()
        except UnicodeDecodeError:
            if not silent:
                warn(f"Could not read file `{filename}` (it's not UTF-8). Skipping.")
            return (0, 0)

    comm_lines = []

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
            raw_matches = list(map(lambda x: x[0], re.findall(comm_multi_regex, lines)))
            multi_comm_lines = list(map(lambda x: x.split("\n"), raw_matches))

            for section in multi_comm_lines:
                if len(section) >= 1 and section[0] == "":
                    section.pop(0)

            # Flatten multi comm lines list
            multi_comm_lines_flat = [
                item for sublist in multi_comm_lines for item in sublist
            ]
            comm_lines += multi_comm_lines_flat
            # Strip multi-line comments to stop them from interfering with single-line ones
            lines = re.sub(comm_multi_regex, "\\2", lines)
            # Replace stripped multi-line comments with empty lines, line count should still be the same
            lines += "\n" * len(multi_comm_lines_flat)

    for comment in comments["single_line"]:
        # Simulate ^ and $ characters, as for some reason the re.MULTILINE flag doesn't work (and thus ^ and $ only
        # match at the beginning and at the end of the string, not at every line)
        comm_single_regex = f"((^|\n)[ \t]*{esc_regex(comment)}.+[ \t]*)"

        # If in strict mode, remove all single line comments
        if strict:
            lines = re.sub(comm_single_regex, "", lines)
        else:
            # Collect all single line comments
            comm_lines += list(
                map(lambda x: x[0], re.findall(comm_single_regex, lines))
            )

    if strict:
        lines = list(filter(lambda x: len(x) > 0, lines.split("\n")))
    else:
        lines = lines.split("\n")

    return len(lines), len(comm_lines)
