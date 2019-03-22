from dataclasses import dataclass


@dataclass
class SearchableData:
    """The most important data fields of the Searchable class.

    Args:
        id: ID of the Deck or Deck-Set.
        name: Name of the Deck or Deck-Set.
        description: Textual description.
        average_freshness: The average freshness over all set's cards.
    """
    id: str
    name: str
    description: str
    average_freshness: float
