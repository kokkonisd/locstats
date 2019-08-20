import os
import re


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
