from setuptools import find_packages
from distutils.core import setup
from danielsdatastructures import __version__, __name__, __author__
print("Packages found:", find_packages())

setup(
    name=__name__,
    version=__version__,
    description="A simple library of naively implemented data structures.",
    author=__author__,
    packages=find_packages()
)