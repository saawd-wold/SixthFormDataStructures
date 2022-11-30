from setuptools import find_packages
from distutils.core import setup
print("Packages found:", find_packages())

setup(
    name="danielsdatastructures",
    version="0.2.2",
    description="A simple library of naively implemented data structures.",
    author="Daniel Sääw",
    author_email="saawd@woldinghamschool.co.uk",
    packages=find_packages()
)