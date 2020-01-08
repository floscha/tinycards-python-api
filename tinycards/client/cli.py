import sys
from getpass import getpass
from pathlib import Path

import typer

from tinycards.client import Tinycards
from tinycards.model import Deck
from tinycards.networking import RestApi


tmp_path = Path('/tmp/.tinycards')
user_path = tmp_path / 'user'
jwt_path = tmp_path / 'jwt'

app = typer.Typer()


def _get_api_from_env():
    try:
        user_id = int(user_path.read_text())
        jwt = jwt_path.read_text()
    except FileNotFoundError:
        print("Please login first. (Use \"tinycards login\")")
        sys.exit(1)
    return RestApi(jwt), user_id


@app.command()
def login(identifier: str = None):
    print("Logging in:")
    if identifier is None:
        identifier = input("Enter your username or email: ")
    password = getpass("Enter your password: ")
    data_source = RestApi()
    user_id = data_source.login(identifier, password)

    tmp_path.mkdir(exist_ok=True)
    user_path.write_text(str(user_id))
    jwt_path.write_text(data_source.jwt)


@app.command()
def logout():
    try:
        user_path.unlink()
        jwt_path.unlink()
        tmp_path.rmdir()
        print("Logged out")
    except FileNotFoundError:
        print("Logout failed. Maybe you weren't even logged in.")


def _list_decks():
    api, user_id = _get_api_from_env()
    decks = api.get_decks(user_id)
    if decks:
        for d in decks:
            print(d.title)
    else:
        print("No decks found.")


def _create_deck(deck_name: str):
    client = Tinycards(silent=True)
    decks = client.create_deck(Deck(deck_name))


@app.command()
def decks(action: str, deck_name: str = typer.Argument(None)):
    if action == 'list':
        _list_decks()
    elif action == 'create':
        _create_deck(deck_name)


if __name__ == '__main__':
    app()
