import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LANG_FILE = os.path.join(BASE_DIR, "languages.json")
with open(LANG_FILE, "r") as ext:
        LANG_DATA = json.loads(ext.read())


def info(message, ending = '\n'):
    print(f"\033[33m{message}\033[0m", end = ending)

def fail(message, ending = '\n'):
    print(f"\033[31m{message}\033[0m", end = ending)
