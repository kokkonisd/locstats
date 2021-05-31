import os

from locstats.definitions import LANG_FILE


def test_languages_file():
    """Sanity-check that the language file is where it's supposed to be."""
    print(LANG_FILE)
    assert os.path.exists(LANG_FILE)
    assert os.path.isfile(LANG_FILE)
