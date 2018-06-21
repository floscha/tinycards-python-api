<img src="temporary_logo.png" width="128">

# Tinycards Python API
[![Build Status](https://travis-ci.org/floscha/tinycards-python-api.svg?branch=master)](https://travis-ci.org/floscha/tinycards-python-api)
[![Coverage Status](https://coveralls.io/repos/github/floscha/tinycards-python-api/badge.svg?branch=master)](https://coveralls.io/github/floscha/tinycards-python-api?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d7f70b4f2a134b268a9ca610fc0208f9)](https://www.codacy.com/app/floscha/tinycards-python-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=floscha/tinycards-python-api&amp;utm_campaign=Badge_Grade)
[![Python Versions](https://img.shields.io/pypi/pyversions/toga.svg)](https://pypi.python.org/pypi/tinycards)
[![PyPI Version](https://img.shields.io/pypi/v/tinycards.svg)](https://pypi.python.org/pypi/tinycards)
[![PyPI Status](https://img.shields.io/pypi/status/tinycards.svg)](https://pypi.python.org/pypi/tinycards)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An unofficial Python API for [Tinycards](https://tinycards.duolingo.com/) by Duolingo.


## Installation

### Install from PyPI

The easiest way to get started is to simple install the library like so:
```
$ pip install tinycards
```

### Install from source
If you want to modify the library's source code and try out your changes locally, you might want to consider building from source which works like follows:

1. Make sure Python with [Setuptools](https://pypi.python.org/pypi/setuptools) is installed.
2. From the project's root folder, install using pip:
```
$ pip install -e .
```

## Run Tests

1. In order to run the tests, you need to set the enviroment variables _TINYCARDS_IDENTIFIER_ and _TINYCARDS_PASSWORD_.
2. Then, from the project's root directory, simply start the _pytest_ test runner:
```
$ pytest 
```
3. When all tests were successful, _pytest_ will exit with 0.

## Usage

Below is a list of some of the most common functions.
For a more practical example, see the [csv_to_deck.py](https://github.com/floscha/tinycards-python-api/blob/master/examples/csv_to_deck.py) script.

### Initialise a new client

```python
>>> # A new client with the given identification (e.g., mail address) and password.
>>> client  = tinycards.Tinycards('identification', 'password')
'Logged in as 'username' (user@email.com)'
>>> # If no identification or password are specified, they are taken from ENV.
>>> client  = tinycards.Tinycards()
'Logged in as 'username' (user@email.com)'
```

### Get info about the currently logged in user.

```python
>>> user = client.get_user_info()
{
  username: 'bachman',
  email: 'bachman@aviato.com',
  fullname: 'Erlich Bachman',
  ...
}
```

### Get all decks of a user

```python
>>> all_decks = client.get_decks()
>>> [deck.title for deck in all_decks]
['Deck 1', 'Deck 2', 'Deck 3']
```

### Update an existing deck

```python
>>> deck_1 = client.find_deck_by_title('Deck 1')
>>> deck_1.title = 'Deck 1.1'
>>> client.update_deck(deck_1)
{
  'title': 'Deck 1.1',
  ...
}
```

### Delete an existing deck

```python
>>> deck = client.find_deck_by_title('Some Deck')
{
  'title': 'Some Deck',
  'id': '8176b324-addc-495d-aadc-fad005e5b439'
  ...
}
>>> client.delete_deck(deck.id)
{
  'title': 'Some Deck',
  'id': '8176b324-addc-495d-aadc-fad005e5b439'
  ...
}
>>> deck = client.find_deck_by_title('Some Deck')
None
```

## Release a new Version
1. Bump the version in `setup.py`.
2. Push a new tag to GitHub.
3. The [Travis build](https://travis-ci.org/floscha/tinycards-python-api) will deploy the release to [PyPI](https://pypi.org/project/tinycards/). 
