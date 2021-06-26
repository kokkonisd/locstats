import os

from locstats.definitions import BASE_DIR, LANG_DATA
from locstats.loc import get_source_files, get_loc


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


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


def test_get_loc_c():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.c"),
        strict=False,
        comments=LANG_DATA["c"]["comments"],
    )
    expected_full = (19, 9)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.c"),
        strict=True,
        comments=LANG_DATA["c"]["comments"],
    )
    expected_strict = (6, 0)
    assert result_strict == expected_strict


def test_get_loc_csharp():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.cs"),
        strict=False,
        comments=LANG_DATA["c#"]["comments"],
    )
    expected_full = (24, 9)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.cs"),
        strict=True,
        comments=LANG_DATA["c#"]["comments"],
    )
    expected_strict = (9, 0)
    assert result_strict == expected_strict


def test_get_loc_cpp():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.cpp"),
        strict=False,
        comments=LANG_DATA["c++"]["comments"],
    )
    expected_full = (19, 8)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.cpp"),
        strict=True,
        comments=LANG_DATA["c++"]["comments"],
    )
    expected_strict = (7, 0)
    assert result_strict == expected_strict


def test_get_loc_css():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.css"),
        strict=False,
        comments=LANG_DATA["css"]["comments"],
    )
    expected_full = (18, 5)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.css"),
        strict=True,
        comments=LANG_DATA["css"]["comments"],
    )
    expected_strict = (9, 0)
    assert result_strict == expected_strict


def test_get_loc_d():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.d"),
        strict=False,
        comments=LANG_DATA["d"]["comments"],
    )
    expected_full = (11, 4)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.d"),
        strict=True,
        comments=LANG_DATA["d"]["comments"],
    )
    expected_strict = (5, 0)
    assert result_strict == expected_strict


def test_get_loc_dart():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.dart"),
        strict=False,
        comments=LANG_DATA["dart"]["comments"],
    )
    expected_full = (17, 7)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.dart"),
        strict=True,
        comments=LANG_DATA["dart"]["comments"],
    )
    expected_strict = (6, 0)
    assert result_strict == expected_strict


def test_get_loc_fsharp():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.fs"),
        strict=False,
        comments=LANG_DATA["f#"]["comments"],
    )
    expected_full = (16, 8)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.fs"),
        strict=True,
        comments=LANG_DATA["f#"]["comments"],
    )
    expected_strict = (6, 0)
    assert result_strict == expected_strict


def test_get_loc_fortran():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.f"),
        strict=False,
        comments=LANG_DATA["fortran"]["comments"],
    )
    expected_full = (6, 2)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.f"),
        strict=True,
        comments=LANG_DATA["fortran"]["comments"],
    )
    expected_strict = (3, 0)
    assert result_strict == expected_strict


def test_get_loc_go():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.go"),
        strict=False,
        comments=LANG_DATA["go"]["comments"],
    )
    expected_full = (14, 7)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.go"),
        strict=True,
        comments=LANG_DATA["go"]["comments"],
    )
    expected_strict = (5, 0)
    assert result_strict == expected_strict


def test_get_loc_html():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.html"),
        strict=False,
        comments=LANG_DATA["html"]["comments"],
    )
    expected_full = (20, 8)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.html"),
        strict=True,
        comments=LANG_DATA["html"]["comments"],
    )
    expected_strict = (9, 0)
    assert result_strict == expected_strict


def test_get_loc_java():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.java"),
        strict=False,
        comments=LANG_DATA["java"]["comments"],
    )
    expected_full = (12, 5)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.java"),
        strict=True,
        comments=LANG_DATA["java"]["comments"],
    )
    expected_strict = (5, 0)
    assert result_strict == expected_strict


def test_get_logc_javascript():
    pass


def test_get_logc_julia():
    pass


def test_get_logc_latex():
    pass


def test_get_logc_markdown():
    pass


def test_get_logc_matlab():
    pass


def test_get_logc_mipsasm():
    pass


def test_get_logc_objectivec():
    pass


def test_get_logc_perl():
    pass


def test_get_logc_php():
    pass


def test_get_loc_python():
    result_full = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.py"),
        strict=False,
        comments=LANG_DATA["python"]["comments"],
    )
    expected_full = (10, 6)
    assert result_full == expected_full

    result_strict = get_loc(
        source_file=os.path.join(TEST_DATA_DIR, "test.py"),
        strict=True,
        comments=LANG_DATA["python"]["comments"],
    )
    expected_strict = (1, 0)
    assert result_strict == expected_strict


def test_get_logc_r():
    pass


def test_get_logc_ruby():
    pass


def test_get_logc_rust():
    pass


def test_get_logc_swift():
    pass


def test_get_logc_typescript():
    pass


def test_get_logc_verilog():
    pass


def test_get_logc_vhdl():
    pass


def test_get_logc_x86asm():
    pass


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
