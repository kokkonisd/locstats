import sys
import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
EXTENSIONS_FILE = os.path.join(ROOT_DIR, "language_extensions.json")


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


def get_loc (file):
    with open(file, "r") as source:
        lines = source.read().split("\n")

    # lines = list(filter(lambda x: len(x) > 0, lines))
    return len(lines)


def main ():
    """The main function."""
    if len(sys.argv) < 3:
        print("Usage: locstats <language> <source dir 1> <source dir 2> ...")
        exit(1)

    language = sys.argv[1]
    source_dirs = sys.argv[2:]

    with open(EXTENSIONS_FILE, "r") as ext:
        extensions = json.loads(ext.read())

    if language.lower() not in extensions:
        print(f"The language `{language}` doesn't exist or hasn't yet been "\
              "put into our database.\nIf you'd like to contribute, you can "\
              "check out locstats' GitHub page: "\
              "https://github.com/kokkonisd/locstats")
        exit(1)



    total_loc_count = 0

    for src in source_dirs:
        source_files = get_source_files(src, extensions[language.lower()])
        for file in source_files:
            total_loc_count += get_loc(file)

    print(f"You have written approximately {total_loc_count} LOC in "\
          f"{language}.")



if __name__ == "__main__":
    main()
