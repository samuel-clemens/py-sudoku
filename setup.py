from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name = 'MasterOfSudoku',
    version = '0.0.0',
    description = 'Sudoku solver and generator written in Python',
    long_description = readme,
    author = '',
    author_email = '',
    url = '',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)