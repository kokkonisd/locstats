import os

from locstats.definitions import BASE_DIR, LANG_DATA
from locstats.loc import get_source_files, get_loc


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

TEST_LANGUAGE_DATA = {
    "ada": {
        "file": "test.adb",
        "expected_full": (11, 1),
        "expected_strict": (6, 0),
    },
    "arduino-code": {
        "file": "test.ino",
        "expected_full": (16, 7),
        "expected_strict": (6, 0),
    },
    "c": {
        "file": "test.c",
        "expected_full": (19, 9),
        "expected_strict": (6, 0),
    },
    "c#": {
        "file": "test.cs",
        "expected_full": (24, 9),
        "expected_strict": (9, 0),
    },
    "c++": {
        "file": "test.cpp",
        "expected_full": (19, 8),
        "expected_strict": (7, 0),
    },
    "css": {
        "file": "test.css",
        "expected_full": (18, 5),
        "expected_strict": (9, 0),
    },
    "d": {
        "file": "test.d",
        "expected_full": (11, 4),
        "expected_strict": (5, 0),
    },
    "dart": {
        "file": "test.dart",
        "expected_full": (17, 7),
        "expected_strict": (6, 0),
    },
    "f#": {
        "file": "test.fs",
        "expected_full": (16, 8),
        "expected_strict": (6, 0),
    },
    "fortran": {
        "file": "test.f",
        "expected_full": (6, 2),
        "expected_strict": (3, 0),
    },
    "go": {
        "file": "test.go",
        "expected_full": (14, 7),
        "expected_strict": (5, 0),
    },
    "html": {
        "file": "test.html",
        "expected_full": (20, 8),
        "expected_strict": (9, 0),
    },
    "java": {
        "file": "test.java",
        "expected_full": (12, 5),
        "expected_strict": (5, 0),
    },
    "python": {
        "file": "test.py",
        "expected_full": (10, 6),
        "expected_strict": (1, 0),
    },
}


def test_get_files():
    result = [os.path.split(f)[-1] for f in get_source_files(BASE_DIR, ".py", True)]
    expected = [
        "definitions.py",
        "loc.py",
        "__init__.py",
        "__main__.py",
    ]
    assert sorted(result) == sorted(expected)


def test_non_existing_directory():
    """Test with a directory that does not exist."""
    result = get_source_files(
        source_dir="thisistotallyadirectorythatexistsyepsure",
        source_file_extensions=".py",
    )
    assert result == []


def test_file_instead_of_directory():
    """Test with a file instead of a directory."""
    result = get_source_files(
        source_dir=os.path.join(BASE_DIR, "__init__.py"),
        source_file_extensions=".py",
    )
    assert result == []


def test_get_loc_python_corner_case():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "corner_case.py"),
        strict=False,
        comments=LANG_DATA["python"]["comments"],
    )
    expected_full = (2, 0)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "corner_case.py"),
        strict=True,
        comments=LANG_DATA["python"]["comments"],
    )
    expected_strict = (1, 0)
    assert result_strict == expected_strict


def test_get_loc_languages():
    for language in TEST_LANGUAGE_DATA:
        result_full = get_loc(
            source_file=os.path.join(
                TEST_DATA_DIR, TEST_LANGUAGE_DATA[language]["file"]
            ),
            strict=False,
            comments=LANG_DATA[language]["comments"],
        )
        result_strict = get_loc(
            source_file=os.path.join(
                TEST_DATA_DIR, TEST_LANGUAGE_DATA[language]["file"]
            ),
            strict=True,
            comments=LANG_DATA[language]["comments"],
        )

        assert (
            result_full == TEST_LANGUAGE_DATA[language]["expected_full"]
        ), f"unexpected full result for {language}"
        assert (
            result_strict == TEST_LANGUAGE_DATA[language]["expected_strict"]
        ), f"unexpected strict result for {language}"
