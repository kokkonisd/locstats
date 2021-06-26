import subprocess
import os
import sys

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def test_cli_no_args():
    """Test a call with no arguments."""
    res = subprocess.run([sys.executable, "-m", "locstats"])
    # A call without arguments should fail
    assert res.returncode == 2


def test_cli_unknown_language():
    """Test a call with an unknown language."""
    res = subprocess.run(
        [
            sys.executable,
            "-m",
            "locstats",
            "thisistotallyalanguagethatexistsyepsure",
            TEST_DATA_DIR,
        ]
    )
    assert res.returncode == 1


def test_cli_python_vanilla():
    """Test a "vanilla" call on Python sources."""
    res = subprocess.run([sys.executable, "-m", "locstats", "python", TEST_DATA_DIR])
    assert res.returncode == 0


def test_cli_python_minimal():
    """Test a call on Python sources with the minimal switch."""
    res = subprocess.run(
        [sys.executable, "-m", "locstats", "python", TEST_DATA_DIR, "-m"]
    )
    assert res.returncode == 0


def test_cli_python_detailed():
    """Test a call on Python sources with the detailed switch."""
    res = subprocess.run(
        [sys.executable, "-m", "locstats", "python", TEST_DATA_DIR, "-d"]
    )
    assert res.returncode == 0


def test_cli_python_strict():
    """Test a call on Python sources with the strict switch."""
    res = subprocess.run(
        [sys.executable, "-m", "locstats", "python", TEST_DATA_DIR, "--strict"]
    )
    assert res.returncode == 0


def test_cli_minimal_detailed_conflict():
    """Test a call with both minimal and detailed switches activated."""
    res = subprocess.run(
        [sys.executable, "-m", "locstats", "python", TEST_DATA_DIR, "-m", "-d"]
    )
    # These options are mutually exclusive, so the call should fail
    assert res.returncode == 2
