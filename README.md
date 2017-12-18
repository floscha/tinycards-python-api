# Tinycards Python API

<img src="temporary_logo.png" width="128">

An unofficial Python API for [Tinycards](https://tinycards.duolingo.com/) by Duolingo.


## Installation

1. Make sure Python (with pip) is installed.
2. Install dependencies from the requirements.txt (hint: requests is the only requirement right now):
```
$ pip install -r requirements.txt
```


## Usage

### Initialise a new client

```python
>>> # A new client with the given identification (e.g., mail address) and password.
>>> client  = tinycards.Tinycards('identification', 'password')
'Logged in as 'username' (user@email.com)'
>>> # If no identification or password are specified, they are taken from ENV.
>>> client  = tinycards.Tinycards()
'Logged in as 'username' (user@email.com)'
```

### Get all decks of a user

```python
>>> all_decks = tinycards.get_decks()
>>> [deck.title for deck in all_decks]
['Deck 1', 'Deck 2', 'Deck 3']
```
