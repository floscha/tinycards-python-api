class SearchableData(object):
    """The most important data fields of the Searchable class."""

    def __init__(self,
                 id_,
                 name,
                 description,
                 average_freshness):
        """Initialize a new instance of the SearchableData class.

        Args:
            id_: ID of the Deck or Deck-Set.
            name: Name of the Deck or Deck-Set.
            description: Textual description.
            average_freshness: The average freshness over all set's cards.
        """
        self.id = id_
        self.name = name
        self.description = description
        self.average_freshness = average_freshness
