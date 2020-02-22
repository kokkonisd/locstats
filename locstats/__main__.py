## 
## @package locstats
## @author Dimitri Kokkonis ([\@kokkonisd](https://github.com/kokkonisd))
## 
## This is the entry point for the `locstats` tool.
## 

import sys
import os
import click

from .definitions import VERSION, LANG_DATA, info, fail
from .loc import get_source_files, get_loc


@click.command()
@click.argument('language', nargs = 1) # Exactly one argument
@click.argument('src_dirs', nargs = -1) # Unlimited arguments
@click.option('--strict',
              is_flag = True,
              default = False,
              help = "Run in strict mode (ignore comments and empty lines).")
@click.option('-m', '--minimal',
              is_flag = True,
              default = False,
              help = "Give minimal output (just the LOC count).")
@click.option('--silent',
              is_flag = True,
              default = False,
              help = "Silence all warnings (such as directories not being "\
                     "found).")
@click.option('-d', '--detailed',
              is_flag = True,
              default = False,
              help = "Output a detaled list of LOC per file.")
@click.version_option(version = VERSION,
                      prog_name = "locstats")
def main(language, src_dirs, strict, minimal, silent, detailed):
    """Counts the LOC in a given language in a given directory set."""

    # Convert user-fed language to lowercase (see `languages.json`)
    language = language.lower()
    # Check if language exists in database
    if language not in LANG_DATA:
        info(f"The language `{language}` doesn't exist or hasn't yet been "\
              "registered in our database.")

        info("\nHere's a list of all the languages we currently support:")
        print(f"{', '.join(sorted(list(LANG_DATA.keys())))}\n")

        info("If you'd like to contribute, you can check out locstats' "\
             "GitHub page: https://github.com/kokkonisd/locstats")
        exit(1)


    loc_count_per_file = []

    for src in src_dirs:
        # Get all the source files from the given directories
        source_files = get_source_files(
            src_dir = src,
            src_extensions = LANG_DATA[language]["extensions"],
            silent = silent
        )

        for file in source_files:
            # Count the LOC in each file
            loc_count_per_file.append((
                file,
                get_loc(file = file,
                        strict = strict,
                        comments = LANG_DATA[language]["comments"],
                        silent = silent)
            ))

    total_loc_count = sum(x[1] for x in loc_count_per_file)

    # Give the LOC count to the user
    if minimal:
        # Just print the number
        print(total_loc_count)
    elif detailed:
        # Print the filenames along with their LOC count and the percentage of
        # the total LOC count they represent
        
        # Sort the files by descending LOC count
        loc_count_per_file = sorted(loc_count_per_file,
                                    key = lambda x: x[1],
                                    reverse = True)

        # Get the maximum filename length (in order to format output later)
        max_filename_length = max(list(map(lambda x: len(x[0]),
                                           loc_count_per_file)))
        # Print the files, their LOC count and their % respective to the total
        # LOC count
        for file, loc in loc_count_per_file:
          print(f"{file}{' ' * (max_filename_length - len(file))} : "\
                f"{loc} ({loc / total_loc_count * 100:.2f}%)")

        print("----")
        print(f"TOTAL LOC{' ' * (max_filename_length - 9)} : "\
              f"{total_loc_count} (100%)")
    else:
        print(f"You have written approximately {total_loc_count} LOC in "\
              f"{LANG_DATA[language]['official_name']}.")


if __name__ == "__main__":
    main()
