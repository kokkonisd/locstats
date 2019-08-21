import os
import unittest

from locstats.definitions import BASE_DIR
from locstats.loc import get_source_files, get_loc


class TestLOC(unittest.TestCase):

    def test_get_files(self):
        self.maxDiff = None

        self.assertEqual(
            sorted(get_source_files(BASE_DIR, '.py')),
            sorted([
                os.path.join(BASE_DIR, 'definitions.py'),
                os.path.join(BASE_DIR, 'loc.py'),
                os.path.join(BASE_DIR, '__init__.py'),
                os.path.join(BASE_DIR, '__main__.py'),
                os.path.join(BASE_DIR, 'tests', 'test_loc.py'),
                os.path.join(BASE_DIR, 'tests', 'test_definitions.py'),
            ])
        )

        self.assertEqual(
            sorted(get_source_files(os.path.join(BASE_DIR, 'tests'), '.py')),
            sorted([
                os.path.join(BASE_DIR, 'tests', 'test_loc.py'),
                os.path.join(BASE_DIR, 'tests', 'test_definitions.py'),
            ])
        )


    def test_get_loc(self):
        self.maxDiff = None

        
