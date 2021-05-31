import setuptools

from src.locstats.definitions import __version__, __author__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="locstats",
    version=__version__,
    author=__author__,
    author_email="kokkonisd@gmail.com",
    description="A statistics tool for your LOC per language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kokkonisd/locstats",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click"],
    packages=["locstats"],
    package_dir={"locstats": "src/locstats"},
    include_package_data=True,
    package_data={"locstats": ["data/languages.json"]},
    entry_points={
        "console_scripts": [
            "locstats = locstats.__main__:main",
        ],
    },
    python_requires=">=3.6",
)
