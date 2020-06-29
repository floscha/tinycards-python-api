from setuptools import setup, find_packages

NAME = 'tinycards'

setup(
    name=NAME,
    version='0.281',
    description="An unofficial Python API for Tinycards by Duolingo",
    url='https://github.com/floscha/tinycards-python-api',
    author='Florian Schäfer',
    author_email='florian.joh.schaefer@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests==2.24.0',
        'requests-toolbelt==0.9.1',
        'retrying==1.3.3',
        'typer==0.3.0'
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'tinycards = tinycards.client.cli:app',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development'
    ]
)
