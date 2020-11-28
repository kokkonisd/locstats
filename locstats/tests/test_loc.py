import os
import unittest

from locstats.definitions import BASE_DIR, LANG_DATA
from locstats.loc import get_source_files, get_loc


class TestLOC(unittest.TestCase):

    def test_get_files(self):
        self.maxDiff = None

        self.assertEqual(
            sorted(get_source_files(BASE_DIR, '.py', True)),
            sorted([
                os.path.join(BASE_DIR, 'definitions.py'),
                os.path.join(BASE_DIR, 'loc.py'),
                os.path.join(BASE_DIR, '__init__.py'),
                os.path.join(BASE_DIR, '__main__.py'),
                os.path.join(BASE_DIR, 'tests', 'test_loc.py'),
                os.path.join(BASE_DIR, 'tests', 'test_definitions.py'),
                os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.py'),
                os.path.join(BASE_DIR, 'tests', 'dummy_data', 'corner_case.py')
            ])
        )

        self.assertEqual(
            sorted(get_source_files(os.path.join(BASE_DIR, 'tests',),
                                    '.py',
                                    True)),
            sorted([
                os.path.join(BASE_DIR, 'tests', 'test_loc.py'),
                os.path.join(BASE_DIR, 'tests', 'test_definitions.py'),
                os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.py'),
                os.path.join(BASE_DIR, 'tests', 'dummy_data', 'corner_case.py')
            ])
        )


    def test_get_loc_c(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.c'),
                    strict=False,
                    comments=LANG_DATA['c']['comments'],
                    silent=False),
            (19, 9)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.c'),
                    strict=True,
                    comments=LANG_DATA['c']['comments'],
                    silent=False),
            (6, 0)
        )


    def test_get_loc_csharp(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.cs'),
                    strict=False,
                    comments=LANG_DATA['c#']['comments'],
                    silent=False),
            (24, 9)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.cs'),
                    strict=True,
                    comments=LANG_DATA['c#']['comments'],
                    silent=False),
            (9, 0)
        )


    def test_get_loc_cpp(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.cpp'),
                    strict=False,
                    comments=LANG_DATA['c++']['comments'],
                    silent=False),
            (19, 8)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.cpp'),
                    strict=True,
                    comments=LANG_DATA['c++']['comments'],
                    silent=False),
            (7, 0)
        )


    def test_get_loc_css(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.css'),
                    strict=False,
                    comments=LANG_DATA['css']['comments'],
                    silent=False),
            (18, 5)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.css'),
                    strict=True,
                    comments=LANG_DATA['css']['comments'],
                    silent=False),
            (9, 0)
        )


    def test_get_loc_d(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.d'),
                    strict=False,
                    comments=LANG_DATA['d']['comments'],
                    silent=False),
            (11, 4)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.d'),
                    strict=True,
                    comments=LANG_DATA['d']['comments'],
                    silent=False),
            (5, 0)
        )


    def test_get_loc_dart(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.dart'),
                    strict=False,
                    comments=LANG_DATA['dart']['comments'],
                    silent=False),
            (17, 7)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.dart'),
                    strict=True,
                    comments=LANG_DATA['dart']['comments'],
                    silent=False),
            (6, 0)
        )


    def test_get_loc_fsharp(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.fs'),
                    strict=False,
                    comments=LANG_DATA['f#']['comments'],
                    silent=False),
            (16, 8)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.fs'),
                    strict=True,
                    comments=LANG_DATA['f#']['comments'],
                    silent=False),
            (6, 0)
        )


    def test_get_loc_fortran(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.f'),
                    strict=False,
                    comments=LANG_DATA['fortran']['comments'],
                    silent=False),
            (6, 2)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.f'),
                    strict=True,
                    comments=LANG_DATA['fortran']['comments'],
                    silent=False),
            (3, 0)
        )


    def test_get_loc_go(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.go'),
                    strict=False,
                    comments=LANG_DATA['go']['comments'],
                    silent=False),
            (14, 7)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.go'),
                    strict=True,
                    comments=LANG_DATA['go']['comments'],
                    silent=False),
            (5, 0)
        )


    def test_get_loc_html(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.html'),
                    strict=False,
                    comments=LANG_DATA['html']['comments'],
                    silent=False),
            (20, 8)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.html'),
                    strict=True,
                    comments=LANG_DATA['html']['comments'],
                    silent=False),
            (9, 0)
        )


    def test_get_loc_java(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.java'),
                    strict=False,
                    comments=LANG_DATA['java']['comments'],
                    silent=False),
            (12, 5)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.java'),
                    strict=True,
                    comments=LANG_DATA['java']['comments'],
                    silent=False),
            (5, 0)
        )


    def test_get_loc_python(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.py'),
                    strict=False,
                    comments=LANG_DATA['python']['comments'],
                    silent=False),
            (10, 6)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'test.py'),
                    strict=True,
                    comments=LANG_DATA['python']['comments'],
                    silent=False),
            (1, 0)
        )


    def test_get_loc_python_corner_case(self):
        self.maxDiff = None

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'corner_case.py'),
                    strict=False,
                    comments=LANG_DATA['python']['comments'],
                    silent=False),
            (2, 0)
        )

        self.assertEqual(
            get_loc(filename=os.path.join(BASE_DIR, 'tests', 'dummy_data', 'corner_case.py'),
                    strict=True,
                    comments=LANG_DATA['python']['comments'],
                    silent=False),
            (1, 0)
        )
