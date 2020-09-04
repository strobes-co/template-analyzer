""" __Doc__ File handle class """
from setuptools import find_packages, setup
from PackageNameAnalyzer.__version__ import __version__


def dependencies(imported_file):
    """ __Doc__ Handles dependencies """
    with open(imported_file) as file:
        return file.read().splitlines()


with open("README.md") as file:
    setup(
        name="PackageName Analyzer",
        license="GPLv3",
        description="(analyzer-description)",
        long_description=file.read(),
        author="Akhil Reni",
        version=__version__,
        author_email="akhil@wesecureapp.com",
        url="https://strobes.co/",
        packages=find_packages(
            exclude=('test')),
        package_data={
            'PackageNameAnalyzer': [
                '*.txt',
                '*.json']},
        entry_points={
            'console_scripts': ['(analyzer-name)_analyzer = PackageNameAnalyzer.(analyzer-name)_analyzer:main']},
        include_package_data=True)