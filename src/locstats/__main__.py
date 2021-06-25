#!/usr/bin/env python3
"""Define the entry point for the CLI tool."""

import argparse
import sys

from .definitions import __version__, LANG_DATA, info
from .loc import get_source_files, get_loc


def locstats_main() -> int:
    """Count the LOC in a given language in a given directory set."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.description = (
        "Determine the number of Lines Of Code written in a given language."
    )
    arg_parser.add_argument("language", nargs=1, help="the language to count LOC in")
    arg_parser.add_argument(
        "src_dirs", nargs="+", help="the directories in which to look for source files"
    )
    arg_parser.add_argument(
        "--strict",
        action="store_true",
        help="run in strict mode (ignore comments and empty lines)",
    )
    arg_parser.add_argument(
        "-m",
        "--minimal",
        action="store_true",
        help="give minimal output (just the LOC count)",
    )
    arg_parser.add_argument(
        "--silent",
        action="store_true",
        help="silence all warnings (such as directories not being found)",
    )
    arg_parser.add_argument(
        "-d",
        "--detailed",
        action="store_true",
        help="output a detailed list of LOC per file",
    )
    arg_parser.add_argument(
        "-v",
        "--version",
        help="print the version of locstats",
        action="version",
        version=f"locstats, version {__version__}",
    )
    args = arg_parser.parse_args()
    assert args is not None

    # Convert user-fed language to lowercase (see `data/languages.json`)
    language = args.language[0].lower()
    # Check if language exists in database
    if language not in LANG_DATA:
        info(
            f"The language `{language}` doesn't exist or hasn't yet been "
            "registered in our database."
        )

        info("\nHere's a list of all the languages we currently support:")
        print(f"{', '.join(sorted(LANG_DATA.keys()))}\n")

        info(
            "If you'd like to contribute, you can check out locstats' "
            "GitHub page: https://github.com/kokkonisd/locstats"
        )
        return 1

    loc_count_per_file = []

    for src in args.src_dirs:
        # Get all the source files from the given directories
        source_files = get_source_files(
            src_dir=src,
            src_extensions=LANG_DATA[language]["extensions"],
            silent=args.silent,
        )

        for filename in source_files:
            # Count the LOC in each file
            loc_count_per_file.append(
                (
                    filename,
                    get_loc(
                        filename=filename,
                        strict=args.strict,
                        comments=LANG_DATA[language]["comments"],
                        silent=args.silent,
                    ),
                )
            )

    # Remove files that don't count towards LOC
    loc_count_per_file = list(filter(lambda x: x[1][0] > 0, loc_count_per_file))

    total_loc_count = sum(x[1][0] for x in loc_count_per_file)
    comm_line_count = sum(x[1][1] for x in loc_count_per_file)

    # Give the LOC count to the user
    if args.minimal:
        # Just print the number
        print(total_loc_count)
    elif args.detailed:
        # Print the filenames along with their LOC count and the percentage of
        # the total LOC count they represent

        # Sort the files by descending LOC count
        loc_count_per_file = sorted(
            loc_count_per_file, key=lambda x: x[1][0], reverse=True
        )

        # Get the maximum filename length (in order to format output later)
        max_filename_length = max(list(map(lambda x: len(x[0]), loc_count_per_file)))

        # Print the "table"'s header
        print(f"FILENAME {' ' * (max_filename_length - 8)} LOC (%)")
        print("-" * (max_filename_length + 20))

        # Print the files, their LOC count and their % respective to the total
        # LOC count
        for filename, (loc, _) in loc_count_per_file:
            print(
                f"{filename}{' ' * (max_filename_length - len(filename))}: {loc} ({loc / total_loc_count * 100:.2f}%)"
            )

        print("-" * (max_filename_length + 20))
        print(f"TOTAL LOC{' ' * (max_filename_length - 9)}: {total_loc_count} (100%)")
    else:
        print(
            f"You have written approximately {total_loc_count} LOC in {LANG_DATA[language]['official_name']}",
            end="",
        )

        if (not args.strict) and (total_loc_count > 0):
            print(
                f", {comm_line_count / total_loc_count * 100:.2f}% of which are comments."
            )
        else:
            print(".")
    return 0


if __name__ == "__main__":
    sys.exit(locstats_main())
