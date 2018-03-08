"""Example script for the Tinycards Python API that creates decks from CSV."""
import csv
from getpass import getpass
import os

from tinycards import Tinycards
from tinycards.model import Deck


def csv_to_deck(csv_path):
    """Creates a Tinycards deck from a CSV file.

    The CSV file is expected to have two columns named 'front' and 'back'.
    """
    # Create new deck.
    tinycards = Tinycards(user_identifier, user_password)
    deck = Deck('French Words', tinycards.user_id)
    deck = tinycards.create_deck(deck)

    # Extract data from CSV file.
    word_pairs = []
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            current_word_pair = (row['front'], row['back'])
            word_pairs.append(current_word_pair)

    # Populate deck with cards from CSV data.
    for pair in word_pairs:
        deck.add_card(pair)

    # Save changes to Tinycards.
    tinycards.update_deck(deck)


if __name__ == '__main__':
    # Take identifier and password from ENV or ask user if not set.
    user_identifier = os.environ.get('TINYCARDS_IDENTIFIER')
    if not user_identifier:
        print("Input identifier (e.g. email):")
        user_identifier = input()
    user_password = os.environ.get('TINYCARDS_PASSWORD')
    if not user_password:
        print("Input password:")
        user_password = getpass()

    csv_to_deck('examples/example.csv')
