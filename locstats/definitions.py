import os
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
EXTENSIONS_FILE = os.path.join(ROOT_DIR, "languages.json")
with open(EXTENSIONS_FILE, "r") as ext:
        LANG_DATA = json.loads(ext.read())
