# This setup.py file is used to package the find_salon module as a Python package.
# It includes metadata about the package, dependencies, and entry points for command-line scripts.
# To install the package, run:
# pip install .
# To build the package, run:
# python setup.py sdist bdist_wheel
# To upload the package to PyPI, use twine:
# twine upload dist/*
# To install the package from PyPI, use:
# pip install find-salon
# Note: Make sure to have the necessary permissions and configurations set up for uploading to PyPI.
# This setup.py file is designed to be used with Python 3.8 or higher.
# It specifies the required dependencies and the entry point for the command-line interface.
# The package will be installed in the Python environment, and the command 'find-salon' will be available in the terminal.
# The find_salon package contains the main logic for scraping Google Maps to find salons.
# The setup.py file is essential for packaging and distributing the find_salon module.
# It allows users to easily install the package and its dependencies.
# This setup.py file is structured to be compatible with Python's packaging standards.
# It uses setuptools to define the package metadata and dependencies.
# The find_salon package is designed to be a command-line tool for finding salons.
# The entry point 'find-salon' maps to the main function in the find_salon.main module.
# This setup.py file is a standard way to package Python projects.
# It ensures that the find_salon package can be easily installed and used by others.
# The setup.py file is crucial for the distribution of the find_salon package.

from setuptools import find_packages, setup

setup(
    name="find-salon",
    version="1.0.0",
    packages=find_packages(),  # will find find_salon package
    include_package_data=True,
    author="Purushottam Prabhakar",
    author_email="purushottam.prab@gmail.com",
    url="https://github.com/Purushottam1024",
    install_requires=[
        "selenium==4.20.0",
        "webdriver-manager==4.0.1",
        "openpyxl==3.1.2",
    ],
    entry_points={
        "console_scripts": [
            "find-salon=find_salon.main:main",  # <-- package prefix here
        ],
    },
    description="A CLI tool to find salons near a location using Google Maps scraping.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS ubuntu 24.4",
    ],
    python_requires=">=3.8",
)
