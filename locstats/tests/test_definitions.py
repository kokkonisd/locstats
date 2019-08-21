import os
import unittest

from locstats.definitions import LANG_FILE


class TestDefinitions(unittest.TestCase):

    def test_languages_file(self):
        self.assertTrue(os.path.exists(LANG_FILE))
        self.assertTrue(os.path.isfile(LANG_FILE))

