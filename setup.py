from setuptools import setup, find_packages

NAME = 'tinycards'

requirements = list(open('requirements.txt', 'r').readlines())

setup(
    name=NAME,
    version='0.2',
    description="An unofficial Python API for Tinycards by Duolingo",
    url='https://github.com/floscha/tinycards-python-api',
    author='Florian Schäfer',
    author_email='florian.joh.schaefer@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements,
    zip_safe=False
)