
#!/usr/bin/env python3

import sys
import os
import click

from .definitions import LANG_DATA
from .loc import get_source_files, get_loc


@click.command()
@click.argument('language', nargs = 1)
@click.argument('src_dirs', nargs = -1)
@click.option('-s', '--strict',
              is_flag = True,
              default = False,
              help = "Run in strict mode (ignore comments and empty lines).")
def main (strict, language, src_dirs):
    """The main function."""

    if language not in LANG_DATA:
        print(f"The language `{language}` doesn't exist or hasn't yet been "\
              "put into our database.\nIf you'd like to contribute, you can "\
              "check out locstats' GitHub page: "\
              "https://github.com/kokkonisd/locstats")
        exit(1)



    total_loc_count = 0

    for src in src_dirs:
        source_files = get_source_files(src,
                                        LANG_DATA[language]["extensions"])
        for file in source_files:
            total_loc_count += get_loc(file,
                                       strict,
                                       LANG_DATA[language]["comments"])

    print(f"You have written approximately {total_loc_count} LOC in "\
          f"{LANG_DATA[language]['official_name']}.")



if __name__ == "__main__":
    main()
