# Tinycards Python API

<img src="temporary_logo.png" width="128">

An unofficial Python API for [Tinycards](https://tinycards.duolingo.com/) by Duolingo.


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
