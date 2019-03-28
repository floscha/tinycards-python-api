import sys

from tinycards import Deck, Tinycards


def _print_usage():
    print("Usage: tinycards decks {list, create} <deck_name>")


def _print_usage_and_exit():
    _print_usage()
    sys.exit(1)


def main():
    args = sys.argv[1:]

    if len(args) == 2 and args[0] == 'decks' and args[1] == 'list':
        client = Tinycards()
        decks = client.get_decks()
        if decks:
            for d in decks:
                print(d.title)
        else:
            print("No decks found.")
    elif len(args) == 3 and args[0] == 'decks' and args[1] == 'create':
        client = Tinycards()
        decks = client.create_deck(Deck(args[2]))
    else:
        _print_usage_and_exit()
