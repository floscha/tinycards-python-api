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
$ pip install .
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

## Release a new Version
1. Bump the version in `setup.py`.
2. Push a new tag to GitHub:
    1. `git tag 0.01`
    1. `git push origin 0.01`
3. The [Travis build](https://travis-ci.org/floscha/tinycards-python-api) will deploy the release to [PyPI](https://pypi.org/project/tinycards/). 

## Development

### Local setup

- Install `virtualenv` and create a so-called "virtual", dedicated environment for the `tinycards-python-api` project:

    ```console
    $ pip install -U virtualenv
    $ cd /path/to/tinycards-python-api
    $ virtualenv .
    $ source bin/activate
    (tinycards-python-api) $
    ```

- Install dependencies within the virtual environment:

    ```console
    (tinycards-python-api) $ pip install -e .
    (tinycards-python-api) $ pip install -r test-requirements.txt
    ```

- Develop and test at will.

- Leave the `virtualenv`:

    ```console
    (tinycards-python-api) $ deactivate
    $
    ```

### Run Tests

1. In order to run the _integration_ tests, you need to set the enviroment variables `TINYCARDS_IDENTIFIER` and `TINYCARDS_PASSWORD`.
   [`direnv`](https://direnv.net/) may be useful to set these automatically & permanently:

    ```console
    $ touch .envrc
    $ echo "export TINYCARDS_IDENTIFIER=<id>" >> .envrc
    $ echo "export TINYCARDS_PASSWORD=<pass>" >> .envrc
    $ direnv allow
    direnv: loading .envrc
    direnv: export +TINYCARDS_IDENTIFIER +TINYCARDS_PASSWORD
    ```

2. Then, from the project's root directory:

    1. run the unit tests:

        ```console
        $ pytest --ignore tests/client_test.py --ignore tests/integration_test.py --cov tinycards
        ```

    2. run all tests:
       **WARNING**: the integration tests **DELETE** all the decks in the account used to test. Please ensure you either are using a dedicated test account, or do not care about losing your existing decks.

        ```console
        $ pytest --cov tinycards
        ```

3. When all tests were successful, `pytest` will exit with `0`.
