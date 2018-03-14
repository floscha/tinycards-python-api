class Trendable(object):
    """Represents a trending object on Tinycards."""

    def __init__(self, id_, type_, data):
        """Initialize a new instance of the Trendable class.

        Args:
            id_: ID of the entity.
            type_: The entity type (Can be DECK, DECK_GROUP or USER).
            data: All data fields of the Trendable.
        """
        self.id = id_
        self.type = type_
        self.data = data
