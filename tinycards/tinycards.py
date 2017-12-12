from networking.rest_api import RestApi


class Tinycards(object):
    """The entry point class to the Tinycards Python API.

    Example:
        >>> import tinycards
        >>> tinycards_api = tinycards.Tinycards()

    Args:
        identifier (str): The Tinycards identifier to use for logging in.
            For example, a user's email address.
            Will be taken from ENV if not specified:
            .. envvar:: IDENTIFIER
        password (str): The user's password to login to Tinycards.
            Will be taken from ENV if not specified.
            .. envvar:: PASSWORD
    """

    def __init__(self,
                 identifier=None,
                 password=None):
        """Initialize a new instance of the Tinycards class."""
        self.data_source = RestApi()
        self.user_id = self.data_source.login(identifier, password)

    # --- Deck CRUD

    def get_decks(self):
        """Get all Decks for the currently logged in user.

        Returns:
            list: The list of retrieved decks.

        """
        deck_previews = self.data_source.get_decks(self.user_id)

        return deck_previews

    def get_deck(self, deck_id, include_cards=True):
        """Get the Deck with the given ID.

        Args:
            deck_id (str): The ID of the deck to retrieve.
            include_cards (bool): Only include the cards of the deck when set
                to True (as by default). Otherwise cards will be an empty list.

        Returns:
            Deck: The retrieved deck.

        """
        deck = self.data_source.get_deck(deck_id, self.user_id, include_cards)

        return deck

    def find_deck_by_title(self, deck_title):
        """Find an existing deck by its name if it exists.

        Throws an exception if multiple decks with the same title exist.

        Args:
            deck_title (str): The title of the deck to retrieve.

        Returns:
            Deck: The retrieved deck if found. None otherwise.

        """
        all_decks = self.get_decks()
        found = [d for d in all_decks if d.title == deck_title]
        if len(found) == 0:
            return None
        elif len(found) == 1:
            return found[0]
        else:
            raise ValueError("Multiple decks with title '%s' found"
                             % deck_title)

    def create_deck(self, deck):
        """Create a new Deck for the currently logged in user.

        Args:
            deck (Deck): The Deck object to create.

        Returns:
            Deck: The created Deck object if creation was successful.

        """
        created_deck = self.data_source.create_deck(deck)

        return created_deck

    def update_deck(self, deck):
        """Update an existing deck.

        Args:
            deck (Deck): The Deck object to update.

        Returns:
            Deck: The updated Deck object if update was successful.

        """
        updated_deck = self.data_source.update_deck(deck)

        return updated_deck

    def delete_deck(self, deck_id):
        """Delete an existing deck.

        Args:
            deck (Deck): The Deck object to delete.

        Returns:
            Deck: The deleted Deck object if deletion was successful.

        """
        deleted_deck = self.data_source.delete_deck(deck_id)

        return deleted_deck
