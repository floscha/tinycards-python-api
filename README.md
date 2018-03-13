<img src="temporary_logo.png" width="128">

# Tinycards Python API

[![Build Status](https://travis-ci.org/floscha/tinycards-python-api.svg?branch=master)](https://travis-ci.org/floscha/tinycards-python-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An unofficial Python API for [Tinycards](https://tinycards.duolingo.com/) by Duolingo.


## Installation

1. Make sure Python with [Setuptools](https://pypi.python.org/pypi/setuptools) is installed.
2. From the project's root folder, install using pip:
```
$ pip install .
```
3. Import in your Python code:
```python
import tinycards
```

## Run Tests

1. In order to run the tests, you need to set the enviroment variables _TINYCARDS_IDENTIFIER_ and _TINYCARDS_PASSWORD_.
2. Then, from the project's root directory, simply execute the test script:
```
$ python tests/integration_test.py 
```

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
