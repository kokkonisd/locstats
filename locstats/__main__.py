
#!/usr/bin/env python3

import sys
import json
import os
import click
import re


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
EXTENSIONS_FILE = os.path.join(ROOT_DIR, "languages.json")
with open(EXTENSIONS_FILE, "r") as ext:
        LANG_DATA = json.loads(ext.read())


def get_source_files (src_dir, src_extensions):
    source_files = []

    if not os.path.exists(src_dir):
            print(f"Source directory `{src_dir}` doesn't exist. Skipping.")
            return source_files

    if os.path.isfile(src_dir):
            print(f"`{src_dir}` is a file, not a directory. Skipping.")
            return source_files


    for (dirpath, dirnames, filenames) in os.walk(src_dir):
        for file in filenames:
            name, extension = os.path.splitext(os.path.join(dirpath, file))
            if extension in src_extensions:
                source_files += [os.path.join(dirpath, file)]

    return source_files


def get_loc (file, strict, comments):
    with open(file, "r") as source:
        try:
            lines = source.read()
        except:
            print(f"Could not read file `{file}` (probably because it's not "\
                  "UTF-8). Skipping.")
            return 0
        
    if strict:
        for comment in comments:
            lines = re.sub(comment, "", lines)

        lines = list(filter(lambda x: len(x) > 0, lines.split('\n')))
    else:
        lines = lines.split('\n')

    return len(lines)



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
