from setuptools import setup, find_packages

print("Packages found:", find_packages())

setup(
    name="danielsdatastructures",
    version="0.0.14",
    description="A simple library of naively implemented data structures.",
    author="Daniel Sääw",
    author_email="saawd@woldinghamschool.co.uk",
    packages=find_packages(),
)