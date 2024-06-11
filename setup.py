from setuptools import setup
from setuptools import find_packages

long_description= """
# jlu
A collection of functions I use to make my JupyterLab notebooks cleaner.
"""

required = [
    "requests", 
    "numpy"
]

setup(
    name="jlu",
    version="0.0.1",
    description="A collection of functions I use to make my JupyterLab notebooks cleaner.",
    long_description=long_description,
    author="Jacob Hart",
    author_email="jacob.dchart@gmail.com",
    url="https://github.com/jdchart/jlu",
    install_requires=required,
    packages=find_packages()
)