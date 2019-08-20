import os
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
EXTENSIONS_FILE = os.path.join(ROOT_DIR, "languages.json")
with open(EXTENSIONS_FILE, "r") as ext:
        LANG_DATA = json.loads(ext.read())


def info (message, ending = '\n'):
    print(f"\033[33m{message}\033[0m", end = ending)

def fail (message, ending = '\n'):
    print(f"\033[31m{message}\033[0m", end = ending)
