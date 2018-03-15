from tinycards.networking.rest_api import RestApi


class Tinycards(object):
    """The entry point class to the Tinycards Python API.

    Example:
        >>> import tinycards
        >>> tinycards_api = tinycards.Tinycards()

    Args:
        identifier (str): The Tinycards identifier to use for logging in.
            For example, a user's email address.
            Will be taken from ENV if not specified:
            .. envvar:: TINYCARDS_IDENTIFIER
        password (str): The user's password to login to Tinycards.
            Will be taken from ENV if not specified.
            .. envvar:: TINYCARDS_PASSWORD
    """

    def __init__(self,
                 identifier=None,
                 password=None):
        """Initialize a new instance of the Tinycards class."""
        self.data_source = RestApi()
        self.user_id = self.data_source.login(identifier, password)

    # --- Read user info.

    def get_user_info(self):
        """Get info data about the currently logged in user.

        Returns:
            user: A User object for the current user.

        """
        user_info = self.data_source.get_decks(self.user_id)

        return user_info

    # --- Get trends.

    def get_trends(self, types=None, limit=10, page=0, from_language='en'):
        """Get Tinycards trends for the current user.

        Args:
            types (list): What entities to retrieve.
                Can be DECK, DECK_GROUP or USER.
            limit: What number of results to should be returned.
            page: The page to return when returning more than limit results
                (zero-indexed).
            from_language: The language used for learning.

        Returns: A list of Trendable objects.

        """
        if not types:
            types = ['DECK', 'DECK_GROUP']

        trendables = self.data_source.get_trends(types, limit, page,
                                                 from_language)

        return trendables

    # --- Subscriptions

    def subscribe(self, user_id):
        """Subscribe to the given user.

        Args:
            user_id: ID of the user to subscribe to.

        Returns: If successful, returns the ID of the user subscribed to.

        """
        added_subscription = self.data_source.subscribe(user_id)

        return added_subscription

    def unsubscribe(self, user_id):
        """Unsubscribe the given user.

        Args:
            user_id: ID of the user to unsubscribe.

        Returns: If successful, returns the ID of the unsubscribed user.

        """
        removed_subscription = self.data_source.unsubscribe(user_id)

        return removed_subscription

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
            deck_id (Deck): The ID of the Deck to delete.

        Returns:
            Deck: The deleted Deck object if deletion was successful.

        """
        deleted_deck = self.data_source.delete_deck(deck_id)

        return deleted_deck

    # --- Favorites CR(U)D

    def get_favorites(self, user_id=None):
        """Get all favorites for the given user.

        Args:
            user_id (int): ID of the user to get favorites for.

        Returns:
            list: The list of retrieved decks.

        """
        if not user_id:
            user_id = self.user_id

        favorite_decks = self.data_source.get_favorites(user_id)

        return favorite_decks

    def add_favorite(self, deck_id):
        """Add a deck to the current user's favorites.

        Args:
            deck_id: The ID of the deck to be added.

        Returns:
            Favorite: The added favorite.

        """
        added_deck = self.data_source.add_favorite(self.user_id, deck_id)

        return added_deck

    def remove_favorite(self, favorite_id):
        """Add a deck to the current user's favorites.

        Args:
            favorite_id (str): The ID of the favorite to be removed.

        Returns:
            str: The ID of the removed favorite.

        """
        removed_favorite_id = self.data_source.remove_favorite(self.user_id,
                                                               favorite_id)

        return removed_favorite_id

    # --- Search

    def search(self,
               query,
               use_fuzzy_search=True,
               types=None,
               limit=10,
               page=0):
        """Searches for decks, deck groups, or users on Tinycards.

        Args:
            query (str): The used search term(s).
            use_fuzzy_search (bool): Whether or not to use fuzzy search.
            types (list): What entity to search for. Can be DECK, DECK_GROUP
                or USER.
            limit: Number of results to be returned.
            page: The page to return when more than `limit` results are
                available (zero-indexed).

        Returns: A list of Trendable objects.

        """
        trendables = self.data_source.search(query, use_fuzzy_search, types,
                                             limit, page)

        return trendables
