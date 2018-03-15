class Favorite(object):
    """A `Favorite` hold a `Deck` object along with some meta data."""

    def __init__(self, id_, deck):
        """Initialize a new instance of the `Favorite` class.

        Args:
            id_ (str): Unique identifier of the favorite.
            deck (Deck): The favorited deck.
        """
        self.id = id_
        self.deck = deck
