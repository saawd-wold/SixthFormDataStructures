from setuptools import find_packages
from distutils.core import setup
from danielsdatastructures import __version__
print("Packages found:", find_packages())

setup(
    name="danielsdatastructures",
    version=__version__
    description="A simple library of naively implemented data structures.",
    author="Daniel Sääw",
    author_email="saawd@woldinghamschool.co.uk",
    packages=find_packages()
)